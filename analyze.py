import numpy
import matplotlib.pyplot as pPlot

backLegSensorValues = numpy.load("data/backLegSensorData.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorData.npy")
sinVectorValues = numpy.load("data/sinvectordata.npy")
print(backLegSensorValues)
print(frontLegSensorValues)

#matplotlib.pyplot.plot(backLegSensorValues, label="backLeg", linewidth=4)
#matplotlib.pyplot.plot(frontLegSensorValues, label="frontLeg")
pPlot.plot(sinVectorValues, label="Sin Vector")
pPlot.legend()
pPlot.show()