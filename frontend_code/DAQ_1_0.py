import serial
import csv
import easygui
import datetime
import matplotlib.pyplot as plt


class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

X = [590,540,740,130,810,300,320,230,470,620,770,250]
Y = [32,36,39,52,61,72,77,75,68,57,48,48]

plt.scatter(X, Y)

#Program vars
data = Queue()
port = '/dev/ttyUSB0'
#ser = serial.Serial(port, 115200)
running = False
run = 1

#Test vars
flywheels = [69, 420, 1337]
testInfo = ["Bike", "Operator"]

while True:
	fieldValues = easygui.multenterbox("Please enter the following information about the test", "Dynosaur 1.0", testInfo)
	flywheel = easygui.choicebox("Please select the flywheel being used for the test. \nUnits are in kg * m²", "Dynosaur 1.0", flywheels)
	now = datetime.datetime.now()
	filename = fieldValues[0].replace(" ", "") + "_" + fieldValues[1].replace(" ", "") + "_" + str(now.month) + "_" + str(now.day) + "_" + str(now.year)
	path = easygui.diropenbox("Please select the directory to save the test data.", "Dynosaur 1.0", "~")
	print(filename)
	print(path)
	break

plt.title(fieldValues[0] + " Torque Curve")
plt.xlabel("Angular Velocity (RPM)")
plt.ylabel("Torque N*M")
plt.show()
