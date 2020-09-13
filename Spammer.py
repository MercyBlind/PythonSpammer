import os
import pyautogui, time
clear = lambda: os.system('cls')




users = {}
status = ""


def displayMenu():
    status = input("Are you registered user? y/n?\nInput: ")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()


def newUser():
    clear()
    createLogin = input("Create login name: ")

    if createLogin in users:
        print("\nLogin name already exist!\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        print("\nUser created! Redirecting. . .\n")
        time.sleep(2)
        clear()


def oldUser():
    clear()
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    if login in users and users[login] == passw:
        time.sleep(2)
        print("\nLogin successful!\n")
        time.sleep(3)
        clear()
        Main()

    else:
        print("\nUser doesn't exist or wrong password!\n")
        time.sleep(3)
        clear()

def Main():
    clear()
    print("Starting In 5 Seconds. . .")
    time.sleep(3)
    f = open("beee", 'r')
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        time.sleep(2)



while status != "q":
    displayMenu()