"""
login function
"""
import projectsMenu
import mainMenu


def userLogin():
    try:
        file = open("info.txt", 'r')
        email = input("Please enter your EMAIL ? ")
        password = input("Please enter your PASSWORD ? ")
        count = 1
        for line in file:
            record = list(line.split(":"))
            if email == str(record[3]) and password == str(record[4]):
                print("=================================================================")
                print("=               Successful login, Projects Menu.                =")
                print("=================================================================")
                projectsMenu.projectMenu(record[0])
                count = 0
                break
            else:
                count += 1

        if count != 0:
            print("=================================================================")
            print("=               Invalid login, please try again.                =")
            print("=================================================================")
            mainMenu.mainFunction()

    except Exception as e:
        print("====================================================================================================")
        print(f"Failed to Open the file its not exist. {e}")
        print("=====================================================================================================")

        mainMenu.mainFunction()

