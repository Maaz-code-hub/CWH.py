class person:
    name = "Harry"
    occupation = "Software dev"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
b=person()
c=person()
a.name = "Shubham"
a.occupation = "Accoutant"


b.name = "Nikita"
b.occupation = "HR"
# print(a.name,a.occupation)
a.info()
b.info()
c.info()
