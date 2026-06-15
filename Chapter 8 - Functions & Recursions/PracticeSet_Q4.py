'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5
sum(n) = (n - 1) + n
'''

def sum(n):
  if (n == 1):
    return 1
  return sum(n - 1) + n

num = int(input("Enter the number that you want to get sum of: "))
result = sum(num)
print(result)