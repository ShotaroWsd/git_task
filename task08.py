from fractions import Fraction
import math
import numpy as np

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


#累乗 a ** b
class power(Base):
    operation = 'a ** b ='

    def __init__(self, a, b):
        super().__init__(a, b)
        self.result = self.a ** self.b


#累乗根 aのb乗根
class root(Base):
    operation = 'the b th root of a:'

    def __init__(self, a, b):
        super().__init__(a, b)
        self.result = self.a ** (1 / self.b)


#対数 底b, 真数a
class log(Base):
    operation = 'log_b a ='

    def __init__(self, a, b):
        super().__init__(a, b)
        if self.a > 0 and self.b > 0 and self.a != 1:
            self.result = math.log(self.a, self.b)
        else:
            self.result = 'error (Cause: a <= 0 or a == 1 or b <= 0)'


#進数変換 b進法でaを表す
class base_convert(Base):
    operation = 'Convert a to Base b:'

    def __init__(self, a, b):
        super().__init__(a, b)
        if 1 < self.b < 37:
            self.result = np.base_repr(self.a, self.b)
        else:
            self.result = 'error (Cause: a < 2 or a > 36)'


#最大公約数
class gcd(Base):
    operation = 'Greatest Common Divisor:'

    def __init__(self, a, b):
        super().__init__(a, b)
        self.result = math.gcd(self.a, self.b)


def main():
    a = int(input('Input integer a: '))
    b = int(input('Input integer b: '))

    sum(a, b).print_result()
    sub(a, b).print_result()
    mul(a, b).print_result()
    div(a, b).print_result()
    irreducible_frac(a, b).print_result()
    remainder_div(a, b).print_result()
    power(a, b).print_result()
    root(a, b).print_result()
    log(a, b).print_result()
    base_convert(a, b).print_result()
    gcd(a, b).print_result()


if __name__ == '__main__':
    main()