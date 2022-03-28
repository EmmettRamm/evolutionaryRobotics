import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import numpy
import random
import os
import constants as c
import sensor as s
import motor as m

class ROBOT:    
    def __init__(self, solutionID):
        self.ID = str(solutionID)
        brainFile = "brain" + self.ID + ".nndf"
        
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK(brainFile)
        #self.Delete_File()
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        
        self.fitnessFileName = "fitness" + self.ID + ".txt"

    def Delete_File(self):
        sysOut = "del brain" + self.ID + ".nndf"
        os.system(sysOut)

    def Prepare_To_Sense(self):
        self.sensors = dict()
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = s.SENSOR(linkName)

    def Sense(self, t):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(t)
    

    def Prepare_To_Act(self):
        self.motors = dict()
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = m.MOTOR(jointName)
        
    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        tempFitness = "tmp" + str(self.ID) + ".txt"
        outFile = open(tempFitness, "w")
        outFile.write(str(xCoordinateOfLinkZero))
        outFile.close()
        outCommand = "rename " + tempFitness + " " + self.fitnessFileName
        #print (outCommand)
        os.system(outCommand)
        

        #print ("\n", xCoordinateOfLinkZero)

        exit()