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

def loadUsedPlaceInfo():
    with open('usedPlace.json') as data_file:
        usedPlace = json.load(data_file)
        return usedPlace

def loadSaveData(initialUsedPlaceData):
    with open('usedPlace.json', 'r') as file:
        save_data = json.load(file)
        print(save_data)
        return initialUsedPlaceData["used_place"]

def loadAskForChange():
    change = input("Do you want to make any changes (Yes/Not): ")
    while change == "Not" or "No" or "not" or "no":
        print("Goodbye: ")
        break
    if change == "Yes" or "yes":
        print(change)
        return change

def loadParkPlaceInfo():
    with open('parking.json') as data_file:
        parkPlace = json.load(data_file)
        return parkPlace

def loadTimedata(initialParkPlaceData, change):
    if change == "Yes" or "yes":
        time_change = initialParkPlaceData["parking_place"]["Time_range"]
        print(time_change)



def main():
    log = loadLoginData()
    saveName = loadSaveNameData()
    print(saveName)
    usedPlace = loadUsedPlaceInfo()
    if log == 'manager':
        save_data = loadSaveData(usedPlace)
        print(save_data)
        change = loadAskForChange()
        print(change)
        if change == "Yes" or "yes":
            parkPlace = loadParkPlaceInfo()
            time_change = loadTimedata(parkPlace, change)
            print(time_change)


main()
