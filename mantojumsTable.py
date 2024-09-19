class Table:
    def __init__(self,l,w,h):
        self.lenght=l
        self.width=w
        self.height=h
        if isinstance(self,Kichentable):
            p=int(input("Cik vietu: "))
            self.places=p
            print(f"Vietu skaits: {self.places}")
    def izvadaInfo(self):
        print(f"Garums: {self.lenght},Platums: {self.width},Augstums: {self.height} ")
    


class Desktable(Table):
    def square(self):
        return self.width * self.lenght

class Computertable(Desktable):
    def square(self,monitor=0.0):
        return self.width * self.lenght - monitor
''' 
#1  (t4)
class Kichentable(Table):
    def __init__(self,l,w,h,p):
        Table.__init__(self,l,w,h)
        self.places=p
        print(f"Vietas : {self.places}")

#2 (t4)
class Kichentable(Table):
    def __init__(self,l,w,h,p):
        super().__init__(l,w,h)
        self.places=p
        print(f"Vietas : {self.places}")
'''
class Kichentable(Table):
    pass


t1=Table(1.5,1.8,0.75)
t1.izvadaInfo()
t2=Desktable(0.6,0.6,0.7)
print(t2.square())
t2.izvadaInfo()
t3=Computertable(0.6,0.6,0.7)
print(t3.square(0.3))
t4=Kichentable(1.5,2,0.75,)
t4.izvadaInfo()