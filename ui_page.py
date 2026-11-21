def render_ui(joker_key, prov, tabs, p_active_cnt, p_keys_cnt, avg_ms, total_cnt, routing_mode, ep_chat, ep_mod, rows, font_url):
    s_smart = "selected" if routing_mode == "smart" else ""
    s_power = "selected" if routing_mode == "power" else ""
    empty_row = '<tr><td colspan=9 style="text-align:center;color:#64748b;padding:24px">لا توجد مفاتيح لهذا المزود بعد</td></tr>'
    return f"""<!DOCTYPE html><html lang=ar dir=rtl><head><meta charset=utf-8><title>{prov.upper()} - Pro Router</title>
    <link href="{font_url}" rel="stylesheet"><style>
    *{{box-sizing:border-box}}body{{font-family:'Cairo',system-ui,sans-serif;background:#070b14;color:#f8fafc;max-width:1340px;margin:28px auto;padding:0 22px;line-height:1.6}}
    code,select,input[type=text]{{font-family:'JetBrains Mono','Cairo',monospace}}
    .tabs{{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:24px;border-bottom:1px solid #1e293b;padding-bottom:16px}}
    .tab{{text-decoration:none;color:#94a3b8;background:#0f172a;padding:12px 22px;border-radius:12px;border:1px solid #1e293b;font-weight:700;font-size:16px;display:flex;align-items:center;gap:10px}}
    .tab span{{background:#1e293b;color:#38bdf8;padding:3px 10px;border-radius:20px;font-size:13px}}
    .tab.active{{background:linear-gradient(135deg,#0284c7,#2563eb);color:#fff;border-color:#60a5fa}}.tab.active span{{background:rgba(0,0,0,.35);color:#fff}}
    .stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin-bottom:22px}}
    .stat{{background:linear-gradient(145deg,#111827,#0b1120);border:1px solid #1e293b;padding:20px;border-radius:16px;font-size:15px;color:#94a3b8;font-weight:600}}
    .stat b{{font-size:30px;color:#38bdf8;display:block;margin-top:6px;font-weight:800}}
    .card{{background:#0f172a;border:1px solid #1e293b;padding:24px;border-radius:16px;margin-bottom:22px}}.card b{{font-size:18px;color:#f1f5f9}}
    .row{{display:flex;gap:12px;flex-wrap:wrap;align-items:center}}
    select,input[type=text]{{height:48px;padding:10px 16px;border-radius:10px;border:1.5px solid #334155;background:#070b14;color:#f8fafc;font-size:15px}}
    select option,select optgroup{{background:#0f172a;color:#f8fafc;font-size:15px}}
    button{{height:46px;padding:0 18px;border-radius:10px;background:#0284c7;border:none;color:#fff;cursor:pointer;font-family:'Cairo',sans-serif;font-weight:700;font-size:14.5px}}
    .btn-p{{background:#7c3aed}}.btn-s{{background:#059669}}
    .btn-t{{background:#d97706;height:34px;padding:0 12px;font-size:13px}}.btn-g{{background:#334155;height:34px;padding:0 12px;font-size:13px}}.btn-d{{background:#dc2626;height:34px;padding:0 12px;font-size:13px}}
    table{{width:100%;border-collapse:collapse;margin-top:16px}}th{{background:#070b14;color:#94a3b8;font-size:14px;padding:14px 12px;text-align:right;border-bottom:2px solid #1e293b}}
    td{{padding:14px 12px;border-bottom:1px solid #1e293b;text-align:right;font-size:14.5px}}
    .ep-box{{background:#070b14;border:1px solid #1e293b;padding:14px 18px;border-radius:10px;font-size:13.5px;color:#93c5fd;direction:ltr;text-align:left;margin-top:14px}}
    #toast{{position:fixed;bottom:24px;left:24px;background:#1e293b;border:1.5px solid #38bdf8;padding:14px 24px;border-radius:12px;font-size:15px;font-weight:700;display:none}}
    </style></head><body>
    <div style="background:#0f172a;border:1px solid #1e293b;border-radius:12px;padding:10px 18px;margin-bottom:16px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-size:15px;font-weight:700;color:#f8fafc">🃏 مفتاح الجوكر الموحد:</span>
        <span style="font-size:12px;color:#64748b;font-family:'JetBrains Mono',monospace">http://localhost:4000/v1 | auto-free</span>
      </div>
      <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
        <input type=text id="jk-val" value="{joker_key}" readonly style="height:36px;width:320px;font-size:13px;color:#38bdf8;font-weight:600;direction:ltr;text-align:center;padding:0 10px">
        <button type=button class=btn-s style="height:36px;padding:0 14px;font-size:13px" onclick="navigator.clipboard.writeText(document.getElementById('jk-val').value);toast('📋 تم نسخ مفتاح الجوكر!')">📋 نسخ</button>
        <form method=post action=/ui/joker style="margin:0"><input type=hidden name=prov value={prov}><button type=submit class=btn-t style="height:36px;padding:0 14px;font-size:13px">🔄 تجديد</button></form>
      </div>
    </div>
    <div class=tabs>{tabs}</div>
    <div class=stats>
      <div class=stat>مفاتيح {prov.upper()} النشطة<b>{p_active_cnt} / {p_keys_cnt}</b></div>
      <div class=stat>متوسط سرعة {prov.upper()}<b style="color:#10b981">{avg_ms} ms</b></div>
      <div class=stat>إجمالي كل المزودين<b style="color:#a855f7">{total_cnt} مفتاح</b></div>
      <div class=stat>استراتيجية التوجيه<form method=post action=/ui/mode style="margin-top:6px"><input type=hidden name=prov value={prov}><select name=mode onchange="this.form.submit()" style="width:100%"><option value=smart {s_smart}>⚡ توازن ذكي</option><option value=power {s_power}>🚀 الأقوى برمجياً</option></select></form></div>
    </div>
    <div class=card>
      <div class=row style="justify-content:space-between"><b>🌐 إدارة النماذج ونقاط الاتصال لـ {prov.upper()}</b>
      <div class=row><button type=button class=btn-s onclick="autoPick(true)">🚀 اختيار وتطبيق الأسرع والأقوى تلقائياً</button><button type=button class=btn-p onclick="autoPick(false)">📊 مقارنة سرعة النماذج</button><button type=button class=btn-p onclick="testProvider()">⚡ فحص المفاتيح ({p_keys_cnt})</button></div></div>
      <div id="bench-box" style="margin-top:12px"></div>
      <div class=ep-box>CHAT: {ep_chat}<br>MODELS: {ep_mod}</div>
      <div style="margin-top:18px;display:grid;grid-template-columns:1fr;gap:16px">
        <div style="background:#070b14;padding:16px;border-radius:12px;border:1px solid #1e293b">
          <div style="font-size:14px;color:#94a3b8;margin-bottom:10px;font-weight:700">🔄 تحديث نموذج كل مفاتيح {prov.upper()} (قائمة منظمة + بحث فوري)</div>
          <div class=row><input type=text placeholder="🔍 ابحث عن نموذج..." oninput="filterSel('bm',this.value)" style="width:240px"><select name=model id=bm form="f-bulk" style="flex:1;min-width:340px"></select><form id="f-bulk" method=post action=/ui/bulk class=row style="margin:0"><input type=hidden name=provider value={prov}><button type=button class=btn-p onclick="fetchLive()">كشف النماذج المجانية</button><button type=submit class=btn-s>تطبيق على الكل</button></form></div>
        </div>
        <div style="background:#070b14;padding:16px;border-radius:12px;border:1px solid #1e293b">
          <div style="font-size:14px;color:#94a3b8;margin-bottom:10px;font-weight:700">➕ إضافة مفتاح {prov.upper()} جديد</div>
          <form method=post action=/ui/add class=row><input type=hidden name=provider value={prov}><input type=text name=api_key placeholder="الصق المفتاح هنا..." style="flex:1;min-width:280px" required><select name=model id=am style="min-width:340px"></select><button type=submit class=btn-s>+ حفظ وتفعيل</button></form>
        </div>
      </div>
    </div>
    <div class=card><div class=row style="justify-content:space-between"><b>🔑 مفاتيح {prov.upper()} ({p_keys_cnt})</b><select onchange="sortRows(this.value)"><option value=idx>الترتيب الافتراضي</option><option value=fast>⚡ الأسرع استجابة أولاً</option><option value=cap>🧠 الأقوى قدرة أولاً</option></select></div>
      <table><thead><tr><th>#</th><th>النموذج</th><th>القدرة</th><th>السرعة</th><th>الحالة</th><th>الإحصاء</th><th>آخر فحص</th><th>المفتاح</th><th>إجراءات</th></tr></thead><tbody id=tb>{rows or empty_row}</tbody></table>
    </div><div id=toast></div>
    <script>const PROV="{prov}";</script>"""
