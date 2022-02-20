import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
simulation.run()

#bTargetAngles = c.bAmplitude * (numpy.sin(c.bFrequency * numpy.array(numpy.linspace(c.bottomAngleRange, c.topAngleRange, c.loop)) + c.bPhaseOffset))
#fTargetAngles = c.fAmplitude * (numpy.sin(c.fFrequency * numpy.array(numpy.linspace(c.bottomAngleRange, c.topAngleRange, c.loop)) + c.fPhaseOffset))
#numpy.save("data/bSinVectorData.npy", bTargetAngles)
#numpy.save("data/fSinVectorData.npy", fTargetAngles)

#setting up sensors
#backLegSensorValues = numpy.zeros(c.loop)
#frontLegSensorValues = numpy.zeros(c.loop)
#print(backLegSensorValues)
#print(frontLegSensorValues)



#loop for simulation
#for i in range(c.loop):
    #p.stepSimulation()
    #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    #frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    #pyrosim.Set_Motor_For_Joint(
    #bodyIndex = robotId,
    #jointName = "Torso_BackLeg",
    #controlMode = p.POSITION_CONTROL,
    #targetPosition = bTargetAngles[i],
    #maxForce = c.bMaxForce)

    #pyrosim.Set_Motor_For_Joint(
    #bodyIndex = robotId,
    #jointName = "Torso_FrontLeg",
    #controlMode = p.POSITION_CONTROL,
    #targetPosition = fTargetAngles[i],
    #maxForce = c.fMaxForce)

    #time.sleep(c.sleepTime)
    
#numpy.save("data/backLegSensorData.npy", backLegSensorValues)
#numpy.save("data/frontLegSensorData.npy", frontLegSensorValues)
#p.disconnect()
#print(backLegSensorValues)
#print(frontLegSensorValues)