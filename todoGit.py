"""
file name input: args
readFile -> File content list  
            args(fileName)
            fileopen return list data
modifyInput-> input list -> output dictionary
              input: data recived from reading file
              dictionary output : 
              [{
                  Event: "",
                  Time:"",
                  Status:"done"/"undone"
              }]
showAllTodo -> display all todo formatted
showSearchedTodoByTime -> input time, output todo
showSearchTodoByEvent -> input event, output time + event
addTodo-> adds a new event + time
deleteTodo-> input name of event : delete that event
showByStatus : input :done / Undone -> respective todo show   
"""

from sys import argv
from os.path import exists
import sys


currentFile,fileName=argv #unpacking


def readFile(fileName):
    """
    readFile: accepts fileName from args
    fileName: file entered by User in args
    returns a list containing each line as a list element
    """
    if exists(fileName):
        fileObject = open(fileName,"r")
        return fileObject.readlines()
    else:
        raise ValueError("File Doesn't Exist")


def formatString(string):
    """
    formatString: It accepts a list element as a string
    where String Slicing is Done
    returns a Dictionary having labels: event time status
    """
    return {
    "event":string[:string.index("#")],
    "time":string[string.index("#")+1:string.index("@")],
    "status":string[string.index("@")+1:]
    }


def modifyInput(fileData):
    """
    modifyInput: accepts a Dictionary
    formattedData: Empty list which accepts a dictonary as list elements
    returns a list of dicionaries
    """
    formattedData=[]
    for i in fileData:
        formattedData.append(formatString(i))
    return formattedData


rawData=readFile(fileName)
modifiedData=modifyInput(rawData)


def showAllTodo(formattedData):
    """
    showAllTodo: accepts a list of dictionary(formattedData)
    prints all todo tasks like this: 
    --TASK 1--
    Event: ""
    Time: ""
    Status:""
    """
    for i in range(len(formattedData)):
        print("--TASK",i+1,"--")
        print("Event:",formattedData[i]["event"])
        print("Time:",formattedData[i]["time"])
        print("Status:",formattedData[i]["status"])


def showSearchedTodoByTime(formattedData):
    """
    showSearchedTodoByDate: accepts a list of dictionary(formattedData)
    takes time as input from user
    prints todo's according to input time
    """
    userDate = input('Enter the Time: ')
    print("Todo on that time are: ")
    cnt = 0
    for i in range(len(formattedData)):
        if formattedData[i]["time"]==userDate:
            print("--TASK",i+1,"--")
            print("Event:",formattedData[i]["event"])
            print("Time:",formattedData[i]["time"])
            print("Status:",formattedData[i]["status"])
            cnt += 1
    if cnt==0:
        print("No Todo on that Time...")


def showSearchTodoByEvent(formattedData):
    """
    showSearchTodoByEvent: accepts a list of dictionary(formattedData)
    takes event as input from user
    prints todo's according to input events
    """
    userEvent = input('Enter the Event: ')
    print("Todo on that Event are: ")
    cnt = 0
    for i in range(len(formattedData)):
        if formattedData[i]["event"].strip().lower()==userEvent.lower():
            print("--TASK",i+1,"--")
            print("Event:",formattedData[i]["event"])
            print("Time:",formattedData[i]["time"])
            print("Status:",formattedData[i]["status"])
            cnt += 1
    if cnt==0:
        print("No Todo on that Event...")

def showByStatus(formattedData):
    """
    showByStatus: accepts a list of dictionary(formattedData)
    takes status as input from user
    prints todo's according to input status
    """
    userStatus = input('Enter the required Status: ')
    print("Todo of that Status are: ")
    cnt = 0
    for i in range(len(formattedData)):
        if formattedData[i]["status"].strip().lower()==userStatus.lower():
            print("--TASK",i+1,"--")
            print("Event:",formattedData[i]["event"])
            print("Time:",formattedData[i]["time"])
            print("Status:",formattedData[i]["status"])
            cnt += 1
    if cnt==0:
        print("No Todo on that Event...")


def addTodo(formattedData):
    """
    addTodo: accepts list of dictionaries
    formattedData: list of dictionaries 
    adds new event to the file object
    """
    reqFile = open(fileName,"a")
    print("Enter the details like: Event #hrs:min@Status")
    reqFile.write("\n")
    reqFile.write(input())
    reqFile.close()
    print("Data stored in the file.")


def deleteTodoByEvent(formattedData):
    """
    deleteTodoByEvent: accepts list of dictionaries
    formattedData: list of dictionaries
    takes event name as input from user
    removes existing event from the file object
    """
    newList = []
    userChoice = input("Enter The Task which you want to delete: ")
    cnt = 0
    for i in range(len(formattedData)):
        if formattedData[i]["event"].strip().lower()!=userChoice.lower():
            newList.append(formattedData[i])
            cnt += 1
            print("Job Done.")
    if cnt==0:
        print("Event doesn't exist.")
    reqFile = open(fileName,"w")
    requiredString=""
    for i in range(len(newList)):
        requiredString+=newList[i]["event"]+" #"+newList[i]["time"]+"@"+newList[i]["status"]
    reqFile.write(requiredString)
    reqFile.close()
    return newList

print("-- Welcome to the TODO App --")
print()
while(True):
    print()
    print("Enter 1 to View All the TODO")
    print("Enter 2 to Add a TODO")
    print("Enter 3 to Search TODO via Time")
    print("Enter 4 to Search TODO via Event")
    print("Enter 5 to Search TODO via Status")
    print("Enter 6 to Delete a TODO")
    print("Enter 7 to Exit the TODO app")
    print()
    k = int(input("Enter Your Choice: "))
    if k==1:
        showAllTodo(modifiedData)
    elif k==2:
        addTodo(modifiedData)
    elif k==3:
        showSearchedTodoByTime(modifiedData)
    elif k==4:
        showSearchTodoByEvent(modifiedData)
    elif k==5:
        showByStatus(modifiedData)
    elif k==6:
        modifiedData=deleteTodoByEvent(modifiedData)
    elif k==7:
        sys.exit()
