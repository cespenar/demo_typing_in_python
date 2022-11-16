from typing import Any


def double(x):
    """
    Double without type hints.
    """
    return x * 2


def double_any(x: Any) -> Any:
    """
    This is what a type checker assumes without any type hints.
    PyCharm is definitely smarter than this.
    """
    return x * 2


def double_object(x: object) -> object:
    """
    This is wrong, but the code works!
    """
    return x * 2


if __name__ == '__main__':
    print(double(2))
    print(double_any(2))
    print(double_object(2))
