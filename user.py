import json

def loadLoginData():
    log = input("choose between user/manager: ")
    user = "user"
    manager = "manager"
    if log == user:
        print(user)
    elif log == manager:
        print(manager)
    return log


def loadSaveNameData():
    saveName = input("Name and Surname: ")
    return saveName

def loadParkPlaceInfo():
    with open('parking.json') as data_file:
        parkPlace = json.load(data_file)
        return parkPlace

def loadUsedPlaceInfo():
    with open('usedPlace.json') as data_file:
        usedPlace = json.load(data_file)
        return usedPlace


def loadAskForPlace(initialParkPlaceData, initialUsedPlaceData):
    place_code = initialParkPlaceData["parking_place"]["parking_ID"]
    print(place_code)
    current_place = input("Choose your parking place: ")

    while True:
        if int(current_place) not in range(0, 20):
            print("Your Data is Wrong, Please Try Again")
            current_place = input("Choose your parking place: ")
        if int(current_place) in range(0, 20):
            current_place_key = "00" + current_place
            if (checkIfOccupied(current_place_key, initialUsedPlaceData)):
                print("This Place is occupied: ")
                current_place = input("Choose your parking place: ")
            else:
                break
    print(initialParkPlaceData["parking_place"]["parking_ID"][current_place_key])
    return initialParkPlaceData["parking_place"]["parking_ID"][current_place_key]

def checkIfOccupied(current_place_key, initialUsedPlaceData):
    for key, item in initialUsedPlaceData["used_place"].items():
        if (item["place"] == current_place_key):
            return True
    return False

def loadAskForTime(initialParkPlaceData):
    time_time = initialParkPlaceData["parking_place"]["Time_range"]
    print(time_time)
    current_time = input("Choose your parking time range: ")
    while int(current_time) not in range(72):
        print("Your Data is Wrong, Please Try Again")
        current_time = input("Choose your parking time range: ")
    if int(current_time) in range(72):
        return current_time

def loadSavePlace(userName, initialUsedPlaceData, current_place, current_time):
    user_data = {
        "place" : current_place,
        "duration" : current_time
    }

    initialUsedPlaceData["used_place"][userName] = user_data

    with open("usedPlace.json", 'w') as file:
        file.write(json.dumps(initialUsedPlaceData))

def printResult(current_time, current_place, saveName, initialParkPlaceData):
    price = -1
    if current_time in range(2):
        price = initialParkPlaceData["parking_place"]["Time_range"]["range 0-2"]
    elif current_time in range(2, 5):
        price = initialParkPlaceData["parking_place"]["Time_range"]["range 2-5"]
    elif current_time in range(5, 12):
        price = initialParkPlaceData["parking_place"]["Time_range"]["range 5-12"]
    elif current_time in range(12, 24):
        price = initialParkPlaceData["parking_place"]["Time_range"]["range 12-24"]
    elif current_time in range(24, 72):
        price = initialParkPlaceData["parking_place"]["Time_range"]["range 24-72"]

    if (price > -1 ):
        print("Your Place and Time are: " + saveName, current_place, str(current_time) + " hours: " + str(price) + " AMD")
    else:
        print("Your Data is wrong")
        return printResult

def main():
    log = loadLoginData()
    saveName = loadSaveNameData()
    print(saveName)
    parkPlace = loadParkPlaceInfo()
    if log == 'user':
        usedPlace = loadUsedPlaceInfo()
        current_place_key = loadUsedPlaceInfo()
        user_data = checkIfOccupied(current_place_key, usedPlace)
        print(user_data)
        current_place = loadAskForPlace(parkPlace, usedPlace)
        print(current_place)
        current_time = loadAskForTime(parkPlace)
        print(current_time)
        save_place = loadSavePlace(saveName, usedPlace, current_place, current_time)
        print(save_place)
        printResult(int(current_time), current_place, saveName, parkPlace)

main()
