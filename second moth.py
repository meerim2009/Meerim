def fraction(num, den):
    pass


class Fraction:

    def __init__(self,num,den):  # num числитель, den знаменатель
        pass

        if den == 0:
            raise ValueError("Знаменатель не может быть нулем")

        self.num = num
        self.den = den

    def str(self):
        return str(self.num) + '/' + str(self.den)


    def __add__(self,other):
        fraction1 = Fraction(num=1, den=2)
        fraction2 = Fraction(num=2, den=3)
        print(Fraction.__add__())
        return Fraction(self.num * fraction2.den + self.den * fraction2.den, fraction2.den * self.den)

    def __sub__(self, other):
        fraction1 = Fraction(num=2, den=3)
        fraction2 = Fraction(num=2, den=3)
        print(Fraction.__sub__())
        return Fraction(self.num * fraction2.den - self.den * fraction2.den, fraction2.den * self.den)

    def __mul__(self, other):
        fraction1 = Fraction(num=4, den=5)
        fraction2 = Fraction(num=5, den=6)
        print(Fraction.__mul__())
        return Fraction(self.num*fraction2.num,self.den*fraction2.den)

    def __truediv__(self, other):
        fraction1 = Fraction(num=1, den=2)
        fraction2 = Fraction(num=2, den=3)
        print(Fraction.__truediv__())
        return Fraction(self * self.invert(fraction2))

    def repr(self):
        return '{}/{}'.format(self.num, self.den)




