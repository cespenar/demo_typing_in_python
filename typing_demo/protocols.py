# https://peps.python.org/pep-0544/ <- very difficult to read
# https://mypy.readthedocs.io/en/stable/protocols.html

from typing import Protocol, TypeVar

T = TypeVar('T')


class Repeatable(Protocol):
    def __mul__(self: T, repeat_count: int) -> T: ...


RT = TypeVar('RT', bound=Repeatable)


def double(x: RT) -> RT:
    return x * 2


if __name__ == '__main__':
    print(double(2))
    print(double('meow '))
    print(double([1, 2, 3]))
    print(double(3 + 2j))
