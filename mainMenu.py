"""
main application menu function
"""
import registration
import login


def mainFunction():
    choice = input("Please choose registration or login : \n 1) Registration \n 2) Login \n 3) Exit \n")
    while True:
        if choice == "1":
            registration.setData()
            break
        elif choice == "2":
            login.userLogin()
            break
        elif choice == "3":
            print("=========")
            print("=  Bye  =")
            print("=========")
            break
        else:
            choice = input("You should choose registration or login : \n 1) Registration \n 2) Login \n 3) Exit")
