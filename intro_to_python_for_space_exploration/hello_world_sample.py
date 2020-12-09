#variables-----------------------------
numberOfRocks = 5
tempInSpace = -457.87
roverName = "Artemis Rover"
roketOn = False

basaltRockCount = 0
basaltRockCount = 3
basaltRockCount = basaltRockCount + 1
basaltRockCount = 5
basaltRockCount += 3
basaltRockCount -= 2

astronaut = "Remy Morris"
upperCase = astronaut.upper()
upperCase
lowerCase = astronaut.lower()
lowerCase
rocketOutput = "rOckEt iS A laUncH!"
rocketOutput.capitalize()

launchLocationCity = "Cape Canaveral, "
launchLocationState = "Florida"
launchLocationCity + launchLocationState

artemisRoverSounds = "beep beep "
artemisRoverSounds * 3

# Create a list of common moon rocks
rockTypes = ["basalt", "highland", "breccia"]
rockTypes

# A list with rock names and the number of that rock found
rockTypeAndCount = ["basalt", 1, "highland", 2.5, "breccia", 5]
rockTypeAndCount

rockTypes.append("soil")
rockTypes

rockTypes.pop()
rockTypes

rockTypes[0]
rockTypes[2]

rockTypes[2] = "soil"
rockTypes[2]

#print-----------------------------------

numBasalt = 4
print("The number of Basalt rocks found:", numBasalt)

date = "February 26"
numRocks = 15
print("On", date, "number of rocks found:", numRocks)

#True or False---------------------------
temp = 50
print(temp >= 32)
print(temp < 32)

rock = "basalt"
print("highland" == rock)
print("basalt" == rock)

rock = "basaltrock"
print("highland" in rock)
print("basalt" in rock)

#if else--------------------------------

basalt = 1
if basalt == 0:
    print("We have found no basalt rocks.")
else:
    print("We have found some basalt rocks!")
print("Done checking basalt rocks.")

basalt = 1
if basalt == 0:
    print("We found no basalt rocks.")
elif basalt == 1:
    print("We found exactly 1 basalt rock.")
else:
    print("We found more than 1 basalt rock!")
print("Done checking basalt rocks.")

#function-------------------------------
import time
def launchRocket():
    countdown = 5
    while countdown >= 0:
        time.sleep(1)
        print(countdown)
        countdown = countdown - 1  
    print("Lift Off")

launchRocket()

planets = "Mars","Saturn", "Jupiter"

for planet in planets:
    print(planet)

#file I/O-----------------------------

strPath = "text.txt"
fileObject = open(strPath)
textList = fileObject.readlines()
fileObject.close()

for line in textList:
    print(line)

def OutputRocketText(textInput):
    textInput = textInput + " two days."
    return textInput

rocketText = "We will launch in"
newRocketText = OutputRocketText(rocketText)
print(newRocketText)

#Count--------------------------------

print("Artemis Rover Rock Scanner Starting")
basalt = 0
breccia = 0
highland = 0
regolith = 0
rockList = []

strPath = "rocks.txt"
fileObject = open(strPath)
rockList = fileObject.readlines()

for rock in rockList:
    print(rock)

fileObject.close()

def countMoonRocks(rockToID):
    global basalt,breccia,highland,regolith

    rockToID = rockToID.lower()

    if("basalt" in rockToID):
        print("Found a basalt\n")
        basalt += 1
    elif("breccia" in rockToID):
        print("Found a breccia\n")
        breccia += 1
    elif("highland" in rockToID):
        print("Found a highland\n")
        highland += 1
    elif("regolith" in rockToID):
        print("Found a regolith\n")
        regolith += 1
    return

for rock in rockList:
    countMoonRocks(rock)

# TODO Add a print statement for the other types of rocks: breccia, highland and regolith
print("Number of Basalt: ", basalt)
print("Number of breccia: ", breccia)
print("Number of highland: ", highland)
print("Number of regolith: ", regolith)

print("The max number of one type of rock was:", max(basalt, breccia, highland,regolith))
print("The minimum number of one type of rock was:", min(basalt, breccia, highland, regolith))

#Count V2----------------------------------------

rock_category = {"basalt":0, "breccia":0, "highland":0, "regolith":0}

def countMoonRocksV2(rock_list):
    for thisRock in rock_list:
        for is_this_category in rock_category.keys():
            if is_this_category in thisRock:
                rock_category[is_this_category]+=1
    return

countMoonRocksV2(rockList)

import pandas as pd
rock_df = pd.DataFrame({'count':rock_category})
rock_df.sort_values(by='count',ascending=False)