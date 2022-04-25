import numpy
import time
import pyrosim.pyrosim as pyrosim
import os
import random
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        systemPythonCommand = "start /B python simulate.py " + directOrGUI + " " + str(self.myID)
        os.system(systemPythonCommand)

    def Wait_For_Simulation_To_End(self):
        openFile = "fitness" + str(self.myID) + ".txt"
        print (openFile)

        while not os.path.exists(openFile):
            time.sleep(0.01)

        fitnessFile = open(openFile, "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()

        delString = "del " + openFile

        os.system(delString)


    def Create_World(self):
        pyrosim.Start_SDF("sdf/world.sdf")

        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("urdf/body.urdf")

        #Torso
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,1,1])

        #frontleg
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [.2,.5,1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0], size=[.2,1,.2])

        #front lower leg
        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5], size=[.2,.2,1])

        #Back leg
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [.2,-.5,1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0], size=[.2,1,.2])

        #Back lower leg
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5], size=[.2,.2,1])

        #Front left leg
        pyrosim.Send_Joint( name = "Torso_FrontLeftLeg" , parent= "Torso" , child = "FrontLeftLeg" , type = "revolute", position = [-0.5,.5,1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="FrontLeftLeg", pos=[0,0.5,0], size=[.2,1,.2])

        #Front left lower leg
        pyrosim.Send_Joint( name = "FrontLeftLeg_FrontLeftLowerLeg" , parent= "FrontLeftLeg" , child = "FrontLeftLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeftLowerLeg", pos=[0,0,-0.5], size=[.2,.2,1])

        #Front right leg
        pyrosim.Send_Joint( name = "Torso_FrontRightLeg" , parent= "Torso" , child = "FrontRightLeg" , type = "revolute", position = [-0.5,-0.5,1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="FrontRightLeg", pos=[0,-0.5,0], size=[.2,1,.2])

        #Front right lower leg
        pyrosim.Send_Joint( name = "FrontRightLeg_FrontRightLowerLeg" , parent= "FrontRightLeg" , child = "FrontRightLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontRightLowerLeg", pos=[0,0,-0.5], size=[.2,.2,1])

        #Back left leg
        pyrosim.Send_Joint( name = "Torso_BackLeftLeg" , parent= "Torso" , child = "BackLeftLeg" , type = "revolute", position = [.5,.5,1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="BackLeftLeg", pos=[0,0.5,0], size=[.2,1,.2])

        #Back Left Lower Leg
        pyrosim.Send_Joint( name = "BackLeftLeg_BackLeftLowerLeg" , parent= "BackLeftLeg" , child = "BackLeftLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeftLowerLeg", pos=[0,0,-0.5], size=[.2,.2,1])

        #Back right leg
        pyrosim.Send_Joint( name = "Torso_BackRightLeg" , parent= "Torso" , child = "BackRightLeg" , type = "revolute", position = [.5,-0.5,1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="BackRightLeg", pos=[0,-0.5,0], size=[.2,1,.2])

        #Back right lower leg
        pyrosim.Send_Joint( name = "BackRightLeg_BackRightLowerLeg" , parent= "BackRightLeg" , child = "BackRightLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackRightLowerLeg", pos=[0,0,-0.5], size=[.2,.2,1])

        #Back middle right leg
        pyrosim.Send_Joint( name = "Torso_BackMiddleRightLeg" , parent= "Torso" , child = "BackMiddleRightLeg" , type = "revolute", position = [-.2,-0.5,1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="BackMiddleRightLeg", pos=[0,-0.5,0], size=[.2,1,.2])

        #Back middle right lower leg
        pyrosim.Send_Joint( name = "BackMiddleRightLeg_BackMiddleRightLowerLeg" , parent= "BackMiddleRightLeg" , child = "BackMiddleRightLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackMiddleRightLowerLeg", pos=[0,0,-0.5], size=[.2,.2,1])

        #Front middle right leg
        pyrosim.Send_Joint( name = "Torso_FrontMiddleRightLeg" , parent= "Torso" , child = "FrontMiddleRightLeg" , type = "revolute", position = [-.2,0.5,1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="FrontMiddleRightLeg", pos=[0,.5,0], size=[.2,1,.2])

        #Front middle right lower leg
        pyrosim.Send_Joint( name = "FrontMiddleRightLeg_FrontMiddleRightLowerLeg" , parent= "FrontMiddleRightLeg" , child = "FrontMiddleRightLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontMiddleRightLowerLeg", pos=[0,0,-.5], size=[.2,.2,1])

        pyrosim.End()

    def Create_Brain(self):
        sendFile = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(sendFile)
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "FrontLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "BackLeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "BackLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "BackRightLeg")
        pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "BackRightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 11 , linkName = "FrontRightLeg")
        pyrosim.Send_Sensor_Neuron(name = 12 , linkName = "FrontRightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 13 , linkName = "BackMiddleRightLeg")
        pyrosim.Send_Sensor_Neuron(name = 14 , linkName = "BackMiddleRightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 15 , linkName = "FrontMiddleRightLeg")
        pyrosim.Send_Sensor_Neuron(name = 16 , linkName = "FrontMiddleRightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 17 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 18 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 19 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 20 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 21 , jointName = "Torso_FrontLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 22 , jointName = "FrontLeftLeg_FrontLeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 23 , jointName = "Torso_BackRightLeg")
        pyrosim.Send_Motor_Neuron( name = 24 , jointName = "BackRightLeg_BackRightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 25 , jointName = "Torso_BackLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 26 , jointName = "BackLeftLeg_BackLeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 27 , jointName = "Torso_FrontRightLeg")
        pyrosim.Send_Motor_Neuron( name = 28 , jointName = "FrontRightLeg_FrontRightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 29 , jointName = "Torso_BackMiddleRightLeg")
        pyrosim.Send_Motor_Neuron( name = 30 , jointName = "BackMiddleRightLeg_BackMiddleRightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 31 , jointName = "Torso_FrontMiddleRightLeg")
        pyrosim.Send_Motor_Neuron( name = 32 , jointName = "FrontMiddleRightLeg_FrontMiddleRightLowerLeg")


        
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName= currentRow, targetNeuronName= currentColumn + c.numSensorNeurons, weight= self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = (2 * numpy.random.rand()) - 1

    def Set_ID(self, newID):
        self.myID = newID