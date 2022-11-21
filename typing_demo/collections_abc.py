from collections.abc import Iterable, Sequence


class C(Sequence):  # Direct inheritance
    def __init__(self): ...  # Extra method not required by the ABC

    def __getitem__(self, index):  ...  # Required abstract method

    def __len__(self):  ...  # Required abstract method

    def count(self, value): ...  # Optionally override a mixin method


class D:  # No inheritance
    def __init__(self): ...  # Extra method not required by the ABC

    def __getitem__(self, index):  ...  # Abstract method

    def __len__(self):  ...  # Abstract method

    def count(self, value): ...  # Mixin method

    def index(self, value): ...  # Mixin method


Sequence.register(D)


class E:
    def __iter__(self): ...


if __name__ == '__main__':
    print(issubclass(C, Sequence))
    print(isinstance(C(), Sequence))

    print(issubclass(D, Sequence))
    print(isinstance(D(), Sequence))

    print(issubclass(E, Iterable))
    print(isinstance(E(), Iterable))
