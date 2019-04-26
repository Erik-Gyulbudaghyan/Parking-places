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
        parkingIds = parkPlace["parking_places"]["parking_ID"]
        for keys, values in parkingIds.items():
            print(values)
            return parkPlace


def askForPlace():
    current_place = input("Choose your place: ")
    print(current_place)
    return current_place

def loadParkTimeInfo():
    with open('parking.json') as data_file:
        parkTime = json.load(data_file)
        parkingIds2 = parkTime["parking_place"]["Time_range"]
        for keys, values in parkingIds2.items():
            print(keys, "-", values)
            return parkTime



def askForTime():
    current_time = input("Choose your time range: ")
    print(current_time)
    return current_time

def result():
    print(current_place, current_time)
    
    
def loadSetupData():
    place_setup = input("Choose what to change in place: ")
    print(place_setup)
    return place_setup

def loadTimeSetupData():
    time_setup = input("Choose what to change in time range: ")
    print(time_setup)
    return time_setup



def main():
    log = loadLoginData()
    saveName = loadSaveNameData()
    print(saveName)
    parkPlace = loadParkPlaceInfo()
    parkingIds = parkPlace.items()
    print(parkingIds)
    if log == user:
        current_place = askForPlace()
        current_time = askForTime()
        savePlace(current_place)
        sameTime(current_time)
        printCurrentPlace(current_place)
        printCurrentTime(current_time)
        result()=print(current_time, current_place)
    elif log == manager:
        place_setup = loadSetupData()
        time_setup = loadTimeSetupData()
        printCurrentPlace(current_place, place_setup)
        printCurrentTime(current_time, time_setup)

main()
