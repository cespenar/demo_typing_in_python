from collections.abc import Sequence
from random import shuffle
from typing import TypeVar

T = TypeVar('T')


def sample(population: Sequence[T], size: int) -> list[T]:
    if size < 1:
        raise ValueError('size must be >= 1')
    result = list(population)
    shuffle(result)
    return result[:size]


if __name__ == '__main__':
    numbers_int = [1, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 7, 8]
    colors = ['red', 'blue', 'blue', 'red', 'green', 'red', 'red']

    print(sample(numbers_int, 5))
    print(sample(colors, 3))
