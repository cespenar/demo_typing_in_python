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
7. Abstract base classes
8. Generic iterables
9. Parametrized generics and `TypeVar`
10. `typing.Protocols`
11. `typing.Callable`
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