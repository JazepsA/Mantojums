
class Person: 
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Person created ")
    
    def say_hello(self):
        print(f"{self.name} says Hello! ")

class Student(Person):
    def __init__(self,name,age,average_grade):
        #Person.__init__(self,name,age)
        super().__init__(name,age)
        self.average_grade=average_grade
        print("Student created")
    def study(self):
        print(f"{self.name} studies ")
    def say_hello(self):
        print(f"Student with name: {self.name} says Hello! ")

class Teacher(Person):
     def teach(self):
        print(f"{self.name} teaches ")
    
def introduce(person):
    print("Now, a person will say hello")
    person.say_hello()

people_arr=[Student("Tom",15,4.5),Teacher("Emily",21),Student("Dainis",26,4.2)]

for person in people_arr:
    introduce(person)
'''
p1=Student("Tom",15,4.5)
t1=Teacher("Emily",21)
p1.say_hello()
t1.say_hello()
p1.study()
t1.teach()
'''