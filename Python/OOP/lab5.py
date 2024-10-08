from multipledispatch import * 
class Student:
    @dispatch()
    def __init__(self):
        self.name='Ram'
        self.age=20
    @dispatch(str,int)
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
s1=Student()
s1.show()
s2=Student("Hari",20)
s2.show()
