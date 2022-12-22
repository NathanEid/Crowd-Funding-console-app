"""
edit projects function
"""
# Alias because the name exist
import projectsMenu as Pro
import createProject


def getUserProjects():
    projects = []
    file = open("projectInfo.txt", "r")
    for line in file:
        projects.append(list(line.split(":")))
    file.close()
    return projects


def setProjectId():
    projectid = input("What is PROJECT ID you want to Edit? ")
    while True:
        if projectid.isdigit():
            return projectid
        else:
            projectid = input("Invalid ID, What is PROJECT ID you want to Edit? ")


def updateProject(userid):
    try:
        checkeForEmpty = getUserProjects()
        if len(checkeForEmpty) != 0:
            projectid = setProjectId()
            projects = getUserProjects()
            count = 0
            projectindex = 0
            for item in projects:
                if item[0] == projectid and item[6] == f"{userid}\n":
                    projectindex = projects.index(item)
                    break
                else:
                    projectindex = "Null"
                    count = 100
            if count == 100 and projectindex == "Null":
                print("======================================")
                print("=       This Project Not Found       =")
                print("======================================")
            else:
                choice = input("Choose what you want to edit : \n 1) Project Id \n 2) Project Title"
                            " \n 3) Project Details \n 4) Project Total Target \n "
                            "5) Project Start Date \n 6) Project End Date \n")
                while True:
                    if choice == "1":
                        attribute = createProject.setProjectId()
                        projects[projectindex][0] = attribute
                        break
                    elif choice == "2":
                        attribute = createProject.setTitle()
                        projects[projectindex][1] = attribute
                        break
                    elif choice == "3":
                        attribute = createProject.setDetails()
                        projects[projectindex][2] = attribute
                        break
                    elif choice == "4":
                        attribute = createProject.setTotalTarget()
                        projects[projectindex][3] = attribute
                        break
                    elif choice == "5":
                        attribute = createProject.setStartDate()
                        projects[projectindex][4] = attribute
                        break
                    elif choice == "6":
                        attribute = createProject.setEndData()
                        projects[projectindex][5] = attribute
                        break
                    else:
                        choice = input("Choose what you want to edit : \n 1) Project Id \n 2) Project Title"
                                    " \n 3) Project Description \n 4) Project Total Target \n "
                                    "5) Project Start Date \n 6) Project End Date \n")

                try:
                    file = open("projectInfo.txt", "w")
                    for project in projects:
                        file.write(
                            f"{project[0]}:{project[1]}:{project[2]}:{project[3]}:{project[4]}:{project[5]}:{project[6]}")
                    file.close()
                    print("===========================================")
                    print("=    This Project Updated Successfully    =")
                    print("===========================================")
                except Exception as e:
                    print("===================================================================")
                    print(f"There is an Error {e}")
                    print("===================================================================")
        else:
            print("===================================================================")
            print(f"There are no Projects for Edit exist in your account")
            print("===================================================================")

    except Exception as e:
        print("====================================================================================================")
        print(f"Failed to Open the file its not exist. {e}")
        print("=====================================================================================================")
        
    Pro.projectMenu(userid)
