# 🔍 Telegram Chat Monitor Bot

A smart bot for monitoring Telegram chats with keyword filtering.
It automatically finds and forwards messages containing specified keywords directly to your **Saved Messages**.

[![aiogram](https://img.shields.io/badge/aiogram-3.x-blue?logo=python)](https://github.com/aiogram/aiogram)
[![Telegram](https://img.shields.io/badge/Telegram-join%20chat-blue?logo=telegram)](https://t.me/credexus)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

# ✨ Features

* **📊 Chat Monitoring** – Automatically search for messages containing keywords
* **⚡ Dual Filtering System** – Keywords + banned words for precise filtering
* **🔔 Instant Notifications** – Forward detected messages to Saved Messages
* **🎯 Flexible Configuration** – Dynamically change filters via bot commands
* **🚫 Spam Protection** – Ignore messages containing banned words
* **👥 Whitelist** – Restrict bot control access
* **🌐 Group & Channel Support** – Works in all types of Telegram chats

---

# 📸 Screenshots

*(Screenshots section remains unchanged in the original README)*

---

# 🏗 Architecture

```
telegram-chat-monitor/
├── config/                # Configuration files
│ ├── bot_config.py        # Main bot configuration
│ ├── keywords.json        # File containing keywords and banned words
│ └── logger_config.py     # Logging settings
│
├── handlers/              # Message and command handlers
│ ├── commands/            # Bot command handlers
│ │ └── base_handlers.py
│ └── custom_handlers/     # Custom handlers
│ ├── custom_commands.py
│ └── join_handlers.py
│
├── states/                # Finite State Machine states
│ └── all_states.py
│
├── utils/                 # Helper utilities
│ ├── generate_session.py  # Telethon session generator
│ ├── join_groups.py       # Auto join groups
│ ├── json_keywords_manager.py # Keywords manager
│ ├── llogin.py            # Alternative Telethon session generator
│ ├── logger.py            # Logging
│ └── special_func.py      # Special functions
│
├── Dockerfile             # Docker configuration
├── main.py                # Main executable file
└── requirements.txt       # Python dependencies
```

---

# 📦 Installation & Run

## 1. Clone the repository

```bash
git clone https://github.com/ZheglY/multi-chat-keyword-forwarder-.git
cd multi-chat-keyword-forwarder-
```

---

## 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file or set environment variables:

```bash
# Bot
BOT_TOKEN=your_bot_token_here

# User account (for monitoring chats)
API_ID=your_api_id
API_HASH=your_api_hash
SESSION_STRING=your_session_string

# Access settings
ADMIN_CHAT_ID=your_chat_id
ALLOWED_USERS=user_id1,user_id2,user_id3
```

---

## 5. Generate Telethon session

```bash
python utils/generate_session.py
```

If `generate_session.py` fails, run:

```bash
python utils/llogin.py
```

---

## 6. Run the bot

```bash
python main.py
```

---

# 🚀 Deploy on Fly.io

## 1. Install flyctl

```bash
# Linux/Mac
curl -L https://fly.io/install.sh | sh

# Windows
iwr https://fly.io/install.ps1 -useb | iex
```

---

## 2. Initialize the application

```bash
flyctl auth login
flyctl launch --name your-app-name --region fra --no-deploy
```

---

## 3. Configure secrets

```bash
flyctl secrets set \
  BOT_TOKEN="your_bot_token" \
  API_ID="your_api_id" \
  API_HASH="your_api_hash" \
  SESSION_STRING="your_session_string" \
  ADMIN_CHAT_ID="your_chat_id" \
  ALLOWED_USERS="user_id1,user_id2,user_id3"
```

---

## 4. Deploy

```bash
flyctl deploy
```

---

# 📋 Bot Commands

### Main Commands

```
/start
```

Shows bot information and available commands.

```
/filters
```

View and modify keywords used for filtering messages in chats.

```
/ban
```

View and modify banned words that will cause messages to be skipped.

---

### Filter Management

Add keywords:

```
/filters word1 word2 word3
```

Add banned words:

```
/ban banned_word1 banned_word2
```

---

# ⚙️ Configuration

### `keywords.json` format

```json
{
  "keywords": ["usdt", "crypto", "exchange", "buy", "sell"],
  "ban_words": ["scam", "fraud", "drug", "weapon"]
}
```

Example commands:

```bash
# Add keywords
/filters photo video reels editing youtube

# Add banned words
/ban spam scam fraud
```

---

# 🔧 For Developers

Project structure includes:

* **Telethon Client** – For monitoring chats using a user account
* **Aiogram Bot** – For handling commands and interacting with users
* **JSON Keywords Manager** – Manage filters using a JSON file
* **FSM State Management** – Manage bot states

### Adding new functionality

1. Create a handler inside `handlers/`
2. Register it in `main.py`
3. Add a command in `base_handlers.py`

---

# ⚠️ Possible Errors

**Authorization error**

Check that `API_ID` and `API_HASH` are correct.

**Session conflict**

Ensure only **one instance of the bot** is running. Only one session can run at a time.

**Messages are not forwarded**

* The user account must be a member of the monitored chats.
* Make sure keywords exist.
* Add keywords with `/filters`.

⚠️ After restarting the bot, **keywords and banned words will be reset**.

---

# 📄 License

This project is licensed under the **MIT License**.
See the `LICENSE` file for details.

---

# ⚠️ Important

* Use this project **only for legal purposes**
* Follow **Telegram Terms of Service**
* Respect the **privacy of other users**
* Store secret data in **environment variables**

---

⭐ **If this project is useful, please give it a star on GitHub!**