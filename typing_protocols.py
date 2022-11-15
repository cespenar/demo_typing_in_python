from typing import Protocol, Any


class SupportsMultiplication(Protocol):
    def __mul__(self, other: Any) -> Any: ...


def double_correct(x: SupportsMultiplication) -> Any:
    return x * 2


if __name__ == '__main__':
    print(double_correct(2))
    print(double_correct('meow '))
    print(double_correct([1, 2, 3]))
    print(double_correct(3 + 2j))
