class Employee:
  language = 'Python' # this is a class attribute
  salary = 1200000

Ahmad = Employee()
Ahmad.language = "Javascript" # this is the instance (object) attribute
print(Ahmad.language, Ahmad.salary)

#? Instance attributes, take preference over class attributes during assignment & retrieval. 

#* means maine class attribute ko instance attribute se override krdiya. Ab agr mai Ahmad.language print kru ga to javascript print hoga, na k Python.