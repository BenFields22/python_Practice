import csv

WRITE = 'w'
READ = 'r'
filename = 'Example.csv'

with open(filename,mode=WRITE) as file:
    file.write('Doyle McCarty,27\nJodi Mills,25\nNicholas Rose,32\nKian Goddard,36\nZuha Hananis,26')
    print('File was succesfully written')
    file.close
with open(filename,mode=READ)as file:

    allRowsList = csv.reader(file)

    for currentLine in allRowsList:
        print(','.join(currentLine))
        
file.close()


