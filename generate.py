from os import X_OK
import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = .5

for columns in range(5):
    for rows in range(5):
        for z in range(10):
            scale = z/10
            pyrosim.Send_Cube(name="Box", pos=[columns,rows,z + .5] , size=[1-scale,1-scale,1-scale])


pyrosim.End()