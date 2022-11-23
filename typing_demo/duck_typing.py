# https://en.wikipedia.org/wiki/Duck_typing

class Duck:
    def swim(self):
        print('Duck swimming')

    def fly(self):
        print('Duck flying')


class Whale:
    def swim(self):
        print('Whale swimming')


if __name__ == '__main__':
    for animal in [Duck(), Whale()]:
        animal.swim()
        animal.fly()
