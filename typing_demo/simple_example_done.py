# Example: better editor autocompletion with type hints

def get_full_name(first_name: str, last_name: str) -> str:
    """Annotated function."""
    full_name = f'{first_name.title()} {last_name.title()}'
    return full_name


if __name__ == '__main__':
    print(get_full_name('jakub', 'ostrowski'))
