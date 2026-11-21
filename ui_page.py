import json

I18N = {
    "ar": {
        "dir": "rtl", "align": "right",
        "joker_title": "🃏 مفتاح الجوكر الموحد",
        "copy": "📋 نسخ", "copied": "📋 تم نسخ مفتاح الجوكر!", "regen": "🔄 تجديد",
        "active_keys": "المفاتيح النشطة", "avg_speed": "متوسط السرعة",
        "total_keys": "إجمالي كل المزودين", "keys_unit": "مفتاح",
        "routing_mode": "استراتيجية التوجيه",
        "mode_smart": "⚡ توازن ذكي", "mode_power": "🚀 الأقوى برمجياً",
        "manage_title": "🌐 إدارة النماذج ونقاط الاتصال",
        "auto_best": "🚀 اختيار وتطبيق الأفضل تلقائياً",
        "bench_btn": "📊 مقارنة النماذج", "test_all": "⚡ فحص المفاتيح",
        "bulk_title": "🔄 تحديث نموذج جميع المفاتيح",
        "search_ph": "🔍 ابحث عن نموذج...", "fetch_free": "كشف النماذج المجانية",
        "apply_all": "تطبيق على الكل", "add_title": "➕ إضافة مفتاح جديد",
        "key_ph": "الصق مفتاح الـ API هنا...", "save_btn": "+ حفظ وتفعيل",
        "keys_list": "🔑 قائمة المفاتيح", "sort_def": "الترتيب الافتراضي",
        "sort_fast": "⚡ الأسرع استجابة", "sort_cap": "🧠 الأقوى قدرة",
        "th_model": "النموذج", "th_cap": "القدرة", "th_spd": "السرعة",
        "th_stat": "الحالة", "th_stats": "الإحصاء", "th_last": "آخر فحص",
        "th_key": "المفتاح", "th_act": "إجراءات",
        "btn_test": "فحص", "btn_stop": "إيقاف", "btn_start": "تفعيل", "btn_del": "حذف",
        "st_ready": "جاهز", "st_paused": "موقوف", "st_cool": "تهدئة",
        "empty": "لا توجد مفاتيح مضافة لهذا المزود بعد",
        "grp_pro": "🏆 نماذج قوية للبرمجة", "grp_fast": "⚡ نماذج سريعة وخفيفة",
        "no_res": "لا توجد نتائج مطابقة",
        "t_fetching": "⏳ جاري جلب وتصفية النماذج...", "t_fetched": "✅ تم جلب النماذج المجانية!",
        "t_benching": "⏳ جاري قياس سرعة وقدرة النماذج...", "t_applied": "🏆 تم تطبيق النموذج الأفضل: ",
        "t_testing": "⚡ جاري فحص المفاتيح..."
    },
    "en": {
        "dir": "ltr", "align": "left",
        "joker_title": "🃏 Master Joker Key",
        "copy": "📋 Copy", "copied": "📋 Joker key copied!", "regen": "🔄 Rotate",
        "active_keys": "Active Keys", "avg_speed": "Avg Latency",
        "total_keys": "Total Pool Keys", "keys_unit": "Keys",
        "routing_mode": "Routing Strategy",
        "mode_smart": "⚡ Smart Balance", "mode_power": "🚀 Coding Power",
        "manage_title": "🌐 Models & Endpoints Manager",
        "auto_best": "🚀 Auto-Pick & Apply Best",
        "bench_btn": "📊 Benchmark Models", "test_all": "⚡ Test Keys",
        "bulk_title": "🔄 Bulk Update Provider Model",
        "search_ph": "🔍 Search model...", "fetch_free": "Fetch Free Models",
        "apply_all": "Apply to All", "add_title": "➕ Add New API Key",
        "key_ph": "Paste API key here...", "save_btn": "+ Save & Activate",
        "keys_list": "🔑 Managed Keys", "sort_def": "Default Order",
        "sort_fast": "⚡ Fastest First", "sort_cap": "🧠 Highest Power",
        "th_model": "Model", "th_cap": "Power", "th_spd": "Latency",
        "th_stat": "Status", "th_stats": "Stats", "th_last": "Last Check",
        "th_key": "Key", "th_act": "Actions",
        "btn_test": "Test", "btn_stop": "Pause", "btn_start": "Enable", "btn_del": "Delete",
        "st_ready": "Ready", "st_paused": "Paused", "st_cool": "Cooldown",
        "empty": "No keys added for this provider yet",
        "grp_pro": "🏆 High-Power Coding Models", "grp_fast": "⚡ Fast & Lightweight Models",
        "no_res": "No matching models",
        "t_fetching": "⏳ Fetching free models...", "t_fetched": "✅ Free models loaded!",
        "t_benching": "⏳ Benchmarking speed & power...", "t_applied": "🏆 Applied best model: ",
        "t_testing": "⚡ Testing keys..."
    },
    "ku": {
        "dir": "rtl", "align": "right",
        "joker_title": "🃏 کلیلی جۆکەری سەرەکی",
        "copy": "📋 کۆپی", "copied": "📋 کلیلی جۆکەر کۆپی کرا!", "regen": "🔄 نوێکردنەوە",
        "active_keys": "کلیلە چالاکەکان", "avg_speed": "تێکڕای خێرایی",
        "total_keys": "کۆی گشتی کلیلەکان", "keys_unit": "کلیل",
        "routing_mode": "ستراتیژی دابەشکردن",
        "mode_smart": "⚡ هاوسەنگی زیرەک", "mode_power": "🚀 بەهێزترین بۆ کۆد",
        "manage_title": "🌐 بەڕێوەبردنی مۆدێل و بەستەرەکان",
        "auto_best": "🚀 هەڵبژاردنی باشترین بە شێوەی خۆکار",
        "bench_btn": "📊 بەراوردکردنی مۆدێلەکان", "test_all": "⚡ پشکنینی کلیلەکان",
        "bulk_title": "🔄 گۆڕینی مۆدێلی هەموو کلیلەکان",
        "search_ph": "🔍 گەڕان بۆ مۆدێل...", "fetch_free": "هێنانی مۆدێلە خۆڕاییەکان",
        "apply_all": "جێبەجێکردن بۆ هەمووان", "add_title": "➕ زیادکردنی کلیلی نوێ",
        "key_ph": "کلیلی API لێرە دابنێ...", "save_btn": "+ پاشەکەوتکردن",
        "keys_list": "🔑 لیستی کلیلەکان", "sort_def": "ڕیزبەندی بنەڕەتی",
        "sort_fast": "⚡ خێراترین وەڵامدانەوە", "sort_cap": "🧠 بەهێزترین توانا",
        "th_model": "مۆدێل", "th_cap": "توانا", "th_spd": "خێرایی",
        "th_stat": "دۆخ", "th_stats": "ئامار", "th_last": "دوا پشکنین",
        "th_key": "کلیل", "th_act": "کردارەکان",
        "btn_test": "پشکنین", "btn_stop": "وەستاندن", "btn_start": "چالاککردن", "btn_del": "سڕینەوە",
        "st_ready": "ئامادە", "st_paused": "وەستاو", "st_cool": "پشوودان",
        "empty": "هیچ کلیلێک بۆ ئەم دابینکەرە زیاد نەکراوە",
        "grp_pro": "🏆 مۆدێلە بەهێزەکان بۆ کۆد", "grp_fast": "⚡ مۆدێلە خێرا و سووکەکان",
        "no_res": "هیچ ئەنجامێک نەدۆزرایەوە",
        "t_fetching": "⏳ هێنانی مۆدێلە خۆڕاییەکان...", "t_fetched": "✅ مۆدێلەکان بارکران!",
        "t_benching": "⏳ پێوانەکردنی خێرایی و توانا...", "t_applied": "🏆 باشترین مۆدێل جێبەجێ کرا: ",
        "t_testing": "⚡ پشکنینی کلیلەکان..."
    }
}

TEMPLATE = """<!DOCTYPE html><html lang=__LANG__ dir=__DIR__><head><meta charset=utf-8><title>__PROV__ - AI Router</title>
<link href="__FONT__" rel="stylesheet"><style>
*{box-sizing:border-box}body{font-family:'Vazirmatn',system-ui,sans-serif;background:#070b14;color:#f8fafc;max-width:1340px;margin:22px auto;padding:0 22px;line-height:1.6}
code,select,input[type=text]{font-family:'JetBrains Mono','Vazirmatn',monospace}
.tabs{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:20px;border-bottom:1px solid #1e293b;padding-bottom:14px}
.tab{text-decoration:none;color:#94a3b8;background:#0f172a;padding:10px 18px;border-radius:10px;border:1px solid #1e293b;font-weight:700;font-size:15px;display:flex;align-items:center;gap:8px}
.tab span{background:#1e293b;color:#38bdf8;padding:2px 8px;border-radius:20px;font-size:12px}
.tab.active{background:linear-gradient(135deg,#0284c7,#2563eb);color:#fff;border-color:#60a5fa}.tab.active span{background:rgba(0,0,0,.35);color:#fff}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-bottom:20px}
.stat{background:linear-gradient(145deg,#111827,#0b1120);border:1px solid #1e293b;padding:18px;border-radius:14px;font-size:14px;color:#94a3b8;font-weight:600}
.stat b{font-size:28px;color:#38bdf8;display:block;margin-top:4px;font-weight:800}
.card{background:#0f172a;border:1px solid #1e293b;padding:20px;border-radius:14px;margin-bottom:18px}.card b{font-size:17px;color:#f1f5f9}
.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
select,input[type=text]{height:44px;padding:8px 14px;border-radius:9px;border:1.5px solid #334155;background:#070b14;color:#f8fafc;font-size:14px}
select option,select optgroup{background:#0f172a;color:#f8fafc;font-size:14px}
button{height:44px;padding:0 16px;border-radius:9px;background:#0284c7;border:none;color:#fff;cursor:pointer;font-family:'Vazirmatn',sans-serif;font-weight:700;font-size:14px}
.btn-p{background:#7c3aed}.btn-s{background:#059669}
.btn-t{background:#d97706;height:32px;padding:0 10px;font-size:12.5px}.btn-g{background:#334155;height:32px;padding:0 10px;font-size:12.5px}.btn-d{background:#dc2626;height:32px;padding:0 10px;font-size:12.5px}
table{width:100%;border-collapse:collapse;margin-top:14px}th{background:#070b14;color:#94a3b8;font-size:13.5px;padding:12px 10px;text-align:__ALIGN__;border-bottom:2px solid #1e293b}
td{padding:12px 10px;border-bottom:1px solid #1e293b;text-align:__ALIGN__;font-size:14px}
.ep-box{background:#070b14;border:1px solid #1e293b;padding:12px 16px;border-radius:9px;font-size:13px;color:#93c5fd;direction:ltr;text-align:left;margin-top:12px}
#toast{position:fixed;bottom:22px;left:22px;background:#1e293b;border:1.5px solid #38bdf8;padding:12px 20px;border-radius:10px;font-size:14px;font-weight:700;display:none;z-index:99}
</style></head><body>
<div style="background:#0f172a;border:1px solid #1e293b;border-radius:12px;padding:10px 16px;margin-bottom:14px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">
  <div style="display:flex;align-items:center;gap:10px"><span style="font-size:15px;font-weight:700;color:#f8fafc">__JOKER_TITLE__</span><span style="font-size:12px;color:#64748b;font-family:'JetBrains Mono',monospace">http://localhost:4000/v1 | auto-free</span></div>
  <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap"><input type=text id="jk-val" value="__JOKER_KEY__" readonly style="height:34px;width:300px;font-size:12.5px;color:#38bdf8;font-weight:600;direction:ltr;text-align:center;padding:0 8px"><button type=button class=btn-s style="height:34px;padding:0 12px;font-size:12.5px" onclick="navigator.clipboard.writeText(document.getElementById('jk-val').value);toast('__COPIED__')">__COPY__</button><form method=post action=/ui/joker style="margin:0"><input type=hidden name=prov value=__PROV_LOW__><input type=hidden name=lang value=__LANG__><button type=submit class=btn-t style="height:34px;padding:0 12px;font-size:12.5px">__REGEN__</button></form><div style="display:flex;gap:4px;margin-inline-start:8px;border-inline-start:1px solid #334155;padding-inline-start:10px">__LANG_SW__</div></div>
</div>
<div class=tabs>__TABS__</div>
<div class=stats><div class=stat>__ACTIVE_KEYS__ (__PROV__)<b>__P_ACT__ / __P_ALL__</b></div><div class=stat>__AVG_SPEED__ (__PROV__)<b style="color:#10b981">__AVG_MS__ ms</b></div><div class=stat>__TOTAL_KEYS__<b style="color:#a855f7">__TOTAL_CNT__ __KEYS_UNIT__</b></div><div class=stat>__ROUTING_MODE__<form method=post action=/ui/mode style="margin-top:6px"><input type=hidden name=prov value=__PROV_LOW__><input type=hidden name=lang value=__LANG__><select name=mode onchange="this.form.submit()" style="width:100%;height:38px"><option value=smart __S_SMART__>__MODE_SMART__</option><option value=power __S_POWER__>__MODE_POWER__</option></select></form></div></div>
<div class=card><div class=row style="justify-content:space-between"><b>__MANAGE_TITLE__ — __PROV__</b><div class=row><button type=button class=btn-s onclick="autoPick(true)">__AUTO_BEST__</button><button type=button class=btn-p onclick="autoPick(false)">__BENCH_BTN__</button><button type=button class=btn-p onclick="testProvider()">__TEST_ALL__ (__P_ALL__)</button></div></div><div id="bench-box" style="margin-top:10px"></div><div class=ep-box>CHAT: __EP_CHAT__<br>MODELS: __EP_MOD__</div>
  <div style="margin-top:16px;display:grid;grid-template-columns:1fr;gap:14px">
    <div style="background:#070b14;padding:14px;border-radius:10px;border:1px solid #1e293b"><div style="font-size:13.5px;color:#94a3b8;margin-bottom:8px;font-weight:700">__BULK_TITLE__</div><div class=row><input type=text placeholder="__SEARCH_PH__" oninput="filterSel('bm',this.value)" style="width:220px"><select name=model id=bm form="f-bulk" style="flex:1;min-width:300px"></select><form id="f-bulk" method=post action=/ui/bulk class=row style="margin:0"><input type=hidden name=provider value=__PROV_LOW__><input type=hidden name=lang value=__LANG__><button type=button class=btn-p onclick="fetchLive()">__FETCH_FREE__</button><button type=submit class=btn-s>__APPLY_ALL__</button></form></div></div>
    <div style="background:#070b14;padding:14px;border-radius:10px;border:1px solid #1e293b"><div style="font-size:13.5px;color:#94a3b8;margin-bottom:8px;font-weight:700">__ADD_TITLE__</div><form method=post action=/ui/add class=row><input type=hidden name=provider value=__PROV_LOW__><input type=hidden name=lang value=__LANG__><input type=text name=api_key placeholder="__KEY_PH__" style="flex:1;min-width:260px" required><select name=model id=am style="min-width:300px"></select><button type=submit class=btn-s>__SAVE_BTN__</button></form></div>
  </div>
</div>
<div class=card><div class=row style="justify-content:space-between"><b>__KEYS_LIST__ — __PROV__ (__P_ALL__)</b><select onchange="sortRows(this.value)" style="height:38px"><option value=idx>__SORT_DEF__</option><option value=fast>__SORT_FAST__</option><option value=cap>__SORT_CAP__</option></select></div>
  <table><thead><tr><th>#</th><th>__TH_MODEL__</th><th>__TH_CAP__</th><th>__TH_SPD__</th><th>__TH_STAT__</th><th>__TH_STATS__</th><th>__TH_LAST__</th><th>__TH_KEY__</th><th>__TH_ACT__</th></tr></thead><tbody id=tb>__ROWS__</tbody></table>
</div><div id=toast></div>
<script>const PROV="__PROV_LOW__";const TXT=__TXT_JSON__;</script>"""

def render_ui(joker_key, prov, lang, tabs, p_active_cnt, p_keys_cnt, avg_ms, total_cnt, routing_mode, ep_chat, ep_mod, rows, font_url):
    t = I18N.get(lang, I18N["ar"])
    lang_sw = "".join([f"<a href='/ui?prov={prov}&lang={c}' style='padding:4px 10px;border-radius:6px;text-decoration:none;font-size:12px;font-weight:700;background:{'#0284c7' if lang==c else '#1e293b'};color:#fff'>{lbl}</a>" for c, lbl in [("ar","AR"),("en","EN"),("ku","KU")]])
    empty_row = f"<tr><td colspan=9 style='text-align:center;color:#64748b;padding:24px'>{t['empty']}</td></tr>"
    rep = {
        "__LANG__": lang, "__DIR__": t["dir"], "__ALIGN__": t["align"], "__PROV__": prov.upper(), "__PROV_LOW__": prov,
        "__FONT__": font_url, "__JOKER_KEY__": joker_key, "__LANG_SW__": lang_sw, "__TABS__": tabs,
        "__P_ACT__": str(p_active_cnt), "__P_ALL__": str(p_keys_cnt), "__AVG_MS__": str(avg_ms),
        "__TOTAL_CNT__": str(total_cnt), "__S_SMART__": "selected" if routing_mode == "smart" else "",
        "__S_POWER__": "selected" if routing_mode == "power" else "", "__EP_CHAT__": ep_chat, "__EP_MOD__": ep_mod,
        "__ROWS__": rows or empty_row, "__TXT_JSON__": json.dumps(t),
        "__JOKER_TITLE__": t["joker_title"], "__COPIED__": t["copied"], "__COPY__": t["copy"], "__REGEN__": t["regen"],
        "__ACTIVE_KEYS__": t["active_keys"], "__AVG_SPEED__": t["avg_speed"], "__TOTAL_KEYS__": t["total_keys"],
        "__KEYS_UNIT__": t["keys_unit"], "__ROUTING_MODE__": t["routing_mode"], "__MODE_SMART__": t["mode_smart"],
        "__MODE_POWER__": t["mode_power"], "__MANAGE_TITLE__": t["manage_title"], "__AUTO_BEST__": t["auto_best"],
        "__BENCH_BTN__": t["bench_btn"], "__TEST_ALL__": t["test_all"], "__BULK_TITLE__": t["bulk_title"],
        "__SEARCH_PH__": t["search_ph"], "__FETCH_FREE__": t["fetch_free"], "__APPLY_ALL__": t["apply_all"],
        "__ADD_TITLE__": t["add_title"], "__KEY_PH__": t["key_ph"], "__SAVE_BTN__": t["save_btn"],
        "__KEYS_LIST__": t["keys_list"], "__SORT_DEF__": t["sort_def"], "__SORT_FAST__": t["sort_fast"],
        "__SORT_CAP__": t["sort_cap"], "__TH_MODEL__": t["th_model"], "__TH_CAP__": t["th_cap"],
        "__TH_SPD__": t["th_spd"], "__TH_STAT__": t["th_stat"], "__TH_STATS__": t["th_stats"],
        "__TH_LAST__": t["th_last"], "__TH_KEY__": t["th_key"], "__TH_ACT__": t["th_act"],
    }
    html = TEMPLATE
    for k, v in rep.items():
        html = html.replace(k, v)
    return html
