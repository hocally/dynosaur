import serial
import csv
import easygui
import datetime
import matplotlib.pyplot as plt
import time

velocity = []
acceleration = []

# Program vars
title = "Dynosaur 1.0"
port = '/dev/ttyUSB0'
ser = serial.Serial(port, 115200)
logo = "logo.gif"
testState = 0
testRun = 0

# Test vars
fieldValues = []
flywheels = [69, 420, 1337]
testInfo = ["Bike", "Operator", "Terminal speed"]
testChoices = ["Quit", "Enter test parameters", "Calibration mode"]
testSwitch = {testChoices[0]: -1, testChoices[1]: 1, testChoices[2]: 3}
runChoices = ["Go to start", "Test same bike", "Test new bike", "Quit"]
runSwitch = {runChoices[0]: 0, runChoices[1]: 2, runChoices[2]: 1, runChoices[3]: -1}


while True:
	if testState == 0:
		reply = easygui.buttonbox("Please select the desired option.", title, choices=testChoices)
		if reply == logo:
			testState = 0
			continue
		testState = testSwitch[reply]

	elif testState == 1:
		fieldValues = easygui.multenterbox("Please enter the following information about the test", title, testInfo)
		flywheel = easygui.choicebox("Please select the flywheel being used for the test. \nUnits are in kg * m²",
									 "Dynosaur 1.0", flywheels)
		now = datetime.datetime.now()
		filename = fieldValues[0].replace(" ", "") + "_" + fieldValues[1].replace(" ", "") + "_" + str(
			now.month) + "_" + str(now.day) + "_" + str(now.year) + "_" + str(testRun)
		path = easygui.diropenbox("Please select the directory to save the test data.", title, "~")
		testState = 2

	elif testState == 2:
		testRun += 1
		# Wait for start command
		go = easygui.boolbox("Begin test?", "Dynosaur 1.0")
		if go:
			plt.show()
			while True:
				serialData = str(ser.readline())
				#print(serialData)
				velocityData = float(serialData[serialData.find("'") + 1 : serialData.find(",") - 1])
				accelerationData = float(serialData[serialData.find(" ") + 1 : serialData.find("\\") - 1])
				velocity.append(velocityData)
				acceleration.append(accelerationData)
				if velocityData >= float(fieldValues[2]):
					break
		reply = easygui.buttonbox("What now?", choices=runChoices)
		testState = runSwitch[reply]

	elif testState == 3:
		# Calibration?

		# Not totally sure what this should do

		# Probably just run a "test" without requiring bike parameters?
		testState = -1

	else:
		print("Exiting")
		break

