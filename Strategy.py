

import numpy as np

class Strategy():
    
    Confess = 0
    NoConfess = 1
    Random = 2
    
    size = 3
    
    strategy = -1

    def __init__(self):
        self.strategy =  np.random.randint(0,self.size)
        
    def __init__(self,strategy):        
        self.strategy = strategy        
        
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
    s = Strategy(0)
    print(s.Size())
    print(s.NextStep())