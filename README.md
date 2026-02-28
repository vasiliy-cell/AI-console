I've decided to make the CLI much more user-friendly by integrating AI.
From now on, you can simply describe what you want in plain English (or any natural language), and the AI-powered API will automatically convert it into the correct command.

✨ What Is This

AICLI is a desktop terminal with a built-in AI chat.

It combines:

A full-featured shell via PTY

AI token streaming

Command explain / suggest

The ability to abort generation

A modern UI

Architecturally, it is closer to Warp, but built with a Python-first AI logic and minimal Rust.

🚀 What Happens When You Launch It
$ aicli

→ A new window opens
→ On the left — a real bash or zsh
→ On the right — an AI panel
→ Responses stream token by token
→ You can interrupt generation

🏗 Architecture

🧠 Responsibility Distribution
🐍 Python — The Brain

Token streaming

Abort / cancel

Context and history

Prompt logic

Files:

python/
├── ai_service.py
├── api.py
├── errors.py
├── lib.py
└── api_key.txt
🦀 Rust — The Infrastructure

PTY (bash/zsh)

Resize

Events

Launching Python

Bridge between UI and AI

Files:

rust_logic/
├── ai_bridge.rs
└── pty.rs

Integrated via:

src/tauri/
🌐 Frontend — The Interface

xterm.js — terminal rendering

AI panel

Splitter

Resize

Keyboard shortcuts

src/frontend/
├── terminal/
├── ai-panel/
├── app.ts
├── splitter.js
└── resize.ts
🔌 Rust ↔ Python Communication

Uses a simple and reliable stdin/stdout protocol.

Rust → Python
{"type":"prompt","id":"42","text":"explain ls -la"}
Python → Rust (stream)
{"type":"token","id":"42","text":"The "}
{"type":"token","id":"42","text":"command "}
{"type":"done","id":"42"}
Abort
{"type":"abort","id":"42"}
📂 Real Project Structure
AICLI/
├── python/
├── rust_logic/
├── src/
│   ├── frontend/
│   └── tauri/
├── index.html
├── package.json
├── vite.config.js
└── README.md
🛠 Technologies
Backend

🦀 Rust

🧵 tokio

🖥 PTY

⚙ Tauri

Frontend

HTML / CSS

TypeScript

xterm.js

Vite

AI

Python 3.11+

asyncio

aiohttp

Streaming API

🧩 Key Features

✔ Full shell (not emulated)
✔ Real-time streaming
✔ Abort generation
✔ Explain last command
✔ Suggest improvements
✔ Terminal resize support
✔ Isolated AI logic

📦 Installation
1️⃣ Environment Setup

Python 3.11+

Node.js 18+

Rust + Cargo

Git

2️⃣ Python
cd python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Add your API key to:

python/api_key.txt
3️⃣ Frontend
npm install
npm run dev
4️⃣ Run Tauri
npm run tauri dev