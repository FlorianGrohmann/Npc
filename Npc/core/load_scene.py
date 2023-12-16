import requests
from ._config import usd_scene
from ._config import api_server

def load_scene():
    payload ={
        "file_name": usd_scene
    }
    usd = requests.post(f'{api_server}/A2F/USD/Load', json = payload)

    print( f"USD scene: {usd.json()['message']}")

    a2f_instance = requests.get(f'{api_server}/A2F/GetInstances').json()
    a2f_instance = a2f_instance['result']['fullface_instances'][0]

    print(f'A2F Instance: {a2f_instance}')

if __name__ == "__main__":
    load_scene()