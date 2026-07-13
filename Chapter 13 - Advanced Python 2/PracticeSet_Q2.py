name = input('Enter your name: ')
marks = int(input('Enter your marks: '))
phoneNumber = int(input('Enter your phone number: '))

formattedData = 'The name of the student is {}, his marks are {} and phone number is {}'.format(name, marks, phoneNumber)

print(formattedData)