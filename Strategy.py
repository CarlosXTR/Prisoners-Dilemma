

import numpy as np

class Strategy:
    
    Confess = 0
    NoConfess = 1
    Random = 2
    
    size = 3
    
    strategy = -1

    def __init__(self,*args, **kwargs):
        if(len(args) == 0):
            self.initDefault()
        elif(len(args) == 1):
            self.initStrategy(args[0])
        
    def initDefault(self):
        self.strategy = np.random.randint(0,self.size)

    def initStrategy(self, s):
        if( s < self.size):        
            self.strategy = s
        else:
            print("Error init")

    def setStrategy(self,s):
        if(s < self.size):
            self.strategy = s
        else:
            return -1
            
    def getStrategy(self):
        return self.strategy
    
    def Size(self):
        return self.size

    def NextStep(self):
        if(self.strategy == self.Confess):
            return 0
        elif (self.strategy == self.NoConfess):
            return 1
        elif (self.strategy == self.Random):
            return np.random.randint(0,2)

if __name__ == "__main__":
    s = Strategy(2)
    print(s)
    print(s.Size())
    print(s.NextStep())
    print(s.NextStep())