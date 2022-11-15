def double_simple(x):
    """
    Double without type hints.
    """
    return x * 2


def double_simple_typed(x: int) -> int:
    """
    Double with a very simple type hint. This isn't really correct.
    """
    return x * 2


if __name__ == '__main__':
    print(double_simple(2))
    print(double_simple_typed(2))
