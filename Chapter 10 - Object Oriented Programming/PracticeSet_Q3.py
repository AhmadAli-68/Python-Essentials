class Demo:
  a = 4

o = Demo()
print(o.a) # prints the class attribute because the instance attribute is not present.

o.a = 0 # instance attribute is set
print(o.a) # Prints the instance attribute because attribute is now present

print(Demo.a) # prints the class attribute.