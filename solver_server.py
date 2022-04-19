from fastapi import FastAPI

from solver import GuessState, join_by_coma
from solver_cli import nextGuess, start

# HOW TO
# see: https://fastapi.tiangolo.com/tutorial/first-steps/
# uvicorn solver_server:app --reload

app = FastAPI()


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
    import asyncio

    payload = [
        ["gy", 3, "ö", 3, "ny", 3, "ö", 3, "r", 1],
        ["z", 3, "o", 3, "b", 3, "o", 1, "r", 1],
        ["k", 3, "ő", 1, "p", 1, "o", 1, "r", 1],
    ]
    res = asyncio.run(post_table_state(payload))
    print(res)
