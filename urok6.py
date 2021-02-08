def shift(l, n):
    if n == 0:
        return l
    if n > 0:
        for i in range(n):
            a = l.pop()
            l.insert(0, a)
            return l
    if n < 0:
        for i in range(n * -1):
            l.append(l[0])
            l.remove(l[0])
            return l

