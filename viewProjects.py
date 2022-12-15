"""
view all projects function
"""
import projectsMenu


def viewAllProjects(userid):
    file = open("projectInfo.txt", 'r')
    for line in file:
        record = list(line.split(":"))
        print("============================================================\n")
        print(f"        Project Id             :       {record[0]}")
        print(f"        Project Title          :       {record[1]}")
        print(f"        Project Details        :       {record[2]}")
        print(f"        Project Total Target   :       {record[3]}")
        print(f"        Project Start Date     :       {record[4]}")
        print(f"        Project Dnd Date       :       {record[5]}")
        print(f"        Project User Id        :       {record[6]}")
        print("============================================================")
    file.close()
    projectsMenu.projectMenu(userid)
