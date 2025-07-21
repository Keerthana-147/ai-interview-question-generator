from openai import OpenAI
import os

# initialize OpenAI client with OpenRouter API
# Ensure you have the OpenAI Python package installed: pip install openai
# Set your OpenRouter API key as an environment variable or directly here

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",  # or your OpenRouter endpoint
    api_key="YOUR_API_KEY", #insert api key
    timeout=60  # timeout in seconds (default is 10s)
)

def generate_questions_with_openrouter(prompt):
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        max_tokens=2500,  # Adjust based on expected response length
        messages=[
            {"role": "user", "content": prompt}
        ],
        extra_headers={
            "HTTP-Referer": "https://yourprojectname.com",
            "X-Title": "AI Interview Question Generator"
        }
    )
    return completion.choices[0].message.content
