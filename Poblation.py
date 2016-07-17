
from Person import Person
from Strategy import Strategy
import numpy as np
import matplotlib.pyplot as plt

class Poblation:

#    def __init__(self, N):
#        self.NumPeople = N
#        for i in range(self.NumPeople):
#            p = Person(i,self.NumPeople)
#            self.People.append(p)

    def __init__(self, *args, **kwargs):
        self.People = []
        self.NumPeople = 0
        self.Iteration = 0

        if (len(args) == 1):
            self.initNpersonRandom(args[0])

    def initNpersonRandom(self,N):
        self.NumPeople = N

        for i in range(self.NumPeople):
            p = Person(i, self.NumPeople)
            self.People.append(p)

    def appendPerson(self, person):
        self.People.append(person)
        self.NumPeople += 1
            
    def Chooses(self):
        for person in self.People:
            person.MakeChoose()
        self.Iteration+=1
            
    def printDecision(self):
        for person in self.People:
            print(person.getId())
            for i in range(self.NumPeople):
                if (i != person.getId()):
                    print(str(i)+"->"+str(person.getElections(i)))

    def getNumPeople(self):
        return self.NumPeople

    def getPeople(self):
        return self.People

    def Calallpunish(self):
        numMovimientos = (self.NumPeople -1) * self.Iteration

        for person in self.People:
            castigo = 0
            for other in self.People:
                if(person.getId() != other.getId()):
                    for i in other.getElections(person.getId()):
                        castigo += i

            punish = 1 + (castigo/numMovimientos) * (2 * self.NumPeople -3)
            person.setPunish(punish)
            print(str(person.getId()) + "-->"+ str(punish))


    def Calpunish4step(self):
        numMovimientos = (self.NumPeople - 1)

        for person in self.People:
            castigo = 0
            for other in self.People:
                if (person.getId() != other.getId()):
                    castigo += other.getElections(person.getId())[-1]

            punish = 1 + (castigo / numMovimientos) * (2 * self.NumPeople - 3)
            #print("1 + " + str(castigo) + "/" + str(numMovimientos) + " * (2*" + str(self.NumPeople) + "-3)")
            person.setPunish(punish)
            #print(str(person.getId()) + "-->" + str(punish))

    def Calallpunish4step(self,Numiterate):
        allpunish = []
        for i in range(Numiterate):
            punishperpeople = []
            self.Chooses()
            self.Calpunish4step()
            for p in self.getPeople():
                punishperpeople.append(p.getPunish())
            allpunish.append(punishperpeople)

        return allpunish

if __name__ == "__main__":

    ##POBLATION 2

    allpunish = []
    numiterartion = 10
    numperson = 6

    poblation = Poblation()
    p1 = Person(0, numperson, Strategy.CONFESS)
    p2 = Person(1, numperson, Strategy.RANDOM)
    p3 = Person(2, numperson, Strategy.RANDOM)
    p4 = Person(3, numperson, Strategy.CONFESS)
    p5 = Person(4, numperson, Strategy.RANDOM)
    p6 = Person(5, numperson, Strategy.NOCONFESS)
    poblation.appendPerson(p1)
    poblation.appendPerson(p2)
    poblation.appendPerson(p3)
    poblation.appendPerson(p4)
    poblation.appendPerson(p5)
    poblation.appendPerson(p6)

    allpunish = poblation.Calallpunish4step(numiterartion)

    poblation.Calallpunish()
    allpunish = np.array(allpunish)

    for n in range(numperson):
        name = "Person " + str(n)
        plt.plot(allpunish[:, n], label = name)
    plt.legend()
    plt.show()


    #numperson = 5
    #numiterartion = 10
    #allpunish = []

    #poblacion = Poblation(numperson)

    #for i in range(numiterartion):
    #    punishperpeople = []
    #    poblacion.Chooses()
    #    poblacion.Calpunish4step()
    #    for p in poblacion.getPeople():
    #        punishperpeople.append(p.getPunish())
    #    allpunish.append(punishperpeople)

    #poblacion.Calpunish()
    #allpunish = np.array(allpunish)

    #for n in range(numperson):
    #    name = "Person "+str(n)
        #print("Person "+str(n))
        #print(allpunish[:,n])
    #    plt.plot(allpunish[:,n])
    #plt.show()