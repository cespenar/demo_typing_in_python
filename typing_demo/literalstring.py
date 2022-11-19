# PEP 675 – Arbitrary Literal String Type
# https://peps.python.org/pep-0675/

from typing import LiteralString


def run_query(sql: LiteralString) -> None:
    ...


def caller(arbitrary_string: str, literal_string: LiteralString) -> None:
    run_query('SELECT * FROM students')  # ok
    run_query(literal_string)  # ok
    run_query('SELECT * FROM ' + literal_string)  # ok
    run_query(arbitrary_string)  # type checker error
    run_query(  # type checker error
        f'SELECT * FROM students WHERE name = {arbitrary_string}'
    )
