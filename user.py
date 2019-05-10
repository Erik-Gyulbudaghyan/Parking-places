import json

places = ("place N1", "place N2", "place N3", "place N4", "place N5")
times = ("range 0-2", "range 2-5", "range 5-12", "range 12-24", "range 24-more")

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

def loadAskForPlace(initialParkPlaceData):
    print(places)
    current_place = input("Choose your parking place: ")
    while int(current_place) not in range(0, 5):
        print("Your Data is Wrong, Please Try Again")
        current_place = input("Choose your parking place: ")
    if int(current_place) in range(0, 5):
        current_place_key = "00" + current_place
        print(initialParkPlaceData["parking_place"]["parking_ID"][current_place_key])
        return initialParkPlaceData["parking_place"]["parking_ID"][current_place_key]

def loadSavePlace(initialUsedPlaceData, current_place):
    save_place = current_place
    with open("usedPlace.json", 'r') as file:
        dicts_data = json.load(file)
        dicts_data['used_place'].append(save_place)
    with open("usedPlace.json", 'w') as file:
        file.write(json.dumps(dicts_data))
    return initialUsedPlaceData["used_place"]


def loadAskForTime():
    print(times)
    current_time = input("Choose your parking time range: ")
    while int(current_time) not in range(72):
        print("Your Data is Wrong, Please Try Again")
        current_time = input("Choose your parking time range: ")
    if int(current_time) in range(72):
        return current_time


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
        current_place = loadAskForPlace(parkPlace)
        print(current_place)
        save_place = loadSavePlace(usedPlace, current_place)
        print(save_place, current_place)
        current_time = loadAskForTime()
        print(current_time)
        printResult(int(current_time), current_place, saveName, parkPlace)
main()
