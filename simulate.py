import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random
import sys
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
from simulation import SIMULATION

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.run()
simulation.Get_Fitness()