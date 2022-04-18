from random import sample
from collections import defaultdict

def join_by_coma(container):
    return ",".join(container)

def string_param_to_dict(param: str):
    resultDict = defaultdict(lambda: [])
    if param:
        tmpList = param.split(",")
        for i in range(0, len(tmpList), 2):
            resultDict[tmpList[i]].append(tmpList[i + 1])
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

    def add_grey_letter(self, letter):
        if not letter in self.include:
            self.exclude.add(letter)

    def add_green_letter(self, letter, index):
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
    """ Indicates that list of letters must be in the solution."""
    if not letters:
        return True
    for l in letters.split(","):
        if l not in word:
            return False
    return True


def excludes(letters, word):
    """ Indicates that list of letters must not be in the solution."""
    if not letters:
        return True
    for l in letters.split(","):
        if l in word:
            return False
    return True


def not_at(pos_dicts, word):
    """ Indicates that list of letters must not be at given index in the solution."""
    for k, v in pos_dicts.items():
        for i in v:
            if word[int(i) - 1] == k:
                return False
    return True


def startword(words):
    """ Returns random start word. """
    return sample(words, 1)[0]
