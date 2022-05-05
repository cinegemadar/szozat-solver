from random import sample
from collections import defaultdict


def join_by_coma(container):
    """
    >>> join_by_coma(['1','2','3','4']) == "1,2,3,4"
    True
    """
    return ",".join(container)


def string_param_to_dict(param: str):
    """
    >>> dict(string_param_to_dict("a,1,b,2"))
    {'a': ['1'], 'b': ['2']}
    """
    resultDict = defaultdict(lambda: [])
    if param:
        tmpList = param.split(",")
        for index, element in enumerate(tmpList):
            if (index % 2) == 0:
                resultDict[element].append(tmpList[index + 1])
    return resultDict


class GuessState:
    """Keep track of the state of all the guesses."""

    def __init__(self):
        self.include = set()
        self.exclude = set()
        self.wrongplace = set()
        self.pattern = [".", ".", ".", ".", "."]

    def add_yellow_letter(self, letter, index):
        self.exclude.discard(letter)
        self.include.add(letter)
        self.wrongplace.add(f"{letter},{index}")

    def add_grey_letter(self, letter, index):
        """
        >>> t.add_grey_letter('a',1)
        >>> 'a' in t.exclude
        True
        >>> 'a,1' in t.wrongplace
        True
        """
        if not letter in self.include:
            self.exclude.add(letter)
        self.wrongplace.add(f"{letter},{index}")

    def add_green_letter(self, letter, index):
        self.include.add(letter)
        self.pattern[index] = letter
        self.exclude.discard(letter)


def match(pattern, word, wildcard=".", delimiter=","):
    pattern = pattern.split(delimiter)
    if "".join(pattern) == "".join(len(word) * wildcard):
        return True
    for index, character in enumerate(word):
        if pattern[index] == wildcard:
            continue
        if character != pattern[index]:
            return False
    return True


def has(letters, word):
    """Indicates that list of letters must be in the solution.
    >>> has("","alma")
    True
    >>> has("m","alma")
    True
    >>> has("a","korte")
    False
    """
    if not letters:
        return True
    for l in letters.split(","):
        if l not in word:
            return False
    return True


def excludes(letters, word):
    """Indicates that list of letters must not be in the solution."""
    if not letters:
        return True
    for l in letters.split(","):
        if l in word:
            return False
    return True


def not_at(pos_dicts, word):
    """Indicates that list of letters must not be at given index in the solution."""
    for k, v in pos_dicts.items():
        for i in v:
            if word[int(i) - 1] == k:
                return False
    return True


def startword(words):
    """Returns random start word."""
    return sample(words, 1)[0]

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'t':GuessState()})