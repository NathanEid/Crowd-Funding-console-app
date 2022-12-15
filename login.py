"""
login function
"""
import projectsMenu
import mainMenu


def userLogin():
    email = input("Please enter your EMAIL ? ")
    password = input("Please enter your PASSWORD ? ")
    file = open("info.txt", 'r')
    count = 1
    for line in file:
        record = list(line.split(":"))
        if email == str(record[3]) and password == str(record[4]):
            print("==========================Login success==========================")
            projectsMenu.projectMenu(record[0])
            count = 0
            break
        else:
            count += 1

    if count != 0:
        print("==========================Login Failed==========================")
        mainMenu.mainFunction()
