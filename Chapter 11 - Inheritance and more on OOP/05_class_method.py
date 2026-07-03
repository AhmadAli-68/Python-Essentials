# A class method is a method which is bound to the class and not the object of the class. 

#? @classmethod decorator is used to create a class method.

#* class method, basically, aik tarika hai, humare pas, jo aik method k andr class ko directly access krny ka.

class Employee():
  a = int(input('Enter the number: '))
  
  @classmethod # it is a decorator. jo sirf class attribute print kre ga, na k instance attribute, which is 'e.a = 45'
  def showValue(cls):
    print(f'The class attribute of a is {cls.a}')

e = Employee()
e.a = 45 # it is the instance attribute
e.showValue()