import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

loop = 1000

backLegSensorValues = numpy.zeros(loop)
frontLegSensorValues = numpy.zeros(loop)
print(backLegSensorValues)
print(frontLegSensorValues)
pyrosim.Prepare_To_Simulate(robotId)
for i in range(loop):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/30)
    
numpy.save("data/backLegSensorData.npy", backLegSensorValues)
numpy.save("data/frontLegSensorData.npy", frontLegSensorValues)
p.disconnect()
print(backLegSensorValues)
print(frontLegSensorValues)