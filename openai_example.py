# openai_example.py
# Queries OpenAI GPT models using the OpenAI Python SDK

import os
from openai import OpenAI

# Configure API - reads key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def query_openai(prompt):
    """Query OpenAI GPT model with a user prompt."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",   # change to "gpt-4o" if your plan supports it
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("\nQuerying OpenAI...")
    result = query_openai(user_prompt)
    print("\nResponse:")
    print(result)
