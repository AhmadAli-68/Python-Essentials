with open('Q9_file1.txt') as f:
  content1 = f.read()
  
with open('Q9_file2.txt') as f:
  content2 = f.read()

if (content1 == content2):
  print('Yes these files have identical content.')

else: 
  print('No these files have no identical content.')