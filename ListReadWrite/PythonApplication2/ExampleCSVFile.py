WRITE = 'w'
READWRITE = 'w+'
filename = 'ExampleCSV.csv'

file = open(filename,mode=READWRITE)

file.write('Doyle McCarty,27\nJodi Mills,25\nNicholas Rose,32\nKian Goddard,36\nZuha Hananis,26')

file.close()

print('File was succesfully written')

