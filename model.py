import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def custom_request(text,key):
    return requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",

        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },

        data=json.dumps({
            "model": "google/gemini-2.0-flash-exp:free",
            "messages": [
            {
                "role": "user",
                "content": [
                {
                    "type": "text",
                    "text": f"{text}"
                },
                ]
            }
            ],
        })
    )

response = custom_request("hi")