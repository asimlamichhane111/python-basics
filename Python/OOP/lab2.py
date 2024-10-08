class Student:
    def set(self,name,age,faculty):
        self.name=name
        self.age=age
        self.faculty=faculty
    def show(self):
        print(self.name,self.age,self.faculty)
std1=Student()
std1.set('Ram',20,'BIM')
std2=Student()
std2.set('Hari',17,'BHM')
std3=Student()
std3.set('Sita',18,'BBA-F')
std4=Student()
std4.set('Laxman',19,'BIM')
std5=Student()
std5.set('Hanuman',20,'BIM')
students=[std1,std2,std3,std4,std5]
for s in students:
    if s.faculty=='BIM':
        s.show()
