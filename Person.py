from Strategy import Strategy


class Person:
    MyChoose = {}
    Id = 0
    NumberCompanion = 0
    Punish = 0
    strategy = 0

    def __init__(self, *args, **kwargs):
        if (len(args) == 2):
            self.initDefault(args[0], args[1])
        elif (len(args) == 3):
            self.initStrategy(args[0], args[1], args[2])

    def initDefault(self, Id, ncompanion):
        self.Id = Id
        self.NumberCompanion = ncompanion
        for i in range(ncompanion):
            if (i != Id):
                st = Strategy()
                self.MyChoose[i] = [st, []]

    def initStrategy(self, Id, ncompanion, s):
        self.Id = Id
        self.NumberCompanion = ncompanion
        for i, strategy in zip(range(ncompanion), s):
            if (i != Id):
                self.MyChoose[i] = [Strategy(strategy), []]

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

    def getElection(self,n):
        return self.MyChoose[n][1][:]

    def MakeChoose(self):
        for i in range(self.NumberCompanion):
            if ( i in self.MyChoose):
                choose = self.MyChoose[i][0].NextStep()
                self.MyChoose[i][1].append(choose)


if __name__ == "__main__":
    p = Person(1, 20)
    p.MakeChoose()
    p.MakeChoose()
    print(p.getElection(2))
