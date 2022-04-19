import requests
import json

if __name__ == "__main__":
    with open("./test_payload.json", "r") as fp:
        data = json.load(fp)
        result = requests.post(
            "https://szozat-wordle-solver.herokuapp.com/guess", json=data
        )
        print(f"==[ result: {result.json()}")
