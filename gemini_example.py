# gemini_example.py
# Queries Google Gemini using the google-generativeai SDK

import os
import google.generativeai as genai

# Configure API - reads key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")   # free tier friendly model


def query_gemini(prompt):
    """Query Google Gemini with a user prompt."""
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=500,
                temperature=0.7
            )
        )
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Google Gemini...")
    result = query_gemini(user_prompt)
    print("\nResponse:")
    print(result)
