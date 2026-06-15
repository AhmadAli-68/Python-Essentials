# a = 12
# b = 45
# c = 56

# avg = (a + b + c) / 3

# print(avg)

#? let's suppose we do the same thing 50 times. But this will make our code repeatable. To prevent that we use functions.

#? This is called function definition.

def avg():
  a = int(input('Enter the first number: '))
  b = int(input('Enter the second number: '))
  c = int(input('Enter the third number: '))
  
  average = (a+b+c) / 3
  print(average)

avg() #? This is called function call 

#* QUICK QUIZ

def greet():
  name = input("What is your name? ")
  print(f"Have a nice day, {name}!!")
  
greet()