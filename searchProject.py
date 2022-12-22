import createProject
import projectsMenu
import editProject


def showProject(project):
    print("============================================================\n")
    print(f"        Project Id             :       {project[0]}")
    print(f"        Project Title          :       {project[1]}")
    print(f"        Project Details        :       {project[2]}")
    print(f"        Project Total Target   :       {project[3]}")
    print(f"        Project Start Date     :       {project[4]}")
    print(f"        Project Dnd Date       :       {project[5]}")
    print(f"        Project User Id        :       {project[6]}")
    print("============================================================")


def searchProject(userid):
    try:
        projects = editProject.getUserProjects()
        if len(projects) != 0:
            found = 0
            count = 0
            choice = input("Choose what you want to Search with : \n 1) Project Id \n 2) Project Start Date"
                        " \n 3) Project End Date \n 4) Back \n ")
            while True:
                if choice == "1":
                    attribute = createProject.setProjectId()
                    for project in projects:
                        if project[0] == attribute:
                            showProject(project)
                            found = 100
                        else:
                            count = 100
                    if count == 100 and found != 100:
                        print("===========================")
                        print("=    This Id Not Found    =")
                        print("===========================")
                    searchProject(userid)
                    break
                elif choice == "2":
                    attribute = createProject.setStartDate()
                    for project in projects:
                        if project[4] == attribute:
                            showProject(project)
                            found = 100
                        else:
                            count = 100
                    if count == 100 and found != 100:
                        print("===================================")
                        print("=    This Start Date Not Found    =")
                        print("===================================")
                    searchProject(userid)
                    break
                elif choice == "3":
                    attribute = createProject.setEndData()
                    for project in projects:
                        if project[5] == attribute:
                            showProject(project)
                            found = 100
                        else:
                            count = 100
                    if count == 100 and found != 100:
                        print("=================================")
                        print("=    This End Date Not Found    =")
                        print("=================================")
                    searchProject(userid)
                    break
                elif choice == "4":
                    projectsMenu.projectMenu(userid)
                    break
                else:
                    choice = input("Choose what you want to Search with : \n 1) Project Id \n 2) Project Start Date"
                                " \n 3) Project End Date \n 4) Back \n ")
        else:
            print("===================================================================")
            print("There are no Projects for search, The file is Empty.")
            print("===================================================================")
            
            projectsMenu.projectMenu(userid)

    except Exception as e:
        print("====================================================================================================")
        print(f"Failed to Open the file its not exist. {e}")
        print("=====================================================================================================")
        
        projectsMenu.projectMenu(userid)
