# Data structures

from random import randint


def random_list() list:
    arr = []
    for i in range(1,1000000000,5):
      arr.append(i+randint(1,4))
      return arr
    l = random_list()
    print(len(l))
