import datetime#imports information regarding the date and time

#prompt the user that we are going to be inputing information regarding the project.
input('Thank you for using FieldsMachine for your scheduling needs.\nPlease press ENTER to input the deadline information for this project.')

#ask the user to input the due date with the correct format
userinput = input('\nWhat is the deadline for this particular project? \nPlease enter it in the following format: mm/dd/yyyy \n')

#we are creating the deadline from the user input. the user input was a string therefore it must be turned into a date variable using strptime
deadline = datetime.datetime.strptime(userinput, '%m/%d/%Y').date()

#this assigns the current date and time to be used in calculating the delta t
currentday = datetime.date.today()

#print the deadline you entered followed by todays date to give the user some dates to reference
print('\nThe project deadline is ',deadline.strftime('%B %d %Y')+'\nThe date today is ', currentday.strftime('%B %d %Y'))

#calculates the difference in dates. This variable contains the total date information difference
daysleft = deadline - currentday

#calculated the number of weeks based on the days differnce and dividing by 7. The .days function turns the date information into a integer
weeks = daysleft.days/7

#show the user how much time they have till the project is due in days and weeks.
print('\nYou have ', daysleft.days,' days to complete your project (%.1f Weeks)' % weeks)

input('Thank you!')





































