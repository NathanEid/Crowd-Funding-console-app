"""
registration function to get the data from the user and stor it in a file
"""
import re
import mainMenu


def setId():
    userid = input("What is your ID ? ")
    while True:
        if userid.isdigit():
            return userid
        else:
            userid = input("Invalid ID, What is your ID ? ")


def setFirstName():
    firstname = input("What is your FIRST NAME ? ")
    while True:
        if firstname.isalpha():
            return firstname
        else:
            firstname = input("Invalid NAME, What is your FIRST NAME ? ")


def setLastName():
    lastname = input("What is your LAST NAME ? ")
    while True:
        if lastname.isalpha():
            return lastname
        else:
            lastname = input("Invalid NAME What is your LAST NAME ? ")


def setEmail():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = input("What is your EMAIL ? ")
    while True:
        if re.fullmatch(regex, email):
            return email
        else:
            email = input("Invalid EMAIL, What is your EMAIL ? ")


def setPassword():
    password = input("What is your PASSWORD ? ")
    confpassword = input("Please CONFIRM your PASSWORD ? ")
    while True:
        if confpassword == password:
            return password
        else:
            confpassword = input("It doesn't MATCH, Please CONFIRM your PASSWORD ? ")


def setMobile():
    mobileregex = '^01[0-2,5]{1}[0-9]{8}$'
    mobile = input("What is your MOBILE PHONE ? ")
    while True:
        if re.match(mobileregex, mobile):
            return mobile
        else:
            mobile = input("Invalid MOBILE PHONE, What is your MOBILE PHONE ? ")


def setData():
    userid = setId()
    firstname = setFirstName()
    lastname = setLastName()
    email = setEmail()
    password = setPassword()
    mobile = setMobile()

    try:
        fileobj = open("info.txt", "a")
        fileobj.write(f"{userid}:{firstname}:{lastname}:{email}:{password}:{mobile}\n")
        fileobj.close()
        print("===========================================")
        print("=      Registration Done Successfully     =")
        print("===========================================")
        mainMenu.mainFunction()
    except Exception as e:
        print("===================================================================")
        print(f"Registration Failed {e}")
        print("===================================================================")
