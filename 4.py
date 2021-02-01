try:
    a = int(input("Hello"))
    x = a + 1
except TypeError:
    print("Не складывать число и строку")
except ZeroDivisionError:
    print("Hello")
finally:
    print("Finally done")