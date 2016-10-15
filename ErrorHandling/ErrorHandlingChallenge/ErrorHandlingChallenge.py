
def openFile(openfile):
    
    try:
        with (open(openfile,'r')) as file:
            contents = file.read()
            report = print('Your file says: ',contents)
            file.close()
            return report
            

    except:
        print('I am sorry your file could not be found.Please try again.')
        return openFile(indicateFile())


def indicateFile():
    try:
        intFile = input('What is the name of the file that you would like to read?\n')

        return intFile


        
    except:
        print('I am sorry that is not an acceptable input. Please try again.')
        return indicateFile()

file = indicateFile()
openFile(file)