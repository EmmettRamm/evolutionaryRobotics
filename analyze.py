import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load("data/backLegSensorData.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorData.npy")
print(backLegSensorValues)
print(frontLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues, label="backLeg", linewidth=4)
matplotlib.pyplot.plot(frontLegSensorValues, label="frontLeg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()