import json

places = ("place N1", "place N2", "place N3", "place N4", "place N5")
times = ("range 0-1", "range 1-2", "range 2-5", "range 5-12", "range 12-24", "range 24-more")

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


def loadAskForPlace():
    print(places)
    current_place = input("Choose your parking place: ")
    return current_place

def loadAskForTime():
    print(times)
    current_time = input("Choose your parking time range: ")
    return current_time

def printResult(current_time, current_place, saveName):
    print("Your Place and Time are: " + saveName, current_place, current_time)

def main():
    log = loadLoginData()
    saveName = loadSaveNameData()
    print(saveName)
    parkPlace = loadParkPlaceInfo()
    if log == 'user':
        current_place = loadAskForPlace()
        print(current_place)
        current_time = loadAskForTime()
        print(current_time)
        printResult(current_time, current_place, saveName)
main()
