def fraction(num, den):
    pass


class Fraction:

    def __init__(self,num,den):  # num числитель, den знаменатель

        self.num = num
        self.den = den

    def str(self):
        return str(self.num) + '/' + str(self.den)


    def add(self, other):
        fraction1 = Fraction(num=1, den=2)
        fraction2 = Fraction(num=2, den=3)
        # print(Fraction3num, "/", fraction3.den)
        return Fraction(self.num * fraction2.den + self.den * fraction2.den, fraction2.den * self.den)

    def sub(self, other):
        fraction1 = Fraction(num=2, den=3)
        fraction2 = Fraction(num=2, den=3)
        print(Fraction.sub())
        return Fraction(self.num * fraction2.den - self.den * fraction2.den, fraction2.den * self.den)

    def mul(self, other):
        fraction1 = Fraction(num=4, den=5)
        fraction2 = Fraction(num=5, den=6)
        print(Fraction.mul())
        return Fraction(self.num*fraction2.num,self.den*fraction2.den)

    def truediv(self, other):
        fraction1 = Fraction(num=1, den=2)
        fraction2 = Fraction(num=2, den=3)
        print(Fraction.truediv())
        return Fraction(self * self.invert(fraction2))

    def repr(self):
        return '{}/{}'.format(self.num, self.den)


a = Fraction
print(a.add())


