class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


rits = Employee()
rits.language = "JavaScript" # This is an instance attribute
print(rits.language, rits.salary)
 