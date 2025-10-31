a = int(input("Enter your age: "))

# if elif else ladder

if (a >= 18):
    print('You are above the age of consent')
    print('Good for you')

elif (a <= 0):
    print("You can't enter the 0 or a negative number as an age.")
    
else:
    print('You are below the age of consent')

print("End of the execution!")