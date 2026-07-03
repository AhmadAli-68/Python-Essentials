# super() method is used to access the methods of a super class in the derived class.

class Employee:
  def __init__(self):
    print('Constructor of the Employee class')
  a = 1

class Programmer(Employee):
  def __init__(self):
    print('Constructor of the Programmer class')
  b = 2

class Manager(Programmer):
  def __init__(self):
    super().__init__() #* What will happen here? Well, super() will invoke its parent class constructor which is a Programmer class.
    
    print('Constructor of the Manager class')
  c = 3

# o = Employee()
# print(o.a)

# p = Programmer()
# print(p.a, p.b)

m = Manager()
print(m.a, m.b, m.c)