from typing import Never, NoReturn


def never_call_me(arg: Never) -> None:
    pass


def int_or_str(arg: int | str) -> None:
    never_call_me(arg)  # type checker error
    match arg:
        case int():
            print('It is an int')
        case str():
            print('It is a str')
        case _:
            never_call_me(arg)  # ok, arg is of type Never


def stop() -> NoReturn:
    raise RuntimeError('no way')
