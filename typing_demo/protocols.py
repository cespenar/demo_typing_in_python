from typing import Protocol, Any


class Multiplicable(Protocol):
    def __mul__(self, other: Any) -> Any: ...


def double_multiplicable(x: Multiplicable) -> Any:
    return x * 2


if __name__ == '__main__':
    print(double_multiplicable(2))
    print(double_multiplicable('meow '))
    print(double_multiplicable([1, 2, 3]))
    print(double_multiplicable(3 + 2j))
