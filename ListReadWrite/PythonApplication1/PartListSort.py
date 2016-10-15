#code to practice different coding tecniques 

guests = []
name = '  '
command = '  '
i = 1
while command != 'DONE':
    name = input('Please enter the name of the person attending the party.\n').upper()

    guests.append(name)
    print(name,' has been added to the guest list')

    command = input('\nIf you have another person to add please press ENTER.\nIf there are no more names to add then please type DONE.').upper()


guests.sort()
print('Your guest list, in alphabetical order is: ')

for guest in guests:
    print(i,'.)',guest.capitalize())
    i+=1


    



