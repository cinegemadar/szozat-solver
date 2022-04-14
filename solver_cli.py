import solver
from solver import GuessState, join_by_coma
from words import WORDS

from random import sample
import typer

app = typer.Typer()

@app.command()
def start():
    """Sugguest initial guess."""
    typer.echo("".join(solver.startword(WORDS)))


@app.command()
def nextGuess(
    pattern: str,
    exclude: str = None,
    include: str = None,
    posExclude: str = None,
    single: bool = False,
    print: bool = False
):
    """Suggest next guess based on current state."""
    posExcludeDict = solver.string_param_to_dict(posExclude)
    hints = filter(lambda x: solver.match(pattern, x), WORDS)
    hints = filter(lambda x: solver.excludes(exclude, x), hints)
    hints = filter(lambda x: solver.has(include, x), hints)
    hints = filter(lambda x: solver.not_at(posExcludeDict, x), hints)
    hints = list(sorted(hints))
    result = []
    if single and hints:
        result = ["".join(sample(hints, 1)[0])]
    else:
        result = [ "".join(hint) for hint in hints]
    if print:
        typer.echo("\n".join(result))
    return result

if __name__ == "__main__":
    app()
