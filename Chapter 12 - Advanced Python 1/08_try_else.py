try:
  a = int(input('Enter a number: '))
  print(a)

except Exception as e:
  print(e)

else:
  print('I am inside else.')

#? Ismy yeh hoga k agr humara try block wala code sai run hota hai to execution flow else block me chala jaye ga. agr nai to phir except block me jayega