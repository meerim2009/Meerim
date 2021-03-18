file = open("data.text", "r")

class Human:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight


humans = []

for i in file.readLines():
    print(i.split(" "))
    print(*i.split(" "))
    humans.append(Human(*i.split(" ")))
file.close()
