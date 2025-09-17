name = 'Ahmad is a good  boy and'
print(name.find("  "))

# it will detect double spaces and return the index number, if not found, then return -1

# Problem no. 4

print(name.replace("  ", " "))

# ! Strings are immutable which means that you cannot change them by applying functions on them 
# replace() does not modify the original string, it returns a new string.