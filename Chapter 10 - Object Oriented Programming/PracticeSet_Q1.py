class Programmer:
  company = 'Microsoft'
  def __init__(self, name, salary, pin):
    self.name = name
    self.salary = salary
    self.pin = pin

p = Programmer('Ahmad', 1200000, 240001)
print(p.name, p.salary, p.pin, p.company)

s = Programmer('Sheraz', 1200000, 240589)
print(s.name, s.salary, s.pin, s.company)