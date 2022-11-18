from typing import Optional


def foo(arg: int = 0) -> None:
    print(arg)


def bar(arg: Optional[int]) -> None:
    print(arg)


def baz(arg: int | None) -> None:
    print(arg)
