# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:32:01 2016

@author: Carlos
"""

import Person

class Poblation:
    
    People = []
    NumPeople = 0
    
    def __init__(self, N):
        NumPeoble = N
        for i in NumPeoble:
            p = Person(i,NumPeoble)
            People.append(p)
            
    def Chooses(self):
        for i in NumPeople:
            People[i].MakeChoose()
            
            
            
