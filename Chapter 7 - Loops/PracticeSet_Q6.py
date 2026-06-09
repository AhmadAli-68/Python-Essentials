# let's suppose the number is 5, its factorial will be 1 x 2 x 3 x 4 x 5, which is equal to 120

num = int(input("Enter the number: "))
product = 1

for i in range (1, num + 1):
  product = product * i
print(f"The factorial of {num} is {product}")