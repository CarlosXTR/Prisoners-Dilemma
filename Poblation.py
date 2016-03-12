
import Person

class Poblation:
    
    People = []
    NumPeople = 0
    
    def __init__(self, N):
        self.NumPeople = N
        for i in self.NumPeople:
            p = Person(i,self.NumPeople)
            self.People.append(p)
            
    def Chooses(self):
        for i in self.NumPeople:
            self.People[i].MakeChoose()
            
            
            
