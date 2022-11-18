from collections.abc import Mapping


def print_dict(dictionary: dict[str, int]) -> None:
    for key, value in dictionary.items():
        print(key, value)


def print_mapping(mapping: Mapping[str, int]) -> None:
    for key, value in mapping.items():
        print(key, value)


if __name__ == '__main__':
    d = {'a': 1, 'b': 2, 'c': 3}
    print_dict(d)
    print_mapping(d)
