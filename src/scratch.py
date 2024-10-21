import openai
from dotenv import load_dotenv
import os
from elasticsearch_connector import connect_to_elasticsearch
from openai import OpenAI
import openai
import requests

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
print(openai_api_key)

if not openai_api_key:
    raise ValueError("OpenAI API key not found in environment variables")

# Set your OpenAI API key
openai.api_key = openai_api_key
client = OpenAI(api_key=openai_api_key)


if __name__ == "__main__":


    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the legal implications of Brown v. Board of Education?"}
        ]
    )

    generated_query = response_text = response.choices[0].message.content
    print(f"Generated Query: {generated_query}")


