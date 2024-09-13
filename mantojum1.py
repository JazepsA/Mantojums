'''
class Person:#MAINCLASS
    def cant_breath(self):
        print("Es neprotu elpot")
    def can_walk(self):
        print("Es protu staigāt! ")

class Doctor(Person):#SUBCLASS
    def can_cure(self):
        print("Es protu ārstēt! ")


    
class Architect(Person):#SUBCLASS
    def can_build(self):
        print("Es protu celt! ")


d=Doctor()
#d.can_cure()
#d.can_walk()
a=Architect()
#a.can_build()
#a.can_walk()
print(issubclass(Doctor,Person))
print(issubclass(Person,Doctor))
'''
class Transportlidzeklis:
    def __init__(self,marka,modelis,maxspeed):
       self.marka=marka
       self.modelis=modelis
       self.maxspeed=maxspeed
  
    def paradis_info(self):
        print(f"Transportlidzekļa modelis {self.modelis},marka {self.marka} ,maksimalais atrums {self.maxspeed}")

class Automasina(Transportlidzeklis):
    def __init__(self,marka,modelis,maxspeed,degviela):
        super().__init__(marka,modelis,maxspeed)
        self.degviela=degviela
    def paradis_info(self):
        super().paradis_info()
        print(f"Degvielas tips: {self.degviela}")
class Motocikls(Transportlidzeklis):
    def __init__(self,marka,modelis,maxspeed,krasa):
        super().__init__(marka,modelis,maxspeed)
        self.krasa=krasa
    def paradis_info_moto(self):
        super().paradis_info()
        print(f"Motocikla krasa: {self.krasa}")

    

a=Automasina("audi","quattro","250km/h","Eļļa")
a.paradis_info()
b=Motocikls("Kawasaki","divriteņu","300km/h","Sarkana")
b.paradis_info_moto()
    