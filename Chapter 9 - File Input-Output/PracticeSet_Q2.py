import random

def game():
  print('You ar playing the game...')
  score = random.randint(1, 65)
  # Fetch the high score
  with open('Q2_Hi_Score.txt') as f:
    HiScore = f.read()
    if(HiScore != ""):
      HiScore = int(HiScore)
    
    else:
      HiScore = 0

  print(f'Your score: {score}')
  
  if (score > HiScore):
    with open('Q2_Hi_Score.txt', 'w') as f:
      f.write(str(score))
  return score

game()