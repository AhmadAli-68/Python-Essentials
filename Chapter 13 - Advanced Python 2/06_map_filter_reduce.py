# Map function

lst = [1, 2, 3, 4, 5]

square = lambda x: x * x

sqList = map(square, lst)
print(list(sqList))

#? Filter Function

def even(n):
  if n % 2 == 0 :
    return True
  return False

onlyEven = filter(even, lst)
print(list(onlyEven))

#* Reduce Function

from functools import reduce

multiply = lambda a, b: a * b

print(reduce(multiply, lst))