import requests
from ._config import api_server

def activate_livelink():
    data = {"node_path": "/World/audio2face/StreamLivelink", "value": True}
    response = requests.post(api_server + "/A2F/Exporter/ActivateStreamLivelink", json=data).json()
    print(response)

if __name__ == "__main__":
    activate_livelink()