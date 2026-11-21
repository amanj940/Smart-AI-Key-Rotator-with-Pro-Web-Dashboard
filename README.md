# 🚀 Smart AI Key Rotator & Pro Web Dashboard

**A local intelligent multi-provider AI API key router & load balancer** supporting **Google Gemini, Groq, OpenRouter, Cerebras, and Mistral** with a modern Pro Web Dashboard, Master Joker Key authentication, live speed benchmarking, and multi-language support (**English / کوردی / العربية**).

---

## 🇬🇧 English Documentation

### ✨ Key Features
- **🃏 Master Joker API Key:** Single unified API key (`sk-joker-...`) to connect **OpenCode**, **Cline / Roo Code**, **Open WebUI**, **n8n**, or any OpenAI-compatible client securely.
- **🌍 Ultra-Pro Multi-Language UI (EN / KU / AR):** Instant zero-duplication language switcher with automatic `LTR / RTL` layout and **Vazirmatn** typography.
- **⚡ Auto-Benchmark & Smart Routing:** Live latency (`ms`) and coding capability scoring (`%`) to automatically select and apply the fastest & strongest free models.
- **🛡️ Auto-Cooldown Failover:** Automatically bypasses rate-limited (`429`) or failing keys without interrupting your workflow.
- **⚙️ Background Systemd Service:** Auto-starts on boot and self-heals on failure.

### 🛠️ Quick Installation
```bash
git clone https://github.com
cd Smart-AI-Key-Rotator-with-Pro-Web-Dashboard
chmod +x install.sh && ./install.sh
```

1. Open the dashboard in your browser: **`http://localhost:4000/ui`**
2. Copy your **Master Joker Key (`sk-joker-...`)** from the top bar.
3. Connect any AI application using:
   - **Base URL:** `http://localhost:4000/v1`
   - **API Key:** `sk-joker-xxxxxxxxxxxxxxxx`
   - **Model:** `auto-free`

---

## ☀️ کوردی (سۆرانی)

### ✨ تایبەتمەندییە سەرەکییەکان
- **🃏 کلیلی جۆکەری سەرەکی (Master Joker Key):** تەنها یەک کلیلی یەکگرتوو بۆ بەستنەوەی **OpenCode** و **Cline / Roo Code** و **Open WebUI** و **n8n** و هەموو بەرنامەکانی تری گونجاو لەگەڵ OpenAI API.
- **🌍 ڕووکاری فرەزمان (EN / KU / AR):** گۆڕینی خێرای زمان بەبێ دووبارەبوونەوە لەگەڵ گۆڕینی ئاڕاستەی پەڕە (`RTL / LTR`) بە فۆنتی جوانی **Vazirmatn**.
- **⚡ پێوانەکردنی خێرایی و هەڵبژاردنی خۆکار:** پێوانەکردنی خێرایی (`ms`) و توانای کۆدنووسینی مۆدێلە خۆڕاییەکان و جێبەجێکردنی خێراترین و بەهێزترین مۆدێل بە شێوەی خۆکار.
- **🛡️ تێپەڕاندنی خۆکاری کێشەکان (Auto-Cooldown):** لە کاتی پڕبوونی سنووری هەر کلیلێک (`429`) یان بوونی هەڵە، ڕاستەوخۆ دەگوازرێتەوە بۆ کلیلی دواتر بەبێ پچڕانی کارەکەت.
- **⚙️ کارکردنی خۆکار لە پاشبنەمادا (`systemd`):** لەگەڵ داگیرساندنی کۆمپیوتەر بە شێوەی خۆکار کار دەکات.

### 🛠️ دامەزراندنی خێرا
```bash
git clone https://github.com
cd Smart-AI-Key-Rotator-with-Pro-Web-Dashboard
chmod +x install.sh && ./install.sh
```

1. پانێڵی کۆنترۆڵ بکەرەوە لە وێبگەڕەکەت: **`http://localhost:4000/ui`**
2. **کلیلی جۆکەر (`sk-joker-...`)** کۆپی بکە لە شریتی سەرەوە.
3. ئەم زانیارییانە بەکاربهێنە بۆ بەستنەوەی هەر بەرنامەیەک:
   - **Base URL:** `http://localhost:4000/v1`
   - **API Key:** `sk-joker-xxxxxxxxxxxxxxxx`
   - **Model:** `auto-free`
