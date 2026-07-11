# Advanced Typing Hints

from typing import List, Union, Tuple, Dict

numbers: List[int] = [1, 2, 3, 4, 5, 6]

person: Tuple[str, int] = ('Alice', 30)

scores: Dict[str, int] = {'Ahmad': 90, 'Ali': 85}

# union type for variables that can hold integer values
# union tells that a variable can be string or integer
identifier: Union[int, str] = 'ID123'
identifier = 12345

# Type Definitions

n : int = 5

name : str = 'Ahmad'

n.numerator

#? Let's suppose humary pas aik variable n = 5, jo k aik obviously integer hai. Agr mai chahu k mai int k sb functions/methods ko use kr sku to mai n ko aik explicit type de skta hu.... like below....

'''
examples:

n : int = 5
n : str = 'Ahmad'
'''

def sum(a: int, b: int) -> int:
  return a + b

print(sum(5, 5))