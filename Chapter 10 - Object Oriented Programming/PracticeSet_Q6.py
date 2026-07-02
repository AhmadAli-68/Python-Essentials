class Employee:
  language = 'Python' # this is a class attribute
  salary = 1200000
  
  def getInfo(ahmad):
    print(f"The language is {ahmad.language}. And the salary is {ahmad.salary}")
  
  def greet(ahmad):
    print('Good Morning!')

Ahmad = Employee()

print(Ahmad.language, Ahmad.salary)

Ahmad.getInfo()
Ahmad.greet()