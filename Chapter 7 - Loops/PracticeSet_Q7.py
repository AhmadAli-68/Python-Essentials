'''
for n = 3
  *
 ***
*****
'''

'''
    *
   ***
  *****  <- right side
 *******
*********

when the loop is printing the spaces ans stars, we will not focus on the right side of the stars.
'''

num = int(input("Enter the number: "))

for i in range(1, num + 1):
  print(" " * (num - i), end="") # print statement gives new line by default, this end="" argument will not give the new line.
  print("*" * (2*i - 1), end="")
  print("")