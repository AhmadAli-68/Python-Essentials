class Employee: #! base class
  company = 'i2c'
  salary = 1200000
  def show(self):
    print(f'The name is {self.company} and the salary is {self.salary}')

class Coder:
  language = 'Python'
  def printLanguage(self):
    print(f'Out of all the languages, here is your language: {self.language}')

class Programmer(Employee, Coder): #! derived or child class
  company = 'Devsinc'
  def showLanguage(self):
    print(f'The name of the company is {self.company} and they are working in {self.language} language')

a = Employee()
b = Programmer()

b.show()
b.showLanguage()
b.printLanguage()