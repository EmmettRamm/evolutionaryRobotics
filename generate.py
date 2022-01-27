from os import X_OK
import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    length = 1
    width = 1
    height = 1

    x = 0
    y = 0
    z = .5

    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[1,1,.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Torso_Leg" , parent= "Torso" , child = "Leg" , type = "revolute", position = [.5,0,1])
    pyrosim.Send_Cube(name="Leg", pos=[1.0,0,1.5], size=[1,1,1])

    pyrosim.End()

Create_Robot()

Create_World()
