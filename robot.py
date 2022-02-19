import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c

class ROBOT:
    def Prepare_To_Sense():
        self.sensors = dict()
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)
    
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        self.motors = dict()
        pyrosim.Prepare_To_Simulate(self.robotId)
        Prepare_To_Sense()