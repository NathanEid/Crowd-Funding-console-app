# ITI-DevOps

## Crowd-Funding console app
Crowdfunding is a way to raise money for an individual or organization by collecting donations through 
family, friends, friends of friends, strangers, businesses, and more. By using social media, people can 
reach more potential donors than traditional forms of fundraising.

### The aim of the project
Create a console app to start fundraise projects.

### Technologies
Python 3

### Features
1 - Authentication System:
    • Registration:
        • User ID
        • First name
        • Last name
        • Email [validated against email regex]
        • Password
        • Confirm password
        • Mobile phone [validated against Egyptian phone numbers]
    • Login:
        • The user should be able to login after activation using his email and password

2 - Projects:
    • The user can create a project fund raise campaign which contains:
        • Project ID
        • Title
        • Details
        • Total target (i.e 250000 EGP)
        • Set start/end time for the campaign [validate the date formula]
    • User can view all projects
    • User can edit his own projects
    • User can delete his own project
    • User can search for a project using:
        • Project ID
        • Start Date
        • End Date

### Setup
1- For run the Project on linux:
    • Group all project's files in the same directory.
    • Project runs from the "mainPage.py".
    • Use comand "python3 mainPage.py" in the termenal.
    • Or you can use any IDE like pycharm or visual studio code.

2- For run the Project on another OS:
    • You can use any IDE like pycharm or visual studio code.