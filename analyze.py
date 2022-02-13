import numpy
import matplotlib.pyplot as pPlot

#backLegSensorValues = numpy.load("data/backLegSensorData.npy")
#frontLegSensorValues = numpy.load("data/frontLegSensorData.npy")
fSinVectorValues = numpy.load("data/fSinVectorData.npy")
bSinVectorValues = numpy.load("data/bSinVectorData.npy")
#print(backLegSensorValues)
#print(frontLegSensorValues)

#matplotlib.pyplot.plot(backLegSensorValues, label="backLeg", linewidth=4)
#matplotlib.pyplot.plot(frontLegSensorValues, label="frontLeg")
pPlot.plot(fSinVectorValues, label="Front Leg")
pPlot.plot(bSinVectorValues, label="Back Leg")
pPlot.legend()
pPlot.show()