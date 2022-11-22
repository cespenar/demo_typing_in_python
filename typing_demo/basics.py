if __name__ == '__main__':
    # Basic syntax
    # Variable annotations
    name: str
    age: int
    salary: float = 500_000.0

    # Extremely simple example, but age might be interesting here...
    name = input('Name: ')
    age = int(input('Age: '))

    print(name, type(name))
    print(age, type(age))
    print(salary, type(salary))
