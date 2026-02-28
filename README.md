AICLI

A beginner-friendly AI-powered terminal.

✨ Why This Exists

I've decided to make the CLI much more user-friendly by integrating AI.
From now on, you can simply describe what you want in plain English (or any natural language), and the AI-powered API will automatically convert it into the correct command.

No more memorizing flags.
No more digging through documentation.
No more fear of breaking something.

Just describe your intent — the terminal handles the syntax.

👶 Built for Beginners

Traditional terminals can feel intimidating:

Cryptic errors

Complex flags

Unclear documentation

Fear of making mistakes

AICLI changes that.

You can:

Ask what a command does

Generate the correct command from natural language

Get suggestions for safer alternatives

Learn while working

You don’t need to know the exact syntax.
You just need to know what you want to achieve.

🚀 How It Works

When you run:

$ aicli

A new desktop window opens:

Left side → real bash or zsh

Right side → built-in AI assistant

Responses stream in real time

You can interrupt generation anytime

It’s a real shell — not a simulation — enhanced with AI guidance.

🛠 Requirements

Make sure you have the following installed:

Python 3.11+

Node.js 18+

Rust + Cargo

Git

📦 Installation Guide
1️⃣ Clone the repository
git clone <your-repository-url>
cd AICLI
2️⃣ Setup Python (AI Service)

Navigate to the Python directory:

cd python

Create a virtual environment:

python -m venv venv

Activate it:

macOS / Linux

source venv/bin/activate

Windows

venv\Scripts\activate

Install required dependencies:

pip install -r requirements.txt
🔑 Add Your API Key

Go to: https://platform.deepseek.com/api_keys

Create an API Key (paid service, but affordable)

Then place your key inside:

python/api_key.txt

The file should contain only the API key, without quotes or extra spaces.

3️⃣ Install Frontend Dependencies

Go back to the project root:

cd ..

Install Node dependencies:

npm install
4️⃣ Run the Application

Start the desktop app:

npm run tauri dev
🧠 What Happens Internally

Python handles AI streaming and prompt logic

Rust manages the terminal (PTY, resize, system events)

The frontend renders the terminal and AI panel

The AI runs as a separate process and communicates via stdin/stdout.


