dict1 = {}

name = input("Enter your friend's name: ")
lang = input("Enter language name: ")
dict1.update({name: lang})

name = input("Enter your friend's name: ")
lang = input("Enter language name: ")
dict1.update({name: lang})

name = input("Enter your friend's name: ")
lang = input("Enter language name: ")
dict1.update({name: lang})

name = input("Enter your friend's name: ")
lang = input("Enter language name: ")
dict1.update({name: lang})

print(dict1)

#? Problem 7: if the names of friends (key), but but different language (value), then it will get updated. For example:

#* If the user enter friend's name "Ahmad" (key), and value "Python" (value), and later enter the friend's name "Ahmad" (key) and value "JS" (value), then value will get updated as "JS" and we know in dictionaries, the keys are unique identifiers so key will be appeared only one.

#? Problem 8: If 2 friends (key) have same languages (value), then it will remain as it was before. Because values can be same 