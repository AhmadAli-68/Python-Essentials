class Employee:
  language = 'Python'
  salary = 1200000
  
  def __init__(self, name, language, salary): # dunder method which is automatically called.
    self.name = name
    self.language = language
    self.salary = salary
    print('I am creating an object.')
  
  def getInfo(self):
    print(f"The language is {self.language}. And the salary is {self.salary}")
  
  @staticmethod
  def greet():
    print('Good Morning!')

Ahmad = Employee('Abdul Rehman', 'JavaScript', 1300000)
# Ahmad.name = 'Ahmad'
print(Ahmad.name, Ahmad.language, Ahmad.salary)

Ahmad.getInfo()
Ahmad.greet()

#? __init__() is a special method which is first run as soon as the object is created. 

#? __init__() method is also known as constructor. In Python, these type of methods are called dunder methods