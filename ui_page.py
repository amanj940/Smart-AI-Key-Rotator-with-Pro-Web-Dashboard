
def render_ui(joker_key, prov, lang, tabs, p_active_cnt, p_keys_cnt, avg_ms, total_cnt, routing_mode, ep_chat, ep_mod, rows, font_url):
    t = I18N.get(lang, I18N["ar"])
    s_smart = "selected" if routing_mode == "smart" else ""
    s_power = "selected" if routing_mode == "power" else ""
    lang_sw = "".join([f"<a href='/ui?prov={prov}&lang={c}' style='padding:4px 10px;border-radius:6px;text-decoration:none;font-size:12px;font-weight:700;background:{'#0284c7' if lang==c else '#1e293b'};color:#fff'>{lbl}</a>" for c, lbl in [("ar","AR"),("en","EN"),("ku","KU")]])
    empty_row = f"<tr><td colspan=9 style='text-align:center;color:#64748b;padding:24px'>{t['empty']}</td></tr>"
    css = f"""<link href="{font_url}" rel="stylesheet"><style>
    *{{box-sizing:border-box}}body{{font-family:'Vazirmatn',system-ui,sans-serif;background:#070b14;color:#f8fafc;max-width:1340px;margin:22px auto;padding:0 22px;line-height:1.6}}
    code,select,input[type=text]{{font-family:'JetBrains Mono','Vazirmatn',monospace}}
    .tabs{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:20px;border-bottom:1px solid #1e293b;padding-bottom:14px}}
    .tab{{text-decoration:none;color:#94a3b8;background:#0f172a;padding:10px 18px;border-radius:10px;border:1px solid #1e293b;font-weight:700;font-size:15px;display:flex;align-items:center;gap:8px}}
    .tab span{{background:#1e293b;color:#38bdf8;padding:2px 8px;border-radius:20px;font-size:12px}}
    .tab.active{{background:linear-gradient(135deg,#0284c7,#2563eb);color:#fff;border-color:#60a5fa}}.tab.active span{{background:rgba(0,0,0,.35);color:#fff}}
    .stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-bottom:20px}}
    .stat{{background:linear-gradient(145deg,#111827,#0b1120);border:1px solid #1e293b;padding:18px;border-radius:14px;font-size:14px;color:#94a3b8;font-weight:600}}
    .stat b{{font-size:28px;color:#38bdf8;display:block;margin-top:4px;font-weight:800}}
    .card{{background:#0f172a;border:1px solid #1e293b;padding:20px;border-radius:14px;margin-bottom:18px}}.card b{{font-size:17px;color:#f1f5f9}}
    .row{{display:flex;gap:10px;flex-wrap:wrap;align-items:center}}
    select,input[type=text]{{height:44px;padding:8px 14px;border-radius:9px;border:1.5px solid #334155;background:#070b14;color:#f8fafc;font-size:14px}}
    select option,select optgroup{{background:#0f172a;color:#f8fafc;font-size:14px}}
    button{{height:44px;padding:0 16px;border-radius:9px;background:#0284c7;border:none;color:#fff;cursor:pointer;font-family:'Vazirmatn',sans-serif;font-weight:700;font-size:14px}}
    .btn-p{{background:#7c3aed}}.btn-s{{background:#059669}}
    .btn-t{{background:#d97706;height:32px;padding:0 10px;font-size:12.5px}}.btn-g{{background:#334155;height:32px;padding:0 10px;font-size:12.5px}}.btn-d{{background:#dc2626;height:32px;padding:0 10px;font-size:12.5px}}
    table{{width:100%;border-collapse:collapse;margin-top:14px}}th{{background:#070b14;color:#94a3b8;font-size:13.5px;padding:12px 10px;text-align:{t['align']};border-bottom:2px solid #1e293b}}
    td{{padding:12px 10px;border-bottom:1px solid #1e293b;text-align:{t['align']};font-size:14px}}
    .ep-box{{background:#070b14;border:1px solid #1e293b;padding:12px 16px;border-radius:9px;font-size:13px;color:#93c5fd;direction:ltr;text-align:left;margin-top:12px}}
    #toast{{position:fixed;bottom:22px;left:22px;background:#1e293b;border:1.5px solid #38bdf8;padding:12px 20px;border-radius:10px;font-size:14px;font-weight:700;display:none;z-index:99}}
    </style>"""
    body = f"""<!DOCTYPE html><html lang={lang} dir={t['dir']}><head><meta charset=utf-8><title>{prov.upper()} - AI Router</title>{css}</head><body>
    <div style="background:#0f172a;border:1px solid #1e293b;border-radius:12px;padding:10px 16px;margin-bottom:14px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">
      <div style="display:flex;align-items:center;gap:10px"><span style="font-size:15px;font-weight:700;color:#f8fafc">{t['joker_title']}</span><span style="font-size:12px;color:#64748b;font-family:'JetBrains Mono',monospace">http://localhost:4000/v1 | auto-free</span></div>
      <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap"><input type=text id="jk-val" value="{joker_key}" readonly style="height:34px;width:300px;font-size:12.5px;color:#38bdf8;font-weight:600;direction:ltr;text-align:center;padding:0 8px"><button type=button class=btn-s style="height:34px;padding:0 12px;font-size:12.5px" onclick="navigator.clipboard.writeText(document.getElementById('jk-val').value);toast('{t['copied']}')">{t['copy']}</button><form method=post action=/ui/joker style="margin:0"><input type=hidden name=prov value={prov}><input type=hidden name=lang value={lang}><button type=submit class=btn-t style="height:34px;padding:0 12px;font-size:12.5px">{t['regen']}</button></form><div style="display:flex;gap:4px;margin-inline-start:8px;border-inline-start:1px solid #334155;padding-inline-start:10px">{lang_sw}</div></div>
    </div>
    <div class=tabs>{tabs}</div>
    <div class=stats><div class=stat>{t['active_keys']} ({prov.upper()})<b>{p_active_cnt} / {p_keys_cnt}</b></div><div class=stat>{t['avg_speed']} ({prov.upper()})<b style="color:#10b981">{avg_ms} ms</b></div><div class=stat>{t['total_keys']}<b style="color:#a855f7">{total_cnt} {t['keys_unit']}</b></div><div class=stat>{t['routing_mode']}<form method=post action=/ui/mode style="margin-top:6px"><input type=hidden name=prov value={prov}><input type=hidden name=lang value={lang}><select name=mode onchange="this.form.submit()" style="width:100%;height:38px"><option value=smart {s_smart}>{t['mode_smart']}</option><option value=power {s_power}>{t['mode_power']}</option></select></form></div></div>
    <div class=card><div class=row style="justify-content:space-between"><b>{t['manage_title']} — {prov.upper()}</b><div class=row><button type=button class=btn-s onclick="autoPick(true)">{t['auto_best']}</button><button type=button class=btn-p onclick="autoPick(false)">{t['bench_btn']}</button><button type=button class=btn-p onclick="testProvider()">{t['test_all']} ({p_keys_cnt})</button></div></div><div id="bench-box" style="margin-top:10px"></div><div class=ep-box>CHAT: {ep_chat}<br>MODELS: {ep_mod}</div>
      <div style="margin-top:16px;display:grid;grid-template-columns:1fr;gap:14px">
        <div style="background:#070b14;padding:14px;border-radius:10px;border:1px solid #1e293b"><div style="font-size:13.5px;color:#94a3b8;margin-bottom:8px;font-weight:700">{t['bulk_title']}</div><div class=row><input type=text placeholder="{t['search_ph']}" oninput="filterSel('bm',this.value)" style="width:220px"><select name=model id=bm form="f-bulk" style="flex:1;min-width:300px"></select><form id="f-bulk" method=post action=/ui/bulk class=row style="margin:0"><input type=hidden name=provider value={prov}><input type=hidden name=lang value={lang}><button type=button class=btn-p onclick="fetchLive()">{t['fetch_free']}</button><button type=submit class=btn-s>{t['apply_all']}</button></form></div></div>
        <div style="background:#070b14;padding:14px;border-radius:10px;border:1px solid #1e293b"><div style="font-size:13.5px;color:#94a3b8;margin-bottom:8px;font-weight:700">{t['add_title']}</div><form method=post action=/ui/add class=row><input type=hidden name=provider value={prov}><input type=hidden name=lang value={lang}><input type=text name=api_key placeholder="{t['key_ph']}" style="flex:1;min-width:260px" required><select name=model id=am style="min-width:300px"></select><button type=submit class=btn-s>{t['save_btn']}</button></form></div>
      </div>
    </div>
    <div class=card><div class=row style="justify-content:space-between"><b>{t['keys_list']} — {prov.upper()} ({p_keys_cnt})</b><select onchange="sortRows(this.value)" style="height:38px"><option value=idx>{t['sort_def']}</option><option value=fast>{t['sort_fast']}</option><option value=cap>{t['sort_cap']}</option></select></div>
      <table><thead><tr><th>#</th><th>{t['th_model']}</th><th>{t['th_cap']}</th><th>{t['th_spd']}</th><th>{t['th_stat']}</th><th>{t['th_stats']}</th><th>{t['th_last']}</th><th>{t['th_key']}</th><th>{t['th_act']}</th></tr></thead><tbody id=tb>{rows or empty_row}</tbody></table>
    </div><div id=toast></div>
    <script>const PROV="{prov}";const TXT={{"grp_pro":"{t['grp_pro']}","grp_fast":"{t['grp_fast']}","no_res":"{t['no_res']}","t_fetching":"{t['t_fetching']}","t_fetched":"{t['t_fetched']}","t_benching":"{t['t_benching']}","t_applied":"{t['t_applied']}","t_testing":"{t['t_testing']}"}};</script>"""
    return body
>{t['sort_fast']}</option><option value=cap>{t['sort_cap']}</option></select></div>
      <table><thead><tr><th>#</th><th>{t['th_model']}</th><th>{t['th_cap']}</th><th>{t['th_spd']}</th><th>{t['th_stat']}</th><th>{t['th_stats']}</th><th>{t['th_last']}</th><th>{t['th_key']}</th><th>{t['th_act']}</th></tr></thead><tbody id=tb>{rows or empty_row}</tbody></table>
    </div><div id=toast></div>
    <script>const PROV="{prov}";const TXT={{"grp_pro":"{t['grp_pro']}","grp_fast":"{t['grp_fast']}","no_res":"{t['no_res']}","t_fetching":"{t['t_fetching']}","t_fetched":"{t['t_fetched']}","t_benching":"{t['t_benching']}","t_applied":"{t['t_applied']}","t_testing":"{t['t_testing']}"}};</script>"""
    return body
