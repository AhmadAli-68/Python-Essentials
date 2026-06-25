words = ['Donkey', 'bad', 'gande', 'ganda']

with open('Q5_file.txt', 'r') as f:
  content = f.read()

for word in words:
  content = content.replace(word, "*" * len(word))

with open('Q5_file.txt', 'w') as f:
  f.write(content)