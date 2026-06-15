def removeLetter(l, word):
  n = []
  for item in l:
    if (item != word):
      n.append(item.strip(word))
  return n

l = ['Ahmad', 'Sheraz', 'Abdul Rehman', 'Sheikh', 'Rehman']
print(removeLetter(l, 'Rehman'))