# huggingface_example.py
# Queries Hugging Face Inference API using the requests library

import os
import requests

# Configure API - reads key from environment variable
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Using a reliable, free text-generation model
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.1"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

HEADERS = {"Authorization": f"Bearer {API_KEY}"}


def query_huggingface(prompt):
    """Query Hugging Face Inference API with a user prompt."""
    try:
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 500,
                "temperature": 0.7,
                "return_full_text": False   # return only the generated part
            }
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
        response.raise_for_status()

        data = response.json()

        # The response is a list of generated text objects
        if isinstance(data, list) and len(data) > 0:
            return data[0].get("generated_text", "No text generated.")
        else:
            return str(data)

    except Exception as e:
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Hugging Face...")
    result = query_huggingface(user_prompt)
    print("\nResponse:")
    print(result)
