class Employee:
  language = 'Python' # this is a class attribute
  salary = 1200000
  
  def getInfo(self):
    print(f"The language is {self.language}. And the salary is {self.salary}")
  
  @staticmethod # decorator to mark greet as a static method 
  def greet():
    print('Good Morning!')

Ahmad = Employee()

#Ahmad.language = "Javascript" # this is the instance (object) attribute
print(Ahmad.language, Ahmad.salary)

Ahmad.getInfo()
# Employee.getInfo(Ahmad)
Ahmad.greet()

#? humara aik greet function hai Employee class me, usy hume aik argument pass krna prta tha. jaisy k 'self', hum self k ilawa kuch aur parameter bhi use kr skty hain... but self thora descriptive hai, isi liye hum yehi use krty hain.

#* Let's suppose hum chahty hain k self na use krain, koi bhi argument pass kiye bina humara function run hojaye... to us k liye "@staticMethod" use krty hain. yeh aik decorator hota hai.