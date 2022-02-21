import pybullet as p
import pybullet_data
import constants as c
import numpy
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()


    def Prepare_To_Act(self):
        self.amplitude = c.bAmplitude
        self.frequency = c.bFrequency
        self.offset = c.bPhaseOffset
        self.bTargetAngles = self.amplitude * (numpy.sin(self.frequency * numpy.array(numpy.linspace(c.bottomAngleRange, c.topAngleRange, c.loop)) + self.offset))
        
    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = self.bTargetAngles[t],
        maxForce = c.bMaxForce)

    def Save_Values(self):
        numpy.save("data/motorValues.npy", self.bTargetAngles)