import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        self.worldId = p.loadSDF("world.sdf")