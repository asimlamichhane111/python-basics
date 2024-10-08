class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
s1=Student('Ram',20)
s1.show()
s2=Student('Hari',18)
s2.show()
