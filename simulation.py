import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random

#setting gravity
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

#loading in the floor plane, the robot, and the world
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

#simplifying pi
pi = numpy.pi

#initializing the loop length
loop = 1000

targetAngles = numpy.sin(numpy.array(numpy.linspace(0, 2*pi, loop))) * pi/4

numpy.save("data/sinvectordata.npy", targetAngles)
exit()

#setting up sensors
backLegSensorValues = numpy.zeros(loop)
frontLegSensorValues = numpy.zeros(loop)
print(backLegSensorValues)
print(frontLegSensorValues)

#preping to simulate the robot
pyrosim.Prepare_To_Simulate(robotId)

#loop for simulation
for i in range(loop):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = "Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = random.uniform(-pi/2.0, pi/2.0),
    maxForce = 50)

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = "Torso_FrontLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = random.uniform(-pi/2.0, pi/2.0),
    maxForce = 50)

    time.sleep(1/30)
    
numpy.save("data/backLegSensorData.npy", backLegSensorValues)
numpy.save("data/frontLegSensorData.npy", frontLegSensorValues)
p.disconnect()
print(backLegSensorValues)
print(frontLegSensorValues)