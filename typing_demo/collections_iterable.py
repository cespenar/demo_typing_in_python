from collections.abc import Iterable
from typing import TypeAlias

FromTo: TypeAlias = tuple[str, str]  # Python 3.10


def text_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text = text.replace(from_, to)
    return text


if __name__ == '__main__':
    original_text = 'the quick brown fox jumps over the lazy dog'
    l33t = [('a', '4'), ('e', '3'), ('i', '1'), ('o', '0')]
    print(text_replace(original_text, l33t))
