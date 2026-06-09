friends = ['Apple', 'Orange', 34, False, 'Ahmad', 'Sheraz']
# print(friends)

# ? append()

friends.append("Sheikh")
print(friends)

# ? sort() & reverse()

l1 = [1,56,34,89,45,2,0,5,3,9,23]
# l1.sort()
# l1.reverse()
print(l1)

# ? insert(index, value)

l1.insert(4, 200) # here we insert 200 at index 4.
print(l1)

# pop()

print(l1.pop(4)) # it will print/return the value that is popped from the list.
print(l1)

# remove()

l1.remove(89)
print(l1)