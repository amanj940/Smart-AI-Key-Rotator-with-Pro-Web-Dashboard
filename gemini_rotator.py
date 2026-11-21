import yaml, httpx, time, asyncio
from fastapi import FastAPI, Request, Form
from fastapi.responses import StreamingResponse, JSONResponse, HTMLResponse, RedirectResponse
import core_router as cr
from core_router import CONFIG_PATH, ENDPOINTS, MODELS_URLS, FONT_URL, ALL_KEYS, STATS, cap_score, reload_pool, pick_candidates

app = FastAPI()

@app.post("/ui/mode")
async def ui_mode(mode: str = Form(...), prov: str = Form("gemini")):
    cr.ROUTING_MODE = mode
    return RedirectResponse(f"/ui?prov={prov}", status_code=303)

@app.post("/ui/models")
async def ui_models(request: Request):
    d = await request.json()
    prov, key = d.get("provider", "gemini"), d.get("api_key", "").strip()
    if key == "USE_EXISTING": key = next((x["api_key"] for x in cr.ALL_KEYS if x["provider"] == prov), "")
    url = MODELS_URLS.get(prov)
    if not url or not key: return JSONResponse({"error": "لا يوجد مفتاح"})
    async with httpx.AsyncClient(timeout=20) as c: r = await c.get(url, headers={"Authorization": f"Bearer {key}"})
    if r.status_code != 200: return JSONResponse({"error": f"HTTP {r.status_code}"})
    pro_l, fast_l = [], []
    bad = ["embed", "tts", "whisper", "guard", "vision", "image", "orpheus", "audio", "aqa", "bisect", "1.0", "1.5"]
    for m in r.json().get("data", []):
        mid = m.get("id", "").replace("models/", "")
        low = mid.lower()
        if not mid or any(b in low for b in bad): continue
        if prov == "openrouter":
            pr = m.get("pricing", {})
            if not ((":free" in mid) or (str(pr.get("prompt")) == "0" and str(pr.get("completion")) == "0")): continue
        elif prov == "gemini" and not any(x in low for x in ["flash", "pro"]): continue
        sc = cap_score(mid)
        item = {"id": mid, "t": f"🆓 FREE | قدرة {sc}%", "sc": sc}
        (pro_l if sc >= 90 else fast_l).append(item)
    pro_l.sort(key=lambda x: (-x["sc"], x["id"]))
    fast_l.sort(key=lambda x: (-x["sc"], x["id"]))
    return JSONResponse({"pro": pro_l[:20], "fast": fast_l[:20]})

@app.post("/ui/autobench")
async def ui_autobench(request: Request):
    d = await request.json()
    prov, auto_apply = d.get("provider", "gemini"), d.get("apply", False)
    key = next((x["api_key"] for x in cr.ALL_KEYS if x["provider"] == prov and x["enabled"]), "")
    if not key: return JSONResponse({"error": "لا يوجد مفتاح نشط"})
    async with httpx.AsyncClient(timeout=20) as c: r = await c.get(MODELS_URLS[prov], headers={"Authorization": f"Bearer {key}"})
    if r.status_code != 200: return JSONResponse({"error": f"HTTP {r.status_code}"})
    cands = [m.get("id", "").replace("models/", "") for m in r.json().get("data", []) if m.get("id") and not any(b in m.get("id","").lower() for b in ["embed", "tts", "whisper", "guard", "vision", "image", "orpheus", "audio"])]
    if prov == "gemini": cands = [x for x in cands if any(k in x.lower() for k in ["flash", "pro"])]
    async def probe(client, mid):
        t0 = time.time()
        try:
            res = await client.post(ENDPOINTS[prov], headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"}, json={"model": mid, "messages": [{"role": "user", "content": "hi"}], "max_tokens": 5})
            ms = int((time.time() - t0) * 1000)
            if res.status_code == 200:
                sc = cap_score(mid)
                return {"id": mid, "ms": ms, "cap": sc, "score": round((sc * 1000) / max(ms, 100), 1)}
        except Exception: pass
        return None
    async with httpx.AsyncClient(timeout=15) as client: results = await asyncio.gather(*(probe(client, mid) for mid in cands[:12]))
    valid = sorted([x for x in results if x], key=lambda x: -x["score"])
    if valid and auto_apply:
        with open(CONFIG_PATH) as f: cfg = yaml.safe_load(f) or {"model_list": []}
        for m in cfg.get("model_list", []):
            if m["litellm_params"].get("provider", "gemini") == prov: m["litellm_params"]["model"] = valid[0]["id"]
        with open(CONFIG_PATH, "w") as f: yaml.safe_dump(cfg, f, allow_unicode=True)
        reload_pool()
    return JSONResponse({"models": valid, "applied": valid[0]["id"] if (valid and auto_apply) else None})

@app.post("/ui/test/{idx}")
async def ui_test(idx: int):
    x = cr.ALL_KEYS[idx]; k = x["api_key"]; t0 = time.time()
    try:
        async with httpx.AsyncClient(timeout=20) as c:
            r = await c.post(ENDPOINTS[x["provider"]], headers={"Authorization": f"Bearer {k}", "Content-Type": "application/json"}, json={"model": x["model"], "messages": [{"role": "user", "content": "hi"}], "max_tokens": 5})
        ms = int((time.time() - t0) * 1000); STATS[k]["last"] = time.strftime("%H:%M:%S")
        if r.status_code == 200:
            STATS[k].update({"ms": ms, "ok": STATS[k]["ok"] + 1, "cooldown": 0, "err": "200 OK"})
            return JSONResponse({"ok": True, "ms": ms, "status": "200 OK"})
        STATS[k].update({"fail": STATS[k]["fail"] + 1, "err": f"HTTP {r.status_code}"})
        return JSONResponse({"ok": False, "ms": ms, "status": f"HTTP {r.status_code}", "error": r.text[:160]})
    except Exception as e:
        STATS[k]["err"] = "Timeout"; return JSONResponse({"ok": False, "ms": 0, "status": "Error", "error": str(e)})

@app.post("/ui/toggle/{idx}")
async def ui_toggle(idx: int, prov: str = Form("gemini")):
    with open(CONFIG_PATH) as f: cfg = yaml.safe_load(f) or {"model_list": []}
    cfg["model_list"][idx]["litellm_params"]["enabled"] = not cfg["model_list"][idx]["litellm_params"].get("enabled", True)
    with open(CONFIG_PATH, "w") as f: yaml.safe_dump(cfg, f, allow_unicode=True)
    reload_pool(); return RedirectResponse(f"/ui?prov={prov}", status_code=303)

@app.post("/ui/bulk")
async def ui_bulk(provider: str = Form(...), model: str = Form(...)):
    with open(CONFIG_PATH) as f: cfg = yaml.safe_load(f) or {"model_list": []}
    for m in cfg.get("model_list", []):
        if m["litellm_params"].get("provider", "gemini") == provider: m["litellm_params"]["model"] = model.strip()
    with open(CONFIG_PATH, "w") as f: yaml.safe_dump(cfg, f, allow_unicode=True)
    reload_pool(); return RedirectResponse(f"/ui?prov={provider}", status_code=303)

@app.post("/ui/add")
async def ui_add(provider: str = Form(...), api_key: str = Form(...), model: str = Form(...)):
    with open(CONFIG_PATH) as f: cfg = yaml.safe_load(f) or {"model_list": []}
    cfg.setdefault("model_list", []).append({"model_name": "auto-free", "litellm_params": {"provider": provider, "model": model.strip(), "api_key": api_key.strip(), "enabled": True}})
    with open(CONFIG_PATH, "w") as f: yaml.safe_dump(cfg, f, allow_unicode=True)
    reload_pool(); return RedirectResponse(f"/ui?prov={provider}", status_code=303)

@app.post("/ui/delete")
async def ui_delete(index: int = Form(...), prov: str = Form("gemini")):
    with open(CONFIG_PATH) as f: cfg = yaml.safe_load(f) or {"model_list": []}
    cfg["model_list"].pop(index)
    with open(CONFIG_PATH, "w") as f: yaml.safe_dump(cfg, f, allow_unicode=True)
    reload_pool(); return RedirectResponse(f"/ui?prov={prov}", status_code=303)

@app.post("/v1/chat/completions")
async def chat(request: Request):
    orig = await request.json()
    for x in pick_candidates():
        k = x["api_key"]; body = {**orig, "model": x["model"]}; h = {"Authorization": f"Bearer {k}", "Content-Type": "application/json"}; t0 = time.time()
        if orig.get("stream"):
            c = httpx.AsyncClient(timeout=120)
            r = await c.send(c.build_request("POST", ENDPOINTS[x["provider"]], headers=h, json=body), stream=True)
            if r.status_code == 200:
                STATS[k].update({"ms": int((time.time() - t0) * 1000), "ok": STATS[k]["ok"] + 1, "err": "200 OK", "last": time.strftime("%H:%M:%S")})
                async def gen():
                    try:
                        async for ch in r.aiter_bytes(): yield ch
                    finally: await r.aclose(); await c.aclose()
                return StreamingResponse(gen(), media_type="text/event-stream")
            STATS[k].update({"fail": STATS[k]["fail"] + 1, "cooldown": time.time() + 120, "err": f"HTTP {r.status_code}"}); await r.aclose(); await c.aclose()
        else:
            async with httpx.AsyncClient(timeout=120) as c: r = await c.post(ENDPOINTS[x["provider"]], headers=h, json=body)
            if r.status_code == 200:
                STATS[k].update({"ms": int((time.time() - t0) * 1000), "ok": STATS[k]["ok"] + 1, "err": "200 OK", "last": time.strftime("%H:%M:%S")}); return JSONResponse(r.json())
            STATS[k].update({"fail": STATS[k]["fail"] + 1, "cooldown": time.time() + 120, "err": f"HTTP {r.status_code}"})
    return JSONResponse({"error": "All keys exhausted"}, status_code=429)

@app.get("/ui", response_class=HTMLResponse)
async def ui(prov: str = "gemini"):
    from ui_page import render_ui
    provs_list = [("gemini", "Google Gemini"), ("groq", "Groq"), ("openrouter", "OpenRouter"), ("cerebras", "Cerebras"), ("mistral", "Mistral")]
    tabs = "".join([f"<a href='/ui?prov={pid}' class='{'tab active' if pid==prov else 'tab'}'>{pname} <span>{sum(1 for x in cr.ALL_KEYS if x['provider']==pid)}</span></a>" for pid, pname in provs_list])
    p_keys = [(i, x) for i, x in enumerate(cr.ALL_KEYS) if x["provider"] == prov]
    p_active = [x for _, x in p_keys if x["enabled"]]
    avg_ms = int(sum(STATS[x["api_key"]]["ms"] for x in p_active) / len(p_active)) if p_active else 0
    now = time.time()
    rows = ""
    for local_no, (i, x) in enumerate(p_keys, 1):
        st = STATS.get(x["api_key"], {"ms": 500, "ok": 0, "fail": 0, "cooldown": 0, "err": "جاهز", "last": "-"})
        spd_col = "#10b981" if st["ms"] < 600 else ("#f59e0b" if st["ms"] < 1500 else "#ef4444")
        state_badge = "<span style='color:#94a3b8'>⏸️ موقوف</span>" if not x["enabled"] else (f"<span style='color:#f59e0b'>⏳ تهدئة ({int(st['cooldown']-now)}s)</span>" if st["cooldown"] > now else (f"<span style='color:#ef4444'>❌ {st['err']}</span>" if ("HTTP" in st["err"] or "Error" in st["err"]) else f"<span style='color:#10b981'>🟢 {st['err']}</span>"))
        rows += f"<tr data-idx='{i}' data-ms='{st['ms']}' data-cap='{x['cap']}' style='opacity:{'1' if x['enabled'] else '0.45'}'><td>{local_no}</td><td><code>{x['model']}</code></td><td><b>{x['cap']}%</b></td><td id='ms-{i}' style='color:{spd_col};font-weight:bold'>{st['ms']} ms</td><td id='st-{i}'>{state_badge}</td><td>✅ {st['ok']} / ❌ {st['fail']}</td><td>{st['last']}</td><td><code>{x['api_key'][:6]}...{x['api_key'][-4:]}</code></td><td style='display:flex;gap:6px'><button type=button class='btn-t' onclick='testOne({i})'>فحص</button><form method=post action=/ui/toggle/{i} style=margin:0><input type=hidden name=prov value={prov}><button type=submit class='btn-g'>{'إيقاف' if x['enabled'] else 'تفعيل'}</button></form><form method=post action=/ui/delete style=margin:0><input type=hidden name=index value={i}><input type=hidden name=prov value={prov}><button type=submit class='btn-d'>حذف</button></form></td></tr>"
    return render_ui(prov, tabs, len(p_active), len(p_keys), avg_ms, len(cr.ALL_KEYS), cr.ROUTING_MODE, ENDPOINTS.get(prov,""), MODELS_URLS.get(prov,""), rows, FONT_URL) + """<script>
    const PR={gemini:[{id:"gemini-flash-lite-latest",t:"🆓 FREE | 84%"},{id:"gemini-3.0-flash",t:"🆓 FREE | 84%"},{id:"gemini-2.5-pro",t:"🆓 FREE | 95%"}],groq:[{id:"qwen/qwen3.8-27b",t:"🆓 FREE | 95%"},{id:"openai/gpt-oss-120b",t:"🆓 FREE | 95%"}],openrouter:[{id:"nvidia/nemotron-3-nano-30b-a3b-reasoning:free",t:"🆓 FREE | 84%"},{id:"qwen/qwen3-coder:free",t:"🆓 FREE | 95%"}],cerebras:[{id:"llama3.1-8b",t:"🆓 FREE | 84%"}],mistral:[{id:"codestral-latest",t:"🆓 FREE | 84%"}]};
    function toast(m){const t=document.getElementById("toast");t.innerText=m;t.style.display="block";setTimeout(()=>t.style.display="none",3500)}
    let LAST_MODELS={pro:(PR[PROV]||[]).filter(x=>x.t.includes("95")),fast:(PR[PROV]||[]).filter(x=>!x.t.includes("95"))};
    function renderGroups(id,data,q=""){const s=document.getElementById(id);if(!s)return;q=q.toLowerCase();const p=(data.pro||[]).filter(x=>x.id.toLowerCase().includes(q)),f=(data.fast||[]).filter(x=>x.id.toLowerCase().includes(q));let h="";if(p.length)h+=`<optgroup label="🏆 نماذج قوية للبرمجة">`+p.map(x=>`<option value="${x.id}">${x.id} [${x.t}]</option>`).join("")+`</optgroup>`;if(f.length)h+=`<optgroup label="⚡ نماذج سريعة وخفيفة">`+f.map(x=>`<option value="${x.id}">${x.id} [${x.t}]</option>`).join("")+`</optgroup>`;s.innerHTML=h||`<option value="">لا توجد نتائج</option>`}
    function filterSel(id,q){renderGroups(id,LAST_MODELS,q)}renderGroups("bm",LAST_MODELS);renderGroups("am",LAST_MODELS);
    async function fetchLive(){toast("⏳ جاري فلترة وجلب النماذج المجانية...");const r=await fetch("/ui/models",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({provider:PROV,api_key:"USE_EXISTING"})});const d=await r.json();if(d.pro||d.fast){LAST_MODELS=d;renderGroups("bm",d);renderGroups("am",d);toast("✅ تم جلب "+((d.pro?.length||0)+(d.fast?.length||0))+" نموذج مصفّى!")}else toast("⚠️ "+(d.error||"خطأ"))}
    async function autoPick(apply){const box=document.getElementById("bench-box");box.innerHTML="<span style=color:#38bdf8>⏳ جاري قياس سرعة وقدرة النماذج المجانية...</span>";const r=await fetch("/ui/autobench",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({provider:PROV,apply:apply})});const d=await r.json();if(d.models&&d.models.length){let h="<table style=background:#070b14;border-radius:10px><tr><th>الترتيب</th><th>النموذج</th><th>القدرة</th><th>السرعة</th><th>الكفاءة</th></tr>";d.models.forEach((m,i)=>{const c=m.ms<700?"#10b981":(m.ms<1500?"#f59e0b":"#ef4444");h+=`<tr><td>${i===0?"🏆 #1":"#"+(i+1)}</td><td><code>${m.id}</code></td><td><b>${m.cap}%</b></td><td style="color:${c};font-weight:bold">${m.ms} ms</td><td>${m.score}</td></tr>`});box.innerHTML=h+"</table>";if(d.applied){toast("🏆 تم تطبيق الأفضل: "+d.applied);setTimeout(()=>location.reload(),1500)}}else box.innerHTML="<span style=color:#ef4444>⚠️ "+(d.error||"خطأ")+"</span>"}
    async function testOne(i){const msEl=document.getElementById("ms-"+i),stEl=document.getElementById("st-"+i);msEl.innerText="⏳...";const r=await fetch("/ui/test/"+i,{method:"POST"});const d=await r.json();if(d.ok){msEl.innerText=d.ms+" ms";msEl.style.color=d.ms<600?"#10b981":"#f59e0b";stEl.innerHTML="<span style=color:#10b981>🟢 "+d.status+"</span>";msEl.parentElement.dataset.ms=d.ms}else{msEl.innerText=d.ms+" ms";msEl.style.color="#ef4444";stEl.innerHTML="<span style=color:#ef4444>❌ "+d.status+"</span>"}}
    function testProvider(){const idxs=Array.from(document.querySelectorAll("#tb tr[data-idx]")).map(r=>r.dataset.idx);toast("⚡ فحص "+idxs.length+" مفتاح...");idxs.forEach(i=>testOne(i))}
    function sortRows(by){const tb=document.getElementById("tb"),rs=Array.from(tb.querySelectorAll("tr[data-idx]"));rs.sort((a,b)=>by==="fast"?a.dataset.ms-b.dataset.ms:(by==="cap"?b.dataset.cap-a.dataset.cap:a.children.innerText-b.children.innerText));rs.forEach(r=>tb.appendChild(r))}
    </script></body></html>"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=4000, log_level="warning")
