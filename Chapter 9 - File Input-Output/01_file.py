'''
a = 'a very long string with emails'

emails = []
it took 3 seconds to run
-> program run
-> Email generate
-> Program end

-> RAM will be cleared after program terminates. Because RAM is a volatile memory

-> But if we want to persist (save) our program after running then we will use a File.

-> HDD or SSD are non-volatile memories. which means we can persist (store) our data permanently or as long as we want.
'''

f = open("file.txt") # open() is a built in function which is use to open files.
data = f.read() # .read() is used to read the data from the file.
print(data)
f.close() # .close() is used to close the file after opening it, It is very important and can't be missed