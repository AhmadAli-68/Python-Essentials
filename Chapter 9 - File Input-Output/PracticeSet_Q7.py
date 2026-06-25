lineNo = 1

with open('Q6_log.txt', 'r') as f:
  lines = f.readlines()

for line in lines:
  if ('python' in line):
    print(f'Yes python is present in the line no. {lineNo}.')
    break
  lineNo += 1

else:
  print(f'No python is not present.')