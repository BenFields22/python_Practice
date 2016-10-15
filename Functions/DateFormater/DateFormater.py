#program to take a date entry and format it to another format that we wish 
import datetime

def enterDate():
    userInput = input('Please enter the current date in the following format mm/dd/yyyy: ')
    enteredDate = datetime.datetime.strptime(userInput,'%m/%d/%Y')
    return enteredDate

def formatDate(dateToFormat):
    print('You entered the date: ',dateToFormat.strftime('%B %d %Y'))#use the strftime function to format the date
    print('Thank you')

def defineTheDateWithCorrectFormat():
    date = enterDate()
    formatDate(date)
    
defineTheDateWithCorrectFormat()

    