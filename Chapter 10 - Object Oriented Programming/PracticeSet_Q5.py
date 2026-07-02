from random import randint

class Train:
  def __init__(self, trainNo):
    self.trainNo = trainNo
  
  def book(self, trainNo, fro, to):
    print(f'Train is booked in train no. {trainNo}, from {fro} to {to}')
  
  def getStatus(self, trainNo):
    print(f'Train no. {trainNo} is running on time.')
  
  def getFare(self, trainNo, fro, to):
    print(f'Ticket fare for train no. {trainNo}, from {fro} to {to} is {randint(222, 5555)}')

TrainNo = int(input('Enter the train no: '))
t = Train(TrainNo)

pickUp = input('Enter the pick up point: ')
destination = input('Enter the destination point: ')

t.book(TrainNo, pickUp, destination)
t.getStatus(TrainNo)
t.getFare(TrainNo, pickUp, destination)