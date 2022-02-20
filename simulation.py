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

        #preping to simulate the robot
        

    def run(self):
        for t in range(c.loop):
            p.stepSimulation()
            self.robot.Sense(t)
            
            #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            #frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

            #pyrosim.Set_Motor_For_Joint(
            #bodyIndex = robot.robotId,
            #jointName = "Torso_BackLeg",
            #controlMode = p.POSITION_CONTROL,
            #targetPosition = bTargetAngles[i],
            #maxForce = c.bMaxForce)

            #pyrosim.Set_Motor_For_Joint(
            #bodyIndex = robot.robotId,
            #jointName = "Torso_FrontLeg",
            #controlMode = p.POSITION_CONTROL,
            #targetPosition = fTargetAngles[i],
            #maxForce = c.fMaxForce)

            time.sleep(c.sleepTime)
        
    def __del__(self):
        p.disconnect()

    
