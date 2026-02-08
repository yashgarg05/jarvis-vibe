# Jarvis — A Local AI Voice Assistant (Vibecoded)

Jarvis is a **local, voice-controlled AI assistant** built from scratch using Python and a locally running LLM via **Ollama**.
It listens, thinks, speaks, and executes system commands — all **offline**, all on your machine.

This project is **vibecoded**: built iteratively, experimentally, and with curiosity-first engineering.
Not over-engineered. Not tutorial-copied. Just shipped.

---

## Features

* Voice input using microphone
* Local LLM reasoning via Ollama (no cloud APIs)
* Text-to-speech responses
* System commands (open apps, browser, etc.)
* Continuous agent loop (listen → think → act)
* Clean voice-based exit command
* Fully local & private

---

## How Jarvis Works (High Level)

```
Voice Input
   ↓
Speech → Text
   ↓
Command Router
   ├── System Command
   └── LLM Reasoning (Ollama)
   ↓
Text → Speech
```

This is the same core loop used in real AI agents and assistants.

---

## Tech Stack

* **Python 3.10+**
* **Ollama** (local LLM runtime)
* **llama3.x** (or any Ollama-supported model)
*  **google-generativeai**
* `speech_recognition`
* `pyttsx3` / macOS `say`
* `pyaudio`

No OpenAI keys. No Gemini quotas. No internet dependency for thinking.

---

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/jarvis.git
cd jarvis
```

### 2. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install & start Ollama

```bash
brew install ollama
ollama run llama3.1
```

(You can replace `llama3.1` with any supported model.)

---

## Run Jarvis

```bash
python main.py
```

Speak naturally:

* “What is artificial intelligence”
* “Open Chrome”
* “Exit”

Jarvis will respond **by voice**.

---

## Voice Notes

* Jarvis waits while speaking (no overlapping audio)
* On macOS, native system voice is recommended for stability
* Voice behavior is intentionally simple and reliable

---

## Known Limitations

* No wake word (by design, for now)
* No long-term memory yet
* Voice quality depends on OS TTS engine
* This is an evolving agent, not a polished product

---

## Roadmap (Maybe)

* Intent classifier (commands vs conversation)
* Persistent memory
* Better voice models
* Interruptible speech
* Background desktop mode

Or maybe something completely different. That’s the vibe.

---

## License

MIT — do whatever you want. Break it. Improve it. Fork it.
