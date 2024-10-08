class Student:
    def set(self,name,age,faculty):
        self.name=name
        self.age=age
        self.faculty=faculty
    def show(self):
        print(self.name,self.age,self.faculty)
std1=Student()
std1.set('Ram',20,'BIM')
std1.show()
std2=Student()
std2.set('Hari',18,'BHM')
std2.show()
