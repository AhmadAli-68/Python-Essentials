class Calculator:
  def __init__(self, n):
    self.n = n
  
  def square(self):
    print(f'The square is {self.n * self.n}')
    
  def cube(self):
    print(f'The cube is {self.n ** 3}')
    
  def squareRoot(self):
    print(f'The square is {self.n ** 0.5}')
    
  @staticmethod
  def greet():
    print("Hello Ahmad!")

num = int(input('Enter the number: '))
result = Calculator(num)

result.square()
result.cube()
result.squareRoot()
result.greet()