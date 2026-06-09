a1 = int(input('Enter the number 1: '))
a2 = int(input('Enter the number 2: '))
a3 = int(input('Enter the number 3: '))
a4 = int(input('Enter the number 4: '))

if (a1 > a2 and a1 > a3 and a1 > a4):
    print(f"{a1} is greater")
elif (a2 > a1 and a2 > a3 and a2 > a4):
    print(f"{a2} is greater")
elif (a3 > a1 and a3 > a2 and a3 > a4):
    print(f"{a3} is greater")
else:
    print(f"{a4} is greater")