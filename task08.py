#スーパークラス　継承して四則演算他の計算と出力を行う
class Base:   
    result = 0
    operation = ''

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_result(self):
        print(self.operation, self.result)

#和 a + b
class sum(Base):
    operation = 'a + b ='

    def __init__(self, a, b):
        super().__init__(a, b)
        self.result = self.a + self.b


def main():
    a = int(input('Input integer a: '))
    b = int(input('Input integer b: '))

    sum(a, b).print_result()

if __name__ == '__main__':
    main()