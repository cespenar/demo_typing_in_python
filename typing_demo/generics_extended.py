from collections import Counter
from collections.abc import Iterable, Hashable
from decimal import Decimal
from fractions import Fraction
from statistics import mode
from typing import TypeVar


def user_mode_float(data: Iterable[float]) -> float:
    """
    The annotation is wrong - user_mode can be used for many types of data, not
    only the types consistent with float.
    """
    pairs = Counter(data).most_common()
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]


T = TypeVar('T')


def user_mode_generic(data: Iterable[T]) -> T:
    """
    This annotation is also incorrect - it accepts every iterable conistent with
    Iterable[T], including iterables of unhashable types that Counter cannot
    handle.
    """
    pairs = Counter(data).most_common()
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]


NumberT = TypeVar('NumberT', float, Decimal, Fraction, str)


def user_mode_restricted(data: Iterable[NumberT]) -> NumberT:
    """
    str in NumberT? Really? Also, we can't keep listing the types forever, as
    we realize the function can deal with them.
    """
    pairs = Counter(data).most_common()
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]


HashableT = TypeVar('HashableT', bound=Hashable)


def user_mode_hashable(data: Iterable[HashableT]) -> HashableT:
    """
    Much better - now we're working only with the hashable types.
    """
    pairs = Counter(data).most_common()
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]


if __name__ == '__main__':
    numbers_int = [1, 1, 2, 3, 3, 3, 3, 4]
    colors = ['red', 'blue', 'blue', 'red', 'green', 'red', 'red']

    print(mode(numbers_int))
    print(mode(colors))

