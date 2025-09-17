# ? Tuple is also like list, but it is immutable, the values inside the tuple cannot be changed.

a = (1,2,5,7,8,0)
# print(type(a))

b = (1) #? this is not a tuple
# print(type(b)) #* it will return <class 'int'>

c = (1,) #? this is a single value tuple
# print(type(c)) #* <class 'tuple'>

#! *******************************************************

#? Tuple Methods

# * count()

tuple1 = (1, 45, 34, 78, 45, False, 45, "Ahmad")
count = tuple1.count(45)
print(count)

# * index()

ind = tuple1.index(45)
print(ind)

print(len(tuple1))