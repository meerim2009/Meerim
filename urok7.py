r = open('text.txt', 'r')
r_1 = r.read(3)
for line in r:
    print(line)
print(r)
print(r_1)
r.close()   # обязательно закрыть


with open('text.txt', 'r', encoding='UTF-8') as file:
    r = file.read()
    print(r)