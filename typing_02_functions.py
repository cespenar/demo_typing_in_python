# double without type hints
def double_simple(x):
    return x * 2


# double with a very simple type hint. This isn't really correct.
def double_simple_typed(x: int) -> int:
    return x * 2


if __name__ == '__main__':
    print(double_simple(2))
    print(double_simple_typed(2))
