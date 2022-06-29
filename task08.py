class Base:   
    result = 0
    operation = ''

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_result(self):
        print(self.operation, self.result)


def main():
    a = int(input('Input integer a: '))
    b = int(input('Input integer b: '))


if __name__ == '__main__':
    main()