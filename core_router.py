import secrets
import yaml, httpx, base64, time, asyncio

CONFIG_PATH = "/home/kozer/litellm_config.yaml"
ENDPOINTS = {
    "gemini": base64.b64decode("aHR0cHM6Ly9nZW5lcmF0aXZlbGFuZ3VhZ2UuZ29vZ2xlYXBpcy5jb20vdjFiZXRhL29wZW5haS9jaGF0L2NvbXBsZXRpb25z").decode(),
    "groq": base64.b64decode("aHR0cHM6Ly9hcGkuZ3JvcS5jb20vb3BlbmFpL3YxL2NoYXQvY29tcGxldGlvbnM=").decode(),
    "openrouter": base64.b64decode("aHR0cHM6Ly9vcGVucm91dGVyLmFpL2FwaS92MS9jaGF0L2NvbXBsZXRpb25z").decode(),
    "cerebras": base64.b64decode("aHR0cHM6Ly9hcGkuY2VyZWJyYXMuYWkvdjEvY2hhdC9jb21wbGV0aW9ucw==").decode(),
    "mistral": base64.b64decode("aHR0cHM6Ly9hcGkubWlzdHJhbC5haS92MS9jaGF0L2NvbXBsZXRpb25z").decode(),
}
MODELS_URLS = {
    "gemini": base64.b64decode("aHR0cHM6Ly9nZW5lcmF0aXZlbGFuZ3VhZ2UuZ29vZ2xlYXBpcy5jb20vdjFiZXRhL29wZW5haS9tb2RlbHM=").decode(),
    "groq": base64.b64decode("aHR0cHM6Ly9hcGkuZ3JvcS5jb20vb3BlbmFpL3YxL21vZGVscw==").decode(),
    "openrouter": base64.b64decode("aHR0cHM6Ly9vcGVucm91dGVyLmFpL2FwaS92MS9tb2RlbHM=").decode(),
    "cerebras": base64.b64decode("aHR0cHM6Ly9hcGkuY2VyZWJyYXMuYWkvdjEvbW9kZWxz").decode(),
    "mistral": base64.b64decode("aHR0cHM6Ly9hcGkubWlzdHJhbC5haS92MS9tb2RlbHM=").decode(),
}
FONT_URL = "https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600&display=swap"

def cap_score(mod: str) -> int:
    m = mod.lower()
    if any(x in m for x in ["pro", "coder", "120b", "70b", "r1", "v3", "v4", "3.8"]): return 95
    if any(x in m for x in ["flash", "32b", "27b", "latest", "mistral", "8b"]): return 84
    return 72

ALL_KEYS, STATS, ROUTING_MODE = [], {}, "smart"

def reload_pool():
    global ALL_KEYS
    with open(CONFIG_PATH) as f: cfg = yaml.safe_load(f) or {"model_list": []}
    ALL_KEYS = []
    for m in cfg.get("model_list", []):
        p = m["litellm_params"]; k = p["api_key"]
        mod = p.get("model", "gemini-flash-lite-latest")
        ALL_KEYS.append({"provider": p.get("provider", "gemini"), "model": mod, "api_key": k, "enabled": p.get("enabled", True), "cap": cap_score(mod)})
        STATS.setdefault(k, {"ms": 500, "ok": 0, "fail": 0, "cooldown": 0, "err": "جاهز", "last": "-"})

def pick_candidates():
    now = time.time()
    active = [x for x in ALL_KEYS if x["enabled"] and STATS.get(x["api_key"], {}).get("cooldown", 0) <= now]
    if not active: active = [x for x in ALL_KEYS if x["enabled"]]
    if ROUTING_MODE == "power": active.sort(key=lambda x: (-x["cap"], STATS[x["api_key"]]["ms"]))
    else: active.sort(key=lambda x: (STATS[x["api_key"]]["ms"] / (x["cap"] / 80.0)))
    return active

reload_pool()

JOKER_KEY = ""

def get_joker_key():
    global JOKER_KEY
    with open(CONFIG_PATH) as f:
        cfg = yaml.safe_load(f) or {}
    jk = cfg.get("joker_key", "")
    if not jk:
        jk = "sk-joker-" + secrets.token_hex(16)
        cfg["joker_key"] = jk
        with open(CONFIG_PATH, "w") as f:
            yaml.safe_dump(cfg, f, allow_unicode=True)
    JOKER_KEY = jk
    return jk

def regen_joker_key():
    global JOKER_KEY
    with open(CONFIG_PATH) as f:
        cfg = yaml.safe_load(f) or {}
    JOKER_KEY = "sk-joker-" + secrets.token_hex(16)
    cfg["joker_key"] = JOKER_KEY
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(cfg, f, allow_unicode=True)
    return JOKER_KEY

get_joker_key()
import secrets
JOKER_KEY = ""
def get_joker_key():
    global JOKER_KEY
    with open(CONFIG_PATH) as f: cfg = yaml.safe_load(f) or {}
    jk = cfg.get("joker_key", "")
    if not jk:
        jk = "sk-joker-" + secrets.token_hex(16)
        cfg["joker_key"] = jk
        with open(CONFIG_PATH, "w") as f: yaml.safe_dump(cfg, f, allow_unicode=True)
    JOKER_KEY = jk
    return jk

def regen_joker_key():
    global JOKER_KEY
    with open(CONFIG_PATH) as f: cfg = yaml.safe_load(f) or {}
    JOKER_KEY = "sk-joker-" + secrets.token_hex(16)
    cfg["joker_key"] = JOKER_KEY
    with open(CONFIG_PATH, "w") as f: yaml.safe_dump(cfg, f, allow_unicode=True)
    return JOKER_KEY

get_joker_key()
