import requests
import json

# from test_payload import payload
payload=[
    ["a", 1, "b", 2, "c", 3, "d", 3, "e", 1],
    ["a", 1, "b", 2, "c", 3, "d", 3, "e", 1],
    ["a", 1, "b", 2, "c", 3, "d", 3, "e", 1],
    ["a", 1, "b", 2, "c", 3, "d", 3, "e", 1],
    ["a", 1, "b", 2, "c", 3, "d", 3, "e", 1],
    ["a", 1, "b", 2, "c", 3, "d", 3, "e", 1],
]
if __name__ == "__main__":
    with open('./test_payload.json','r') as fp:
        data=json.load(fp)
        # print(data)
        result = requests.post('http://127.0.0.1:8000/guess', json=data)
        # print(result)
        print(f"==[ result: {result.json()}")
