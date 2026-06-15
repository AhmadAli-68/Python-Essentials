def great(num1, num2, num3):
  if (num1 > num2 and num1 > num3):
    return num1
  elif (num2 > num1 and num2 > num3):
    return num2
  else:
    return num3

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

result = great(a, b, c)
print(f"{result} is the greatest number.")