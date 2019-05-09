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


def loadAskForPlace(initialParkPlaceData):
    print(places)
    current_place = input("Choose your parking place: ")
    while int(current_place) not in range(0, 5):
        print("Your Data is Wrong, Please Try Again")
        current_place = input("Choose your parking place: ")
    if int(current_place) in range(0, 5):
        current_place_key = "00" + current_place
        print(initialParkPlaceData["parking_places"]["parking_ID"][current_place_key])
        return initialParkPlaceData["parking_places"]["parking_ID"][current_place_key]


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
        price = initialParkPlaceData["parking_places"]["time_range"]["range 0-2"]
    elif current_time in range(2, 5):
        price = initialParkPlaceData["parking_places"]["time_range"]["range 2-5"]
    elif current_time in range(5, 12):
        price = initialParkPlaceData["parking_places"]["time_range"]["range 5-12"]
    elif current_time in range(12, 24):
        price = initialParkPlaceData["parking_places"]["time_range"]["range 12-24"]
    elif current_time in range(24, 72):
        price = initialParkPlaceData["parking_places"]["time_range"]["range 24-100"]

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
        current_place = loadAskForPlace(parkPlace)
        print(current_place)
        current_time = loadAskForTime()
        print(current_time)
        printResult(int(current_time), current_place, saveName, parkPlace)
main()
