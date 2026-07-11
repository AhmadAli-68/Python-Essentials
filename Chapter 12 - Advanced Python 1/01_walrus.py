# Using walrus operator

if n := len([1, 2, 3, 4, 5]) > 3: 
  print(f"List is too long ({n} elements, expected <= 3)")

#? So Walrus operator yeh hota hai k... hum kisi bhi variable ko assignment k sath sath expression k tor pr bhi use kr skty hain... which means

'''
pehle hume krty thy...

n = 5

if n < 3 : and so on

but with assignment expression.... hum aik hi line me assignment ka kaam bhi kr skty hain... aur phir usi ko expressions k tor pr use kr skty hain, for conditions. For example:

if n := 5 < 3 :

This is also called Assignment Expression. 
'''