# https://peps.python.org/pep-0544/ <- very difficult to read
# https://mypy.readthedocs.io/en/stable/protocols.html

from typing import Any, Protocol, TypeVar


class Multiplicable(Protocol):
    def __mul__(self, other: Any) -> Any: ...


T = TypeVar('T', bound=Multiplicable)


def double_multiplicable(x: T) -> T:
    return x * 2


if __name__ == '__main__':
    print(double_multiplicable(2))
    print(double_multiplicable('meow '))
    print(double_multiplicable([1, 2, 3]))
    print(double_multiplicable(3 + 2j))
