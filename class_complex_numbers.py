class Complex:


    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


    def __str__(self):
        return(self)


    def __add__(self, other):
        a = self.real + other.real
        b = self.imag + other.imag
        return Complex(a,b)

    def __sub__(self, other):
        a1 = self.real - other.real
        b1 = self.imag - other.imag
        return Complex(a1,b1)

    def __mul__(self, other):
        a2 = self.real * other.real
        b2 = self.imag * other.imag
        return Complex(a2,b2)

    def __truediv__(self, other):
        a3 = self.real * other.real + self.imag * other.imag
        b3 = self.real * other.real - self.imag * other.imag
        c = self.real**2 + other.real**2
        return Complex(a3,b3,c)


    num = complex(2, 4)
    num2 = complex(3, 5)
    print(num + num2)


