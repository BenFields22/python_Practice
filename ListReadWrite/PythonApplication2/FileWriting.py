filename = 'demo.csv'
WRITE = 'w'
READ = 'r'
APPEND = 'a'
READWRITE = 'w+'
file = open(filename,mode = READWRITE)

file.write('Ben,23\n')
file.write('Chris,23')

file.close()

print('File was successfully written')

