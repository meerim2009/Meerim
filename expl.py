while True:
    try:
        num1 = input("Введите первое число")
        num2 = input("Введите второе число")
        znak = input("Введите знак")
        if num1 is None or num2 is None or znak is None:
            raise ValueError
        num1 = int(num1)
        num2 = int(num2)
        if znak == "+":
            print(num1 + num2)
    try:
        if znak == "/":
            print(num1 / num2)

    except ZeroDivisionError:
        print("На ноль делить нельзя")
        continue

        break
    except ValueError:
        print("Введите еще раз ")
    continue










