class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"The name of Employee :{self.id} is {self.name}")

class Programer(Employee):
    def showLanguage(self):
        print("The Default Language is python")

e1=Employee("Rohan das",400)
e1.showDetails()
e2=Programer("Harry",210)
e2.showDetails()
e2.showLanguage()