import random
from typing import Sequence, Any, List
from string import ascii_lowercase


def weighted_choice(options: Sequence[Any], weights: Sequence[float]) -> Any:
    assert len(options) == len(weights)
    sw = sum(weights)
    s = 0.0
    normalized_limits = []
    for x in weights:
        s += x / sw
        normalized_limits.append(s)

    r = random.uniform(0.0, 1.0)

    for option, limit in zip(options, normalized_limits):
        if r <= limit:
            return option


def generate_word(w: int = None, p: Sequence[float] = None, characters: Sequence[str] = ascii_lowercase) -> str:
    """
    :param p:
    :param characters:
    :param w: number of letters - random by default
    :return:
    """
    if w is None:
        if p is None:
            p = [0, 2, 5, 6, 8, 7, 6, 4, 3, 2, 1, 0.5, 0.5, 0.5, 0.5, 0.5]
        w = weighted_choice(range(len(p)), p)

    _word = "".join(random.choice(characters) for _ in range(w))
    return _word


def generate_text(n: int, **kwargs) -> List[str]:
    """

    :param n: number of words
    :return:
    """

    words = [generate_word(**kwargs) for _ in range(n)]
    return words


def make_spaces(words: Sequence[str], desired_line_length: int, extra_space_char: str = "_") -> Sequence[str]:
    no_of_spaces_between_words = len(words) - 1
    # sum of chars in words plus number of spaces between words
    used_chars = sum(len(word) for word in words) + no_of_spaces_between_words
    # remaining chars to fill
    chars_to_fill = desired_line_length - used_chars + 1
    # additional number of spaces to be added after each word
    extra_space_ratio = chars_to_fill/no_of_spaces_between_words
    s = [int((i + 1) * extra_space_ratio) for i in range(no_of_spaces_between_words + 1)]
    list_of_extra_spaces = [(x1 - x0) for x0, x1 in zip(s, s[1:])]
    # after each word there is one mandatory space plus 'd' of extra spaces
    # last word has no following space, but empty character has to be added
    # so the length of spaces matches the length of words
    spaces = [(" " + extra_space_char * d) for d in list_of_extra_spaces] + [""]
    return spaces


def print_lines(lines: Sequence[Sequence[str]], line_limit: int = 80) -> None:
    print("   ", "".join(f"{d // 10:<10d}" for d in range(0, line_limit + 1, 10)))
    print("   ", "".join(f"{d % 10}" for d in range(0, line_limit + 1, 1)))
    # print("_" * (line_limit + 8))

    no_of_chars_in_lines = []
    for i, line in enumerate(lines):
        no_of_chars_in_lines.append(sum(len(x) + 1 for x in line) - 1)

        print(f"{i:02d} |", end="")
        for word, space in zip(line, make_spaces(line, line_limit)):
            print(f"{word}{space}", end="")
        print(f"| {no_of_chars_in_lines[-1]:02d}")

    avg_line = sum(no_of_chars_in_lines[:-1]) / (len(lines) - 1) if len(lines) > 1 else no_of_chars_in_lines[0]
    avg_per = avg_line / line_limit * 100.0
    print("-" * (line_limit + 8))
    print(f"    Average line length: {avg_line:.1f} ({avg_per:.2f}%) ")


def simple_split(words: Sequence[str], line_limit: int = 80) -> List[List[str]]:
    """
    Simple (greedy) solution.
    While there are words to add.
    1. Create new line.
    1. Add as many words to current line as you can.
    2. If nothing more can be added to current line, go to step 1.

    :param words:
    :param line_limit:
    :return:
    """
    pos = 0
    lines = []
    row = []
    for word in words:
        wl = len(word)
        if pos < (line_limit - wl):
            pos += wl + 1
            row.append(word)
        else:
            pos = 0
            lines.append(row)
            row = []
    # dont forget about last line
    if row:
        lines.append(row)
    return lines


def dp_split(words: Sequence[str], line_limit: int = 80) -> List[List[str]]:
    """
    TODO
    :param words:
    :param line_limit:
    :return:
    """
    pass


if __name__ == '__main__':
    text_lines = simple_split(words=generate_text(1301, characters="X"), line_limit=80)
    print_lines(lines=text_lines)
