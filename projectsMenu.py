"""
main menu for projects function
"""
import createProject
import viewProjects
import mainMenu
import deleteProject
import editProject
import searchProject


def projectMenu(userid):
    choice = input("Please choose from the following menu : \n 1) Create Project \n 2) View All projects"
                   " \n 3) Edit your project \n 4) Delete your project "
                   "\n 5) Search for a project \n 6) Log Out \n 7) Exit \n")
    while True:
        if choice == "1":
            createProject.setData(userid)
            break
        elif choice == "2":
            viewProjects.viewAllProjects(userid)
            break
        elif choice == "3":
            editProject.updateProject(userid)
            break
        elif choice == "4":
            deleteProject.deleteProject(userid)
            break
        elif choice == "5":
            searchProject.searchProject(userid)
            break
        elif choice == "7":
            print("=========")
            print("=  Bye  =")
            print("=========")
            break
        elif choice == "6":
            mainMenu.mainFunction()
            break
        else:
            choice = input("Please choose from the following menu : \n 1) Create Project \n 2) View All projects"
                           " \n 3) Edit your project \n 4) Delete your project \n 5) Search for a project \n")
