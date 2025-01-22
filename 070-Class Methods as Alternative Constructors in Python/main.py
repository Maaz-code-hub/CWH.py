class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    @classmethod                   #use cls instead of self in class method
    def fromstr(cls,string):                          
        return cls(string.split("-")[0],int(string.split("-")[1]))

e=Employee("Harry",12000)
print(e.name)
print(e.salary)

string="John-12000"
e2=Employee.fromstr(string)
print(e2.name)
print(e2.salary)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
    
Person=Person.from_string("John Doe,30")
print(Person.name,Person.age)