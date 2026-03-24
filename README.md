# AI API Integration

A collection of Python programs that interact with six different Generative AI providers: OpenAI, Groq, Ollama, Hugging Face, Google Gemini, and Cohere.

---

## Project Structure

```
ai-api-integration/
├── openai_example.py
├── groq_example.py
├── ollama_example.py
├── huggingface_example.py
├── gemini_example.py
├── cohere_example.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── openai_output.png
    ├── groq_output.png
    ├── ollama_output.png
    ├── huggingface_output.png
    ├── gemini_output.png
    └── cohere_output.png
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd ai-api-integration
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Never hardcode your API keys. Export them as environment variables before running any script.

**Linux / Mac** (add to `~/.bashrc` or `~/.zshrc` for persistence):

```bash
export OPENAI_API_KEY="your-openai-key"
export GROQ_API_KEY="your-groq-key"
export HUGGINGFACE_API_KEY="your-huggingface-key"
export GOOGLE_API_KEY="your-google-key"
export COHERE_API_KEY="your-cohere-key"
```

**Windows (PowerShell):**

```powershell
$env:OPENAI_API_KEY="your-openai-key"
$env:GROQ_API_KEY="your-groq-key"
$env:HUGGINGFACE_API_KEY="your-huggingface-key"
$env:GOOGLE_API_KEY="your-google-key"
$env:COHERE_API_KEY="your-cohere-key"
```

---

## How to Obtain Each API Key

| Provider | Steps |
|---|---|
| **OpenAI** | Sign up at https://platform.openai.com/ → go to API Keys → Create new key |
| **Groq** | Sign up at https://console.groq.com/ → API Keys → Create API Key |
| **Ollama** | No API key needed — install locally from https://ollama.ai/ |
| **Hugging Face** | Sign up at https://huggingface.co/ → Settings → Access Tokens → New Token |
| **Google Gemini** | Visit https://makersuite.google.com/app/apikey → Create API Key |
| **Cohere** | Sign up at https://dashboard.cohere.com/ → API Keys → New Trial Key |

---

## How to Run Each Program

Each program accepts a text prompt from the user and prints the AI's response.

```bash
# OpenAI
python openai_example.py

# Groq
python groq_example.py

# Ollama (must have Ollama installed and running locally)
ollama pull llama3        # pull the model once
ollama serve              # start the local server (if not already running)
python ollama_example.py

# Hugging Face
python huggingface_example.py

# Google Gemini
python gemini_example.py

# Cohere
python cohere_example.py
```

---

## Screenshots

See the `screenshots/` folder for sample outputs from each provider.

---

## Notes

- Free tier rate limits apply for all providers — avoid sending too many requests quickly.
- Ollama runs fully offline on your machine; no API key is needed.
- Do **not** commit your `.env` file or paste API keys anywhere in the code.
