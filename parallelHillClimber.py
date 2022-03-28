from solution import SOLUTION
import copy
import constants as c
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        #self.parent = SOLUTION()
        self.nextAvailableID = 0
        self.parents = {}
        
        for parent in range(0, c.populationSize):
            self.parents[parent] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Evaluate(self, solutions):
        for parent in range(0, len(solutions)):
            solutions[parent].Start_Simulation("DIRECT")

        for parent in range(0, len(solutions)):
            solutions[parent].Wait_For_Simulation_To_End()

    def Evolve(self):
        
        #self.parent.Evaluate("GUI")
        #print (len(self.parents))
        #print (self.parents)
        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        #self.child = copy.deepcopy(parent)
        #self.child.setID(self.nextAvailableID)
        #self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        for key in self.parents:
            if (self.parents[key].fitness > self.children[key].fitness):
                self.parents[key] = self.children[key]


    def Show_Best(self):
        #os.system("python simulate.py GUI")
        bestFitness = self.parents[0].fitness
        bestFitKey = 0
        for key in self.parents:
            if (self.parents[key].fitness < bestFitness):
                bestFitness = self.parents[key].fitness
                bestFitKey = key
        self.parents[bestFitKey].Start_Simulation("GUI")

    def Print(self):
        for key in self.parents:
            #outString = "\nFitness of parent: " + str(self.parents[key].fitness) + ". Fitness of child: " + str(self.children[key].fitness) + ".\n"
            print ("\nParent fitness: " + str(self.parents[key].fitness) + ". Child fitness: " + str(self.children[key].fitness) + ".\n")