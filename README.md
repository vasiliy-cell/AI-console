
⚠️ **DEVELOPMENT STATUS:** This project is currently **under active development** and is approximately **70% complete**. The frontend and AI logic are functional, but full backend integration is still in progress.

**AICLI** is a user-friendly desktop terminal emulator designed specifically for beginners. It integrates a powerful AI assistant that allows you to interact with your system using natural language. Instead of memorizing complex flags or digging through endless documentation, you can simply describe what you want to achieve, and the AI handles the syntax.

##  Built for Beginners

- **Natural Language to Commands:** Describe your intent in plain English, and the AI generates the correct command.
- **Real-time Explanations:** The AI explains what commands do so you can learn while you work.
- **Modern Interface:** A clean GUI featuring a dual-panel layout: a professional terminal on one side and an AI chat assistant on the other.
- **Safety First:** Reduces the fear of breaking things by helping you understand exactly what will happen before you hit enter.

--------------------------------------------------------------------------------

##  System Architecture

The project follows a **Clean Architecture** to ensure speed, safety, and intelligence:

1. **Frontend :** Built with **HTML, CSS, and TypeScript**, using **xterm.js** to render a high-performance terminal in a dedicated panel.
2. **Rust Backend / Tauri :** Acts as the bridge between the UI and the system. It manages the **PTY (Pseudo-Terminal)** for running shells like Bash or Zsh and handles window events.
3. **Python AI Service :** A separate process that manages AI logic, prompt engineering, and context. It communicates with the Rust backend via **stdin/stdout** for fast, sandboxed streaming of AI responses.

<img width="2752" height="1536" alt="image" src="https://github.com/user-attachments/assets/66cf7bdd-2023-42c4-bdbb-e39dd73d96c4" />


--------------------------------------------------------------------------------

## 📦 Installation Guide
**Note:** Because the project is still in its early stages, the manual installation process is currently **complex**. We are working on making it much **simpler and more automated** in future releases.

To run AICLI, you will need **Python 3.11+**, **Node.js**, and **Rust (Cargo)** installed on your system.

### 1. Clone the Repository

```
git clone https://github.com/vasiliy-cell/AI-console.git
cd AICLI
```

### 2. Setup Python AI Service

Navigate to the python directory and create a virtual environment:

```
cd python
python -m venv venv
# Activation (macOS/Linux):
source venv/bin/activate
# Install requirements:
pip install -r requirements.txt
```

### 3. Add Your API Key

1. Go to: [https://platform.deepseek.com/api_keys](https://www.google.com/url?sa=E&q=https%3A%2F%2Fplatform.deepseek.com%2Fapi_keys)
2. Create an API Key (paid service, but affordable).
3. Place your key inside the file: `python/api_key.txt`.
    - _Note: The file should contain only the API key, without quotes or extra spaces._

Create a file named `python/api_key.txt` and paste your AI provider's API key inside (plain text, no quotes).

### 4. Install Frontend & Launch

Return to the root directory, install the dependencies, and start the app in development mode:

```
cd ..
npm install
npm run tauri dev
```

--------------------------------------------------------------------------------

## 🛠 Core Dependencies

AICLI is powered by several industry-standard technologies:

- **Tauri:** Lightweight framework for native desktop GUIs.
- **xterm.js:** The gold standard for terminal rendering in the browser.
- **portable-pty:** A Rust library for low-level terminal process management.
- **Tokio:** Asynchronous runtime for the Rust backend.
- **Serde:** High-performance data serialization.
