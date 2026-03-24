# ollama_example.py
# Queries a locally running Ollama model via its REST API
# Ollama must be installed and running: https://ollama.ai/
# Pull a model first with: ollama pull llama3

import requests
import json

# Ollama runs locally — no API key needed
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"   # change to any model you have pulled locally


def query_ollama(prompt):
    """Query a local Ollama model with a user prompt."""
    try:
        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False   # get a single complete response
        }

        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()
        return data.get("response", "No response received.")

    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Make sure Ollama is running (run 'ollama serve')."
    except Exception as e:
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print(f"\nQuerying Ollama ({MODEL_NAME})...")
    result = query_ollama(user_prompt)
    print("\nResponse:")
    print(result)
