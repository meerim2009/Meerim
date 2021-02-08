def shift(l, n):
    if n < 0:
        n = abs(n)
        for i in range(n):
            l.append(l.pop(0))
    else:
        for i in range(n):
            l.insert(0, l.pop())


nums = [4, 5, 6, 7, 8, 9, 0]
print(nums)

shift(nums, -2)
print(nums)

shift(nums, 3)
print(nums)

