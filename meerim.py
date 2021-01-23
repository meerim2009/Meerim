a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
x = input("Введите операцию между числами")
if x == '+':
    print(a+b)
elif x == '-':
    print(a-b)
elif x == '*':
    print(a*b)
elif x == '/':
    print(a/b)
elif x == '//':
    print(a//b)
elif x == '%':
    print(a%b)

else:
    print("Повторите еще раз")

