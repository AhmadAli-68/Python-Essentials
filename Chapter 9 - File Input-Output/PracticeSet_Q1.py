f = open('Q1_poem.txt')

content = f.read()
if('Twinkle' in content or 'twinkle' in content):
  print('The word twinkle is present in the content.')

else:
  print('The word twinkle is not present in the content')

f.close()