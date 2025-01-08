class person:

    def __init__(self,n,o):
        print("Hey i am a person")
        self.name = n
        self.ocu = o
    def info(self):
        print(f"{self.name} is a {self.ocu}")

a=person("Harry","Dev")
b=person("Divya","HR")
# a.name="Divya"
# a.ocu="HR"
# print(a.name)
a.info()
b.info()