word = 'Donkey'

with open('Q4_file.txt', 'r') as f:
  content = f.read()

newContent = content.replace(word, '######')

with open('Q4_file.txt', 'w') as f:
  f.write(newContent)