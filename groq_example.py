# groq_example.py
# Queries Groq-hosted Llama models using the Groq Python SDK

import os
from groq import Groq

# Configure API - reads key from environment variable
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)


def query_groq(prompt):
    """Query Groq Llama model with a user prompt."""
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # fast and free on Groq's free tier
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
    print("\nQuerying Groq...")
    result = query_groq(user_prompt)
    print("\nResponse:")
    print(result)
