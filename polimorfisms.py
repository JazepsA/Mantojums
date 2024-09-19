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