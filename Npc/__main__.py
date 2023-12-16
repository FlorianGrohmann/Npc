from dotenv import load_dotenv
success = load_dotenv()
if not success:
    print("Failed to load .env file")

from .core.load_scene import load_scene
from .core.activate_livelink import activate_livelink
from .core.chat import chat
from .core.fetch_tts import fetch_tts
from .core.audio_to_array import audio_to_array
from .core.send_audio import send_audio

load_scene()
activate_livelink()

while(True):
    user = input("Enter text: ")
    assistant = chat(user)
    response_data = fetch_tts(assistant)
    wavarr, sample_rate = audio_to_array(response_data)
    send_audio(wavarr, sample_rate)