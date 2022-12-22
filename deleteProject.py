"""
delete project functions
get user data ----> for bring the data from the file in list
set project id ----> to get the id from the user for delete
delete project ----> main function for delete the project from the list and write the new list in the file
"""
# Alias because the name exist
import projectsMenu as Pro


def getUserProjects():
    projects = []
    file = open("projectInfo.txt", "r")
    for line in file:
        projects.append(list(line.split(":")))
    file.close()
    return projects


def setProjectId():
    projectid = input("What is PROJECT ID you want to Delete? ")
    while True:
        if projectid.isdigit():
            return projectid
        else:
            projectid = input("Invalid ID, What is PROJECT ID you want to Delete? ")


def deleteProject(userid):
    try:
        checkeForEmpty = getUserProjects()
        if len(checkeForEmpty) != 0:
            projectid = setProjectId()
            projects = getUserProjects()
            projectslenth = len(projects)
            for item in projects:
                if item[0] == projectid and item[6] == f"{userid}\n":
                    projects.remove(item)
            if projectslenth != len(projects):
                try:
                    file = open("projectInfo.txt", "w")
                    for project in projects:
                        file.write(
                            f"{project[0]}:{project[1]}:{project[2]}:{project[3]}:{project[4]}:{project[5]}:{project[6]}")
                    file.close()
                    print("===========================================")
                    print("=    This Project Deleted Successfully    =")
                    print("===========================================")
                except Exception as e:
                    print("======================================================")
                    print(f"There is an Error {e}")
                    print("======================================================")

            else:
                print("===========================================")
                print("=         Not Found This Project          =")
                print("===========================================")
        else:
            print("===================================================================")
            print(f"There are no Projects for Delete exist in your account")
            print("===================================================================") 

    except Exception as e:
        print("====================================================================================================")
        print(f"Failed to Open the file its not exist. {e}")
        print("=====================================================================================================")
    
    Pro.projectMenu(userid)
