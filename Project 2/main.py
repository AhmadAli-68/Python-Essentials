import random

number = random.randint(1, 100)
userInput = -1
guesses = 1

while (userInput != number):
  userInput = int(input('Guess the number: '))

  if(userInput > number):
    print('Your guess is high. Enter the lower number please.')
    guesses += 1
  elif(userInput < number):
    print('Your guess is low. Enter the higher number please.')
    guesses += 1

print(f'\nCongratulation! You have guessed the right number which is {number} in {guesses} attempts.')