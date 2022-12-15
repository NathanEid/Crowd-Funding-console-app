"""
create project function
"""
import re
import projectsMenu
import datetime


def setProjectId():
    projectid = input("What is your PROJECT ID ? ")
    while True:
        if projectid.isdigit():
            return projectid
        else:
            projectid = input("Invalid ID, What is your ID ? ")


def setTitle():
    title = input("What is your PROJECT TITLE ? ")
    return title


def setDetails():
    details = input("What is your PROJECT DETAILS ? ")
    return details


def setTotalTarget():
    totaltarget = input("What is your TOTAL TARGET ? ")
    while True:
        if totaltarget.isdigit():
            return totaltarget
        else:
            totaltarget = input("Invalid TARGET, What is your TOTAL TARGET ? ")


def validate(date_text):
    try:
        if date_text == datetime.datetime.strptime(date_text, '%d-%m-%Y').strftime('%d-%m-%Y'):
            return date_text
    except Exception as e:
        return f"Not match {e}"


def setStartDate():
    startdate = input("Enter the START DATE in form DD-MM-YYYY ? ")
    while True:
        if startdate == validate(startdate):
            return startdate
        else:
            startdate = input("Invalid DATE form, Enter the START DATE in form DD-MM-YYYY ? ")


def setEndData():
    enddate = input("Enter the END DATE in form DD-MM-YYYY ? ")
    while True:
        if enddate == validate(enddate):
            return enddate
        else:
            enddate = input("Invalid DATE form, Enter the END DATE in form DD-MM-YYYY ? ")


def setData(userid):
    projectid = setProjectId()
    title = setTitle()
    details = setDetails()
    totaltarget = setTotalTarget()
    startdate = setStartDate()
    enddate = setEndData()
    projectuserid = userid

    try:
        fileobj = open("projectInfo.txt", "a")
        fileobj.write(f"{projectid}:{title}:{details}:{totaltarget}:{startdate}:{enddate}:{projectuserid}\n")
        fileobj.close()
        print("===========================================")
        print("=      Project Created Successfully       =")
        print("===========================================")
        projectsMenu.projectMenu(userid)
    except Exception as e:
        print(e)
