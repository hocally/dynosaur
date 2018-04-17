import serial
import csv
import easygui
import datetime
import matplotlib.pyplot as plt

X = [590, 540, 740, 130, 810, 300, 320, 230, 470, 620, 770, 250]
Y = [32, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]


#Program vars
port = '/dev/ttyUSB0'
#ser = serial.Serial(port, 115200)
logo = "logo.gif"
testState = 0
testRun = 1

#Test vars
flywheels = [69, 420, 1337]
testInfo = ["Bike", "Operator"]
testChoices = ["Quit", "Enter test params.", "Calibration mode"]
testSwitch = {testChoices[0] : -1, testChoices[1] : 1, testChoices[2] : 3}
runChoices = ["Go to start", "Test same bike", "Test new bike", "Quit"]
runSwitch = {runChoices[0] : 0, runChoices[1] : 2, runChoices[2] : 1, runChoices[3] : -1}

while True:
	if testState == 0:
		reply = easygui.buttonbox("Please select the desired option.", image = logo, choices = testChoices)
		if reply == logo:
			testState = 0
			continue
		testState = testSwitch[reply]

	elif testState == 1:
		fieldValues = easygui.multenterbox("Please enter the following information about the test", "Dynosaur 1.0", testInfo)
		flywheel = easygui.choicebox("Please select the flywheel being used for the test. \nUnits are in kg * m²", "Dynosaur 1.0", flywheels)
		now = datetime.datetime.now()
		filename = fieldValues[0].replace(" ", "") + "_" + fieldValues[1].replace(" ", "") + "_" + str(now.month) + "_" + str(now.day) + "_" + str(now.year) + "_" + str(testRun)
		path = easygui.diropenbox("Please select the directory to save the test data.", "Dynosaur 1.0", "~")
		testState = 2

	elif testState == 2:
		#run test
		#view/save results
		reply = easygui.buttonbox("What now?", choices=runChoices)
		testState = testSwitch[reply]

	elif testState == 3:
		#calibration?
		print("Calibrating dyno")
		testState = -1

	else:
		break
