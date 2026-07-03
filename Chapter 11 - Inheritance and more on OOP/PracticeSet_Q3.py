class Employee:
  def __init__(self, salary, increment):
    self.salary = salary
    self.increment = increment
  
  @property # this is our getter function
  def salaryAfterIncrement(self):
    return int(self.salary + (self.salary * (self.increment/100)))
  
  @salaryAfterIncrement.setter
  def salaryAfterIncrement(self, new_salary):
    self.increment = ((new_salary/self.salary) - 1) * 100

salary = int(input("Enter your salary: "))
increment = 25

emp = Employee(salary, increment)

print(f'Current increment: {emp.increment}%')
print(f'Current salary after increment: {emp.salaryAfterIncrement}')

# Take the desired new salary from the user
new_salary = int(input('\nEnter your desired salary after increment: '))

# this line automatically calls the setter
emp.salaryAfterIncrement = new_salary

print('\nAfter entering the desired salary...\n')

print(f'Original Salary: {emp.salary}')
print(f'Updated increment: {emp.increment:.2f}%')
print(f'Salary after increment: {emp.salaryAfterIncrement}')