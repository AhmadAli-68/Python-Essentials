def InchesToCM(num):
  return num * 2.54

num = int(input('Enter the number that you want to convert in CM: '))
result = InchesToCM(num)
print(f"The {num} inches is equal to {result} CM.")