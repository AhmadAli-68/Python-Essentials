with open('Q8_this.txt', 'r') as f:
  content = f.read()

with open('Q8_this_copy.txt', 'w') as f:
  f.write(content)