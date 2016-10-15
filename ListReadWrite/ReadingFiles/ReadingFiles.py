import csv
with open('ExampleReadFile.txt','r') as exFile:
    allRowsList = csv.reader(exFile)

    for currentRow in allRowsList:
        print(','.join(currentRow))
        for firstEntry in currentRow:
            print(firstEntry)



##allFileContents = exFile.read()
#firstLine = exFile.readline()

#print(firstLine)
#secondLine = exFile.readline()
#print(secondLine)

exFile.close()

