import requests
import time

def main() -> None:
    respuesta = requests.get('https://jsonplaceholder.typicode.com/posts/1')

    print(respuesta.json())
