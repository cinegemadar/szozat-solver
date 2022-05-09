import urllib.request
import json


success = False

try:
    openUrl = urllib.request.urlopen(
        "https://raw.githubusercontent.com/mdanka/szozat/main/src/constants/hungarian-word-letter-listL.json"
    )
except urllib.error.HTTPError:
    openUrl = None

if openUrl and openUrl.getcode() == 200:
    WORDS = json.loads(openUrl.read())
    with open("./szozat.json", "w") as fp: # Create cache
        json.dump(WORDS, fp)
    success = True
else:
    with open("./szozat.json", "r") as fp: # Read cache
        WORDS = json.load(fp)

if __name__ == "__main__":
    print(WORDS[:10])
    print(f"Connection succeeded: {success}")
