import os
import json

import requests

xi_api_key = os.environ.get("xi_api_key")
elevenlabs_url = os.environ.get("elevenlabs_url")

def fetch_tts(text):
    url = elevenlabs_url
    headers = {
        'xi-api-key': xi_api_key,
        'Content-Type': 'application/json'
    }
    payload = {
        'model_id': "eleven_multilingual_v2",
        'text': text,
        'voice_settings': {
            'similarity_boost': 0.75,
            'stability': 0.5
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code != 200:
        raise Exception(f"HTTP error! status: {response.status_code}")

    return response.content

if __name__ == "__main__":
    response_data = fetch_tts("Your text here")
    with open("output.mp3", "wb") as file:
        file.write(response_data)
