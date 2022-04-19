from fastapi import FastAPI
import asyncio

from solver import GuessState, join_by_coma
from solver_cli import nextGuess, start

# HOW TO
# see: https://fastapi.tiangolo.com/tutorial/first-steps/
# uvicorn solver_server:app --reload

app = FastAPI()


@app.post("/test")
async def post_test():
    """Post test endpoint."""
    import json

    with open("./test_payload.json", "r") as fp:
        return await post_table_state(json.load(fp))


@app.post("/guess")
async def post_table_state(words: list[list]):
    """Send the current state of the board to the server and recieve the next guess."""
    if not len(words):
        return start()
    gs = GuessState()
    for word in words:
        for i in range(0, len(word), 2):
            letter = word[i]
            color = word[i + 1]
            if color == 1:  # GREEN
                gs.add_green_letter(letter, int(i / 2))
                continue
            if color == 2:  # YELLOW
                gs.add_yellow_letter(letter, int(i / 2) + 1)
                continue
            if color == 3:  # GREY
                gs.add_grey_letter(letter, int(i / 2) + 1)
    return nextGuess(
        pattern=join_by_coma(gs.pattern),
        exclude=join_by_coma(gs.exclude),
        include=join_by_coma(gs.include),
        posExclude=join_by_coma(gs.wrongplace),
        single=True,
    )


if __name__ == "__main__":  # Test
    print(asyncio.run(post_test()))
