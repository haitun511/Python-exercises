import re


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    result = 0

    for letter in set(line):
        for match in re.findall(letter + "+", line):
            if len(match) > result:
                result = len(match)

    return result