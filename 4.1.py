# 4.1 Даны два различных вещественных числа. Определить: а) какое из них больше;
# б) какое из них меньше.
a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
if a > b:
    print(a)
if b > a:
    print(b)
# 4.19 Известны площади круга и равностороннего треугольни-
# ка. Определить:
# а) уместится ли круг в треугольнике?
# б) уместится ли треугольник в круге?
x = int(input("Введите площадь круга"))
y = int(input("Введите площадь треугольника"))
if x > y:
    print("уместится")
    if x < y:
        print("не уместится")
    else:
        if y > x:
            print("уместится")
            if y < x:
                print("не уместится")


# 4.40 Проверить, принадлежит ли число, введенное с клавиа- туры, интервалу (–5, 3).
a = int(input("Введите число"))
if -5 <= a <= 3:
    print('yes')
else:
    print("no")

# 5.40 Дано 9-значное число. Определить сумму его цифр. Ве- личины для хранения всех 9 цифр числа не использовать.
number = str(input('Введите число: '))
sum_ = 0
for char in number:
    sum_ += int(char)
print(sum_)

# Циклический сдвиг
def shift(l, n):
    if n == 0:
        return l
    if n > 0:
        for i in range(n):
            a = l.pop()
            l.insert(0, a)
        return l
    if n < 0:
        for i in range(abs(n)):
            l.append(l[0])
            l.remove(l[0])
        return l
num = [1, 2, 3, 4, 5, 0]
print(num)

shift(num, -2)
print(num)

shift(num, 3)
print(num)

