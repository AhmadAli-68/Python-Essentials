from functools import reduce

lst = [1, 2, 6, 8, 9, 10, 15, 14, 13, 20, 34, 3434, 55, 64343, 35, 85, 78, 75, 45, 5]

def greater(a, b):
  if a > b :
    return a
  return b

print(reduce(greater, lst))