# cohere_example.py
# Queries Cohere models using the Cohere Python SDK

import os
import cohere

# Configure API - reads key from environment variable
api_key = os.getenv("COHERE_API_KEY")
client = cohere.Client(api_key=api_key)


def query_cohere(prompt):
    """Query Cohere model with a user prompt."""
    try:
        response = client.chat(
            model="command-r",   # reliable model available on free tier
            message=prompt,
            temperature=0.7,
            max_tokens=500
        )
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Cohere...")
    result = query_cohere(user_prompt)
    print("\nResponse:")
    print(result)
