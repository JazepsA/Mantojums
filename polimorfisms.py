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
