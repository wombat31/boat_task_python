boat1=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
boat2=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
boat3=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
boat4=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
boat5=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
boat6=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
boat7=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
boat8=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
boat9=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
boat10=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
boatTimes=[10.0,10.5,11.0,11.5,12.0,12.5,13.0,13.5,14.0,14.5,15.0,15.5,16.0,16.5,17.0]
halfHourCost=12
hourCost=20
availableSlotCheck=0
addHalfHour = False

# Ask which boat you would like to take out

while True:
    try:
        boatChoice = int(input("Which boat would you like to hire? (1 - 10)"))
        if boatChoice in range(0,11):
            print("Thank you, your preference is noted")
            break
        else:
            print("Sorry, that is an invalid choice, please choose again")
    except ValueError:
        print("That is not even a number, please try again!")

#Gain a valid time for booking out

while True:
    try:
        timeOut = float(input("What time would you like to take the boat out?"))
        if timeOut>=10 and timeOut<=16.5:
            print("Thank you, that is a valid time for booking out a boat")
            break
        else:
            print("Sorry, that is an invalid time")
    except ValueError:
        print("That is not even a number")

#Gain a valid time for returning the boat

while True:
    try:
        timeIn = float(input("What time would you like to return the boat"))
        if timeIn>=10.5 and timeIn <=17:
            print("Thank you, that is a valid time for bookign out a boat")
            break
        else:
            print("Sorry that is not a valid return time")
    except ValueError:
        print("That is not even a number")

#Check if boat is available by checking the boat array to see if
#there are only "0" in the required array indices
timeRequired = boatTimes.index(timeIn) - boatTimes.index(timeOut)
for i in range(boatTimes.index(timeOut),boatTimes.index(timeIn)):
    if boat1[i] == "0":
        availableSlotCheck = availableSlotCheck + 1
if availableSlotCheck== timeRequired:
    print("The boat is available at the times requested")
else:
    print("Sorry the boat is not available")

# Work out whether or not to add half an hour
if timeRequired % 2 != 0:
    addHalfHour = True

#Append to the chosen boat array
if boatChoice==1:
    if addHalfHour == False:
        for i in range (timeRequired):
            boat1[boatTimes.index(timeOut) + i]=(hourCost/2)
    else:
        for i in range (timeRequired-1):
            boat1[boatTimes.index(timeOut)+ i]=(hourCost/2)
        boat1[(boatTimes.index(timeOut)+(timeRequired-1))]=(halfHourCost)
        