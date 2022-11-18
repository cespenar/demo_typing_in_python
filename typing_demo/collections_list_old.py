from __future__ import annotations  # Python >= 3.7

from typing import List  # Python >= 3.5


def upper_split(text: str) -> list[str]:
    """
    Python >=3.7
    It looks exactly like the new version, but requires importing `annotations`.
    This behaviour was made default in Python 3.9, so in the new versions
    nothing has to be imported anymore.
    """
    return text.upper().split()


def upper_split_ancient(text: str) -> List[str]:
    """
    Python >=3.5
    `typing.List`, `typing.Set`, `typing.Sequence`, etc. are now deprecated
    and will be eventually removed in the future versions.
    """
    return text.upper().split()
