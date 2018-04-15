import serial

import easygui

import datetime


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


#Program vars
data = Queue()
port = '/dev/ttyUSB0'
ser = serial.Serial(port, 115200)
running = False
run = 1

#Test vars
flywheels = [69, 420, 1337]
testInfo = ["Bike", "Operator"]

while True:
	fieldValues = easygui.multenterbox("Please enter the following information about the test", "Dynosaur 1.0", testInfo)
	flywheel = easygui.choicebox("Please select the flywheel being used for the test. \nUnits are in kg * m²", "Dynosaur 1.0", flywheels)
	now = datetime.datetime.now()
	fieldValues[0] = fieldValues[0].replace(" ", "")
	fieldValues[1] = fieldValues[1].replace(" ", "")
	filename = fieldValues[0] + "_" + fieldValues[1] + "_" + str(now.month) + "_" + str(now.day) + "_" + str(now.year)
	path = easygui.diropenbox("Please select the directory to save the test data.", "Dynosaur 1.0", "~")
	print(filename)
	print(path)
	break
