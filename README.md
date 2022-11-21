# Static typing in Python

***

* different typing systems
* what is and was in Python?
* duck typing
* static duck typing
* what are type hints?
* type aliases
* NewType
* structural vs nominal subtyping
* demo how to use types in older versions of Python
* function annotations

### Types usable in annotations

1. `typing.Any`
    * Special type indicating an unconstrained type.
    * Every type is compatible with `Any`
    * `Any` is compatible with every type
2. Simple types and classes
    * `str`
    * `int`
    * `float`
    * `bool`
    * `bytes`
    * Any class you wrote or imported
3. `typing.Self`
    * Special type to represent the current enclosed class
    * Useful for alternative constructors
    * Python 3.11
4. `typing.LiteralString`
    * Python 3.11
5. `typing.Optional` and `typing.Union`
    * `Optional` is appropriate when `None` is allowed
    * `Union[X, Y]` == `X | Y`
    * `Optional[X]` == `Union[X, None]` == `X | None`
    * `X | Y | ...`
    * Union type expressions - Python 3.10
    * For Python < 3.10: avoid `Optional[X]`, use `Union[X, None]`
6. Generic collections, including tuples and mappings
    * Lists:
        * Subscription syntax: `list[X]` (Python >= 3.9) - homogeneous
          collections
        * `stuff: list[Any]` == `stuff: list` - heterogeneous collections, rare
          stuff
    * Tuples:
        * Tuples as records (with named fields or not): `tuple[X, Y, Z]`
        * Tuples as immutables sequences: `tuple[X, ...]` - one or more
          elements
        * `stuff: tuple[Any]` == `stuff: list` - objects of any type,
          unspecified length
    * Mappings:
        * `dict[X, Y]`
        * `collections.abc.Mapping[X, Y]`
        * `collections.abc.MutableMapping[X, Y]`
7. Abstract base classes
    * Robustness
      principle ([Postel's law](https://en.wikipedia.org/wiki/Robustness_principle)):
      "be conservative in what you send, be liberal in what you accept"
    * Abstract base classes that can be used to test whether a class provides a
      particular interface; for example, whether it is hashable or whether it
      is a mapping
    * `collections.abc` - the most useful module
8. Generic iterables
    * `Sequence` and `Iterable` - the most common parameter types
9. Parametrized generics and `TypeVar`
    * The way to define custom type usable in classes, functions and collections
10. `typing.Protocol`
    * Protocols define interfaces. _Static_ protocols are used only for type checking
    * Static duck typing (structural subtyping)
    * Predefined protocols: `Iterable`, `Hashable`, `Reversible`, etc.
    * Custom protocols: subclasses of `typing.Protocol`
11. `collections.abc.Callable`
    * Used for annotating higher-order functions
12. `typing.Never` and `typing.NoReturn`
    * `Never` - the bottom type, a type that has no members
    * New in Python 3.11
    * `NoReturn` - special type indicating that a function never returns
    * Replaced by `NoReturn`

### Sources

* [Python documentation](https://docs.python.org/3/library/typing.html)
* [mypy documentation](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
* [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/), Luciano Ramalho,
  O'Reilly Media, Inc., April 2022
* [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)
* [PEP 673 – Self Type](https://peps.python.org/pep-0673/)
* [PEP 675 – Arbitrary Literal String Type](https://peps.python.org/pep-0675/)