from fractions import Fraction


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


#差 a - b
class sub(Base):
    operation = 'a - b ='

    def __init__(self, a, b):
        super().__init__(a, b)
        self.result = self.a - self.b


#積　a * b
class mul(Base):
    operation = 'a * b ='

    def __init__(self, a, b):
        super().__init__(a, b)
        self.result = self.a * self.b


#商 a / b
class div(Base):
    operation = 'a / b ='
    
    def __init__(self, a, b):
        super().__init__(a, b)
        if self.b == 0:
            self.result = 'division by 0'
        else:
            self.result = self.a / self.b


#既約分数 a / b
class irreducible_frac(Base):
    operation = 'Irreducible Fraction of a / b:'

    def __init__(self, a, b):
        super().__init__(a, b)
        self.result = Fraction(self.a, self.b)


#余り a % b
class remainder_div(Base):
    operation = 'a % b ='

    def __init__(self, a, b):
        super().__init__(a, b)
        self.result = self.a % self.b


def main():
    a = int(input('Input integer a: '))
    b = int(input('Input integer b: '))

    sum(a, b).print_result()
    sub(a, b).print_result()
    mul(a, b).print_result()
    div(a, b).print_result()
    irreducible_frac(a, b).print_result()
    remainder_div(a, b).print_result()

if __name__ == '__main__':
    main()