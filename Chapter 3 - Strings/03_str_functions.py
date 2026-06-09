name = "AHMAD IS LEGENDARY."
print(name)
print(len(name))
print(name.endswith("d"))
print(name.startswith("A"))
print(name.casefold()) #? convert all letters into small alphabets.
print(name.capitalize()) #? will change only the  first word's letter to capital.
print(name.title()) #? will change every word's first letter to capital.

index = name.find("is")
print(index)

replaced_String = name.replace("legendary", "strong") #? will replace legendary with strong
print(replaced_String)