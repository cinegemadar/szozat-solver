import requests
import json

if __name__ == "__main__":
    with open('./test_payload.json','r') as fp:
        data=json.load(fp)
        result = requests.post('http://127.0.0.1:8000/guess', json=data)
        print(f"==[ result: {result.json()}")
