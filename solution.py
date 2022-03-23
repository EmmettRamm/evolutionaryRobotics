import numpy
import time
import pyrosim.pyrosim as pyrosim
import os
import random

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(3,2)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID

    def Evaluate(self, directOrGUI):
        pass
        #self.Create_World()
        #self.Create_Body()
        #self.Create_Brain()

        #systemPythonCommand = "start /B python simulate.py " + directOrGUI + " " + str(self.myID)
        #print (systemPythonCommand)
        #os.system(systemPythonCommand)

        #openFile = "fitness" + str(self.myID) + ".txt"

        #while not os.path.exists(openFile):
        #    time.sleep(0.01)

        #fitnessFile = open(openFile, "r")
        #self.fitness = float(fitnessFile.read())
        #print (self.fitness)
        #fitnessFile.close()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        systemPythonCommand = "start /B python simulate.py " + directOrGUI + " " + str(self.myID)
        #print (systemPythonCommand)
        os.system(systemPythonCommand)

    def Wait_For_Simulation_To_End(self):
        openFile = "fitness" + str(self.myID) + ".txt"

        while not os.path.exists(openFile):
            time.sleep(0.01)

        fitnessFile = open(openFile, "r")
        self.fitness = float(fitnessFile.read())
        #print (self.fitness)
        fitnessFile.close()

        os.system("del " + openFile)


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        #length = 1
        #width = 1
        #height = 1

        #x = 3
        #y = 3
        #z = .5

        #pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0,1.5,1.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,2,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,-0.5], size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,1,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,-0.5], size=[1,1,1])

        pyrosim.End()

    def Create_Brain(self):
        sendFile = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(sendFile)
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName= currentRow, targetNeuronName= currentColumn + 3, weight= self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow, randomColumn] = (2 * numpy.random.rand()) - 1

    def Set_ID(self, newID):
        self.myID = newID