class Employee:
  language = 'Python' # this is a class attribute
  salary = 1200000

Ahmad = Employee()
Ahmad.name = "Ahmad Ali" # this is the instance (object) attribute
print(Ahmad.name, Ahmad.language)

sheraz = Employee()
sheraz.name = 'Sheraz'
print(sheraz.name, sheraz.language, sheraz.salary)

#? Here name is the object attribute and salary and language are class attributes as they directly belong to the class. 