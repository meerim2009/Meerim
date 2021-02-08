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