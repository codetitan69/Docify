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
            "model": "deepseek/deepseek-r1:free",
            "messages": [
            {
                "role": "user",
                "content": f"{text}"
            }
            ],
        })
    )

def Get_Content(response):
    response_json = json.loads(response.content.decode("utf-8"))
    return response_json["choices"][0]["message"]["content"]