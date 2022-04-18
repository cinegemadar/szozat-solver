from fastapi import FastAPI

from solver import GuessState, join_by_coma
from solver_cli import nextGuess, start

# HOW TO
# see: https://fastapi.tiangolo.com/tutorial/first-steps/
# uvicorn solver_server:app --reload

app = FastAPI()


@app.post("/guess")
async def get_guess(words: list[list]):  # TODO move to solver_server
    """This function show how to parse words data from JSON payload and get the next guess."""
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
                gs.add_grey_letter(letter)
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
        ["a", 1, "b", 2, "c", 3, "d", 3, "e", 1],
        ["a", 1, "b", 2, "c", 3, "d", 3, "e", 1],
        ["a", 1, "b", 2, "c", 3, "d", 3, "e", 1],
        ["a", 1, "b", 2, "c", 3, "d", 3, "e", 1],
        ["a", 1, "b", 2, "c", 3, "d", 3, "e", 1],
        ["a", 1, "b", 2, "c", 3, "d", 3, "e", 1],
    ]
    res = asyncio.run(get_guess(payload))
    print(res)
