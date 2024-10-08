'''
class Pupil:
    __age=0 #private
    #setter piekļuve datiem
    def set_age(self,value:int):
        if value >=0:
            self.__age=value
        else:
            print("Vecums nevar būt negatīvs.")
        #getter vērtības piešķiršana
    def get_age(self):
        return self.__age
pupil=Pupil()
pupil.set_age(-1)
pupil.set_age(10)

#pupil.__age=-1
print(pupil.get_age())
#pupil.set_age()
'''
#1
'''
class Animal: 
    legs=4
    tail=1
    def voice(self):
        return

class Cat(Animal):
    print("Mjauu!")
class Dog(Animal):
    print("Awawgav!")
class Wolf(Animal):
     print("Auuuuuuuuuu!")


a=Animal()
a.voice()
'''
#2
'''
class Animal: 
    legs=4
    tail=1
    def voice(self):
        print("Kaut-kāda skaņa")

class Cat(Animal):
    def cat_voice(self):
        print("Mjau")
class Dog(Animal):
    def dog_voice(self):
        print("Gav")
class Wolf(Animal):
    def wolf_voice(self):
        print("Auuuuf")

animal=Animal()
animal.voice()
cat1,cat2=Cat(),Cat()
dog1,dog2=Dog(),Dog()
wolf1,wolf2=Wolf(),Wolf()

farm_band=[cat1,cat2,dog1,dog2,wolf1,wolf2]
for i in farm_band:
    if isinstance(i,Cat):
        i.cat_voice()
    if isinstance(i,Dog):
        i.dog_voice()
    if isinstance(i,Wolf):
        i.wolf_voice()
'''
#3
'''
class Animal: 
    legs=4
    tail=1
    def voice(self):
        print("Kaut-kāda skaņa")

class Cat():
    def voice(self):
        print("Mjau")
class Dog():
    def voice(self):
        print("Gav")
class Wolf():
    def voice(self):
        print("Auuuuf")

animal=Animal()
animal.voice()
cat1,cat2=Cat(),Cat()
dog1,dog2=Dog(),Dog()
wolf1,wolf2=Wolf(),Wolf()

farm_band=[cat1,cat2,dog1,dog2,wolf1,wolf2]
for i in farm_band:
    i.voice()
'''
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius


    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

# viena izvades metode
C1=Circle(1.5)

print(C1.area())
print(C1.perimeter())

#Geometrisko figuru sarkaksts
shapes=[Rectangle(3,4),Circle(5)]

for shape in shapes:
    print(f"Area : {shape.area():.2f},Perimeter:{shape.perimeter():.2f}")


    


