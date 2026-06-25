with open('Q11_file.txt') as f:
  content = f.read()

with open('Q11_renamed_by_ python.txt', 'w') as f:
  f.write(content)