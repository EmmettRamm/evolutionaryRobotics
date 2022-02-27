import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
import world as w
import robot as r

class SIMULATION:
    def __init__(self):
        #setting gravity
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravity)

        self.world = w.WORLD()
        self.robot = r.ROBOT()

    def run(self):
        for t in range(c.loop):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            
            time.sleep(c.sleepTime)
        
    def __del__(self):
        p.disconnect()