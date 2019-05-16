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
    while change.lower() == "no" or change.lower() == "not":
        print("Goodbye: ")
        change = input("You can change your opinion:  (Yes/Not): ")
    if change.lower() == "yes":
        print(change)
        return change

def loadParkPlaceInfo():
    with open('parking.json') as data_file:
        parkPlace = json.load(data_file)
        return parkPlace

def loadPlaceData(initialParkPlaceData, change):
    if change.lower() == "yes":
        place_code = initialParkPlaceData["parking_place"]["parking_ID"]
        print(place_code)

def loadFirstQuestionData():
    question = input("Do you want to change some of these parking areas (Yes/No): ")
    while question.lower() == "no" or question.lower() == "not":
        print("OK, if you want to change your opinion please write Yes: ")
        question = input("Do you want to change some of these parking areas (Yes/No): ")
    if question.lower() == "yes":
        print(question)
        return question

def AskPlaceChange(initialParkPlaceData, question):
    if question.lower() == "yes":
        new_placeData = input("write new place number: ")
        new_place = input("Also input the name: ")
        parking_data = {
            "00" + new_placeData: new_place,
        }
        print(parking_data)
        initialParkPlaceData["parking_place"]["parking_ID"]["00" + new_placeData] = new_place
        with open("parking.json", 'w') as file:
            file.write(json.dumps(initialParkPlaceData))


def loadTimeData(initialParkPlaceData, change):
    if change.lower() == "yes":
        time_code = initialParkPlaceData["parking_place"]["Time_range"]
        print(time_code)

def loadQuestionData():
        question = input("Do you want to change some of these ranges (Yes/No): ")
        while question.lower() == "no" or question.lower() == "not":
            print("OK, if you want to change your opinion please write Yes: ")
            question = input("Do you want to change some of these ranges (Yes/No): ")
        if question.lower() == "yes":
            print(question)
            return question

def askTimeChange(initialParkPlaceData, question):
    if question.lower() == "yes":
        time_change = input("Chose which to change: ").lower()
        if time_change == "range 0-2" or time_change == "range 2-5" or time_change == "range 5-12" or time_change == "range 12-24" or time_change == "range 24-72":
            with open("parking.json", 'r') as file:
                read_data = json.load(file)
                initialParkPlaceData["parking_place"]["Time_range"][time_change] = int(input("New rate: "))
            with open("parking.json", 'w') as file:
                file.write(json.dumps(initialParkPlaceData))





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
        if change.lower() == "yes":
            parkPlace = loadParkPlaceInfo()
            place_code = loadPlaceData(parkPlace, change)
            print(place_code)
            question = loadFirstQuestionData()
            if question.lower() == "yes":
                parking_data = AskPlaceChange(parkPlace, question)
                print(parking_data)
                time_code = loadTimeData(parkPlace, change)
                print(time_code)
                question = loadQuestionData()
                if question.lower() == "yes":
                    time_change = askTimeChange(parkPlace, question)
                    print(time_change)
main()
