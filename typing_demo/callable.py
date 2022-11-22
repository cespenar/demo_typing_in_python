from collections.abc import Callable


def twice(i: int, next_value: Callable[[int], int]) -> int:
    return next_value(next_value(i))


def increment(i: int) -> int:
    return i + 1


if __name__ == '__main__':
    print(twice(1, increment))
