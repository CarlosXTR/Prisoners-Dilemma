
import Person

class Poblation:
    
    People = []
    NumPeople = 0
    
    def __init__(self, N):
        NumPeoble = N
        for i in NumPeoble:
            p = Person(i,NumPeoble)
            self.People.append(p)
            
    def Chooses(self):
        for i in self.NumPeople:
            self.People[i].MakeChoose()
            
            
            
