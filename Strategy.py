

import numpy as np

class Strategy:

    CONFESS = 0
    NOCONFESS = 1
    RANDOM = 2
    
    size = 3

    def __init__(self,*args, **kwargs):
        self.strategy = -1

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
        if(self.strategy == self.CONFESS):
            return 0
        elif (self.strategy == self.NOCONFESS):
            return 1
        elif (self.strategy == self.RANDOM):
            return np.random.randint(0,2)

if __name__ == "__main__":
    s = Strategy(2)
    print(Strategy.CONFESS)
    print(s)
    print(s.Size())
    print(s.NextStep())
    print(s.NextStep())