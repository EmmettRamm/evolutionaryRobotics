import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load("data/backLegSensorData.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorData.npy")
print(backLegSensorValues)
print(frontLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.show()