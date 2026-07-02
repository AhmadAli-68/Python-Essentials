class Employee:
  language = 'Python' # this is a class attribute
  salary = 1200000
  
  def getInfo(self):
    print(f"The language is {self.language}. And the salary is {self.salary}")
  
  def greet(self):
    print('Good Morning!')

Ahmad = Employee()

#Ahmad.language = "Javascript" # this is the instance (object) attribute
print(Ahmad.language, Ahmad.salary)

Ahmad.getInfo()
# Employee.getInfo(Ahmad)
Ahmad.greet() # will throw the same error as line no. 12, so that's why we used self parameter

# At line 12, Ahmad.getInfo(), background me Employee.getInfo(Ahmad) me convert hota hai, Means yeh is trha run hoga, tbhi yaha error aya k "Employee.getInfo() takes 0 positional arguments but 1 was given".