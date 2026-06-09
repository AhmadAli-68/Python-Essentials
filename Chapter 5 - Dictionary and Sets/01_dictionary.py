d= {} #? Empty Dictionary

dict1 = {
    "Ahmad": 100,
    "Sheraz": 100,
    "Abdul Rehman": 100,
    "list": [1,2,4],
    0: "Sheikh"
}

# ? Dictionaries are mutable in Python.

# print(dict1, type(dict1))

print(dict1[0])
print(dict1["list"])

#todo ************* Dictionary Methods *************

# print(dict1.items()) #? it will return the key-value pairs in the form of tuples, but its type will always be <class 'dict-items'>

# print(dict1.keys()) #? it will return keys.

# print(dict1.values()) #? it will return values.

dict1.update({"Ahmad": 99, "John": 89}) #? we can update the values and add more key-values if they are not in the dictionary.

# print(dict1)

print(dict1.get("Ahmad2")) #* it will return "none"

print(dict1["Ahmad2"]) #* it will return key-error if the key doesn't present in the dictionary.