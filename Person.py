from Strategy import Strategy


class Person:

    def __init__(self, *args, **kwargs):
        self.MyChoose = {}
        self.Id = args[0]
        self.NumberCompanion = args[1]
        self.Punish = 0
        self.strategy = 0

        if (len(args) == 2):
            self.initDefault()
        elif (len(args) == 3):
            self.initStrategy(args[2])

    def initDefault(self):
        for i in range(self.NumberCompanion):
            if (i != self.Id):
                st = Strategy()
                self.MyChoose[i] = [st, []]

    def initStrategy(self, s):
        for i in  range(self.NumberCompanion):
            if (i != self.Id):
                self.MyChoose[i] = [Strategy(s), []]

    def getId(self):
        return self.Id

    def getStrategy(self):
        return self.strategy

    def getChoose(self, index):
        return self.MyChoose[str(index)]

    def setChoose(self, index, value):
        self.MyChoose[str(index)] = value

    def getNumberCompanion(self):
        return self.NumberCompanion

    def getElections(self,n):
        return self.MyChoose[n][1][:]

    def getPunish(self):
        return self.Punish

    def setPunish(self,punish):
        self.Punish = punish

    def MakeChoose(self):
        for i in range(self.NumberCompanion):
            if(i in self.MyChoose):
                choose = self.MyChoose[i][0].NextStep()
                self.MyChoose[i][1].append(choose)

#    def MakeChoose(self,companion):
#        if(companion in self.MyChoose):
#            choose = self.MyChoose[companion][0].NextStep()
#            self.MyChoose[companion][1].append(choose)

if __name__ == "__main__":
    numpersonp = 20
    numpersonp1 = 5

    p = Person(2, numpersonp,Strategy.RANDOM)
    p2 = Person(1, numpersonp1)

    p.MakeChoose()
    p.MakeChoose()

    for i in range(numpersonp):
        if(i != p.getId()):
            print(str(i) + "->"+str(p.getElections(i)))
    for i in range(numpersonp1):
        if (i != p2.getId()):
            print(str(i) + "->" + str(p2.getElections(i)))