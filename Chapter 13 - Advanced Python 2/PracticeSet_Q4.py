def divisibleBy5(num):
  if num % 5 == 0:
    return True
  return False

lst = [1, 2, 6, 8, 9, 10, 15, 14, 13, 20, 34, 3434, 55, 64343, 35, 85, 78, 75, 45, 5]

filteredResult = list(filter(divisibleBy5, lst))
print(filteredResult)