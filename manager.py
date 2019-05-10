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


def main():
    log = loadLoginData()
    saveName = loadSaveNameData()
    print(saveName)
    usedPlace = loadUsedPlaceInfo()
    if log == 'manager':
        save_data = loadSaveData(usedPlace)
        print(save_data)


main()
