class TwoDVector:
  def __init__(self, i, j):
    self.i = i
    self.j = j
  
  def show2DVector(self):
    print(f'The vector is {self.i}i + {self.j}j')

class ThreeDVector(TwoDVector):
  def __init__(self, i, j, k):
    super().__init__(i, j)
    self.k = k
  
  def show3DVector(self):
    print(f'The vector is {self.i}i + {self.j}j + {self.k}k')

twoD = TwoDVector(1, 2)
threeD = ThreeDVector(5, 2, 3)

threeD.show2DVector()
threeD.show3DVector()