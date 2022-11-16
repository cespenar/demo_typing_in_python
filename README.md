# Static typing in Python

***

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
4. `typing.Optional` and `typing.Union`
5. Generic collections, including tuples and mappings
6. Abstract base classes
7. Generic iterables
8. Parametrized generics and `TypeVar`
9. `typing.Protocols`
10. `typing.Callable`
11. `typing.Never` and `typing.NoReturn`

### Sources

* [Python documentation](https://docs.python.org/3/library/typing.html)
* [mypy documentation](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
* [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/), Luciano Ramalho,
  O'Reilly Media, Inc., April 2022
* [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)
* [PEP 673 – Self Type](https://peps.python.org/pep-0673/)