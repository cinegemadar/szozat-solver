import requests
import json

if __name__ == "__main__":
    with open('./test_payload.json','r') as fp:
        data=json.load(fp)
        result = requests.post('https://polar-fortress-90021.herokuapp.com/guess', json=data)
        print(f"==[ result: {result.json()}")
