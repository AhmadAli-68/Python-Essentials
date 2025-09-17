s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 

print(len(s)) #? length wil be 2 because 20 and 20.0 are consider same when compared and as we know, in sets, there can't be any duplicate value.  

# Example

print(1 == 1.1)