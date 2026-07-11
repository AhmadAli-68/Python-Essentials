# List Comprehension is an elegant way to create lists based on existing lists.

myList = [1, 2, 9, 5, 3, 6, 4]

# squaredList = []
# for item in myList:
#   squaredList.append(item * item)

#? This can be simplified by using list comprehensions

squaredList =  [i * i for i in myList]

print(squaredList)