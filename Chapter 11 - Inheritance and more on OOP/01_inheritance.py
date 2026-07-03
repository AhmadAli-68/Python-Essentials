class Employee: #! base class
  company = 'i2c'
  def show(self):
    print(f'The name is {self.name} and the salary is {self.salary}')

#? Inheritance is a way of creating a new class from an existing class. 

# class Programmer:
#   company = 'Devsinc'
#   def show(self):
#     print(f'The name is {self.name} and the salary is {self.salary}')
  
#   def showLanguage(self):
#     print(f'The name is {self.name} and he is good in {self.language} language')

# So instead of doing this, we will inherit the properties from class Employee

class Programmer(Employee): #! derived or child class
  company = 'Devsinc'
  def showLanguage(self):
    print(f'The name is {self.name} and he is good in {self.language} language')

a = Employee()
b = Programmer()

print(a.company, b.company)