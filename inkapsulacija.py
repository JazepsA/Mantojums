class Pupil:
    _age=0 # protected
    __age=0 #private
    age=0 #public
    name="Jānis"
    def say(self):
        print(self.__age,self._age,self.age)

pupil=Pupil()
pupil.age=1 
pupil._age=-1
pupil.__age=-3
print(pupil.age)
print(pupil._age)
print(pupil.__age)
print(pupil.age, pupil._age,pupil.__age)  #izvada vienā rindā
#print(dir(pupil))
pupil.say()