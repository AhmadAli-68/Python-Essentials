a = 89 # it is a global variable and everyone can access this variable

def fun():
  global a # yeh keyword (global a), global variable a (at line 1) ki value change krdeta hai a = 89 -> a = 3

  a = 3 # it is the local variable, which is only used by this function, and no one can access this variable
  print(a)

fun()
print(a)