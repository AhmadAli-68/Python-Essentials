class Complex:
  def __init__(self, real, imaginary):
    self.real = real
    self.imaginary = imaginary
  
  def __add__(self, c2):
    return Complex(self.real + c2.real, self.imaginary + c2.imaginary)
  
  def __mul__(self, c2):
    realPart = self.real * c2.real - self.imaginary * c2.imaginary
    imaginaryPart = self.real * c2.imaginary + self.imaginary * c2.real
    return Complex(realPart, imaginaryPart)
  
  def __str__(self):
    return f'{self.real} + {self.imaginary}i'

c1 = Complex(1, 3)
c2 = Complex(2, 5)
print(f'With Addition, the complex number is: {c1 + c2}')
print(f'With Multiplication, the complex number is: {c1 * c2}')