from solution import SOLUTION
import copy
import constants as c
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        #self.parent = SOLUTION()
        self.parents = {}
        for parent in range(0, c.populationSize):
            self.parents[parent] = SOLUTION()

    def Evolve(self):
        #self.parent.Evaluate("GUI")
        print (len(self.parents))
        print (self.parents)
        for parent in range(0, len(self.parents)):
            self.parents[parent].Evaluate("GUI")

        #for currentGeneration in range(c.numberOfGenerations):
        #    self.Evolve_For_One_Generation()
        pass

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if (self.parent.fitness > self.child.fitness):
            self.parent = self.child


    def Show_Best(self):
        #os.system("python simulate.py GUI")
        pass