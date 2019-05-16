import user
import manager

variation = ("user", "manager", "exit")

def main():
    print(variation)
    choice = input("Choose one of them: ")
    if choice.lower() == "user":
        user.main()
    elif choice.lower() == "manager":
        manager.main()
    elif choice.lower() == "exit":
        print("Goodbye, but if you want to can change your opinion: ")
        choice = input("Choose one of them: ")
        return choice


main()
