# Typing in Python

***

### Introduction

***

* Type annotations were introduced in Python 3.5
* `name: str = Jakub`
* The Python runtime does not enforce type annotation
* Python is a dynamically typed language
* Gradual type hinting in Python
* Duck typing - "if it walks and quacks like a duck, it is a duck"
* Static type checkers verify the code without running it
* Static type checkers: [mypy](http://mypy-lang.org/), [pytype](https://google.github.io/pytype/),
  [pyre](https://pyre-check.org/), [pyright](https://github.com/microsoft/pyright)
* Implicit runtime data validation (e.g. [pydantic](https://pydantic-docs.helpmanual.io/))

"It should also be emphasized that **Python will remain a dynamically typed language, and the authors have no desire to
ever make type hints mandatory, even by convention.**" - [PEP 484](https://peps.python.org/pep-0484/)

### Types usable in annotations

***

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
    * Replaced by `Never`

### Additional remarks

***

* There are many more types, classes and functions in the `typing` module
* Notables use cases of type hints: Pydantic, FastAPI, httpx

### Summary

***

* Type hints are great
* They make the code more readable and understandable
* They help finding bugs (but they cannot replace testing)
* They allow more IDEs to have more accurate and smarter suggestion engine
* Very high cognitive cost of annotating some simple, but powerful functions and APIs

### Sources

***

* [Python documentation](https://docs.python.org/3/library/typing.html)
* [mypy documentation](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
* [The state of type hints in Python](https://bernat.tech/posts/the-state-of-type-hints-in-python/), Bernát Gábor
* [Hypermodern Python Chapter 4: Typing](https://cjolowicz.github.io/posts/hypermodern-python-04-typing/)
* [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/), Luciano Ramalho,
  O'Reilly Media, Inc., April 2022
* [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)
* [PEP 544 – Protocols: Structural subtyping (static duck typing)](https://peps.python.org/pep-0544/)
* [PEP 673 – Self Type](https://peps.python.org/pep-0673/)
* [PEP 675 – Arbitrary Literal String Type](https://peps.python.org/pep-0675/)
* [Awesome Python Typing](https://github.com/typeddjango/awesome-python-typing)