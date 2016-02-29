

class Person:
    
    MyChoose = {}
    Name = 0
    NumberCompanion = 0
    Punish = 0
    Strategy = null
    
    def __init__(self,name, ncompanion):
        self.Name = name
        self.NumberCompanion = ncompanion

    def getName(self):
        return self.Name        
    
    def getChoose(self, index):
        return self.MyChoose[str(index)]
        
    def setChoose(self, index, value):
        self.MyChoose[str(index)] = value
                    
    def getNumberCompanion(self):
        return self.NumberCompanion
        
    def MakeChoose(self):
        for i in range(self.NumberCompanion):
            if (i != self.Name):
                self.setChoose(i,'Lie')
                
                
if __name__ == "__main__":
    p = Person(1,20)
    p.MakeChoose()

    for i in range(p.getNumberCompanion()):
        if (i != p.getName()):
            print p.getChoose(i)