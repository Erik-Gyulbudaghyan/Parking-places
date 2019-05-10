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





def main():
    log = loadLoginData()
    saveName = loadSaveNameData()
    print(saveName)
    
main()
