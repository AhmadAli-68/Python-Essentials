class Employee: # base or parent class
  a = 1

class Programmer(Employee): # child of Employee class but parent of Manager class
  b = 2

class Manager(Programmer): # child class of Programmer class
  c = 3

o = Employee()
print(o.a) # Prints the a attribute from class Employee
# print(o.b) #! will throw an error saying there is no attribute 'b' in Employee object 

p = Programmer()
print(p.a, p.b)

m = Manager()
print(m.a, m.b, m.c)