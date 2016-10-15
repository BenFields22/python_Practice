#defining the function to promt the user to enter a file name and file type.
def getFileName():
    fileName = input('What would you like the file name to be? ')#inputs the file name
    fileType = input('What would you like the file type to be (.txt or .csv) please type the . before the type.')#inputs the file type
    file = fileName + fileType# defines the file name by adding the two user defined strings
    print('Your file name is: ',file)#prints the file name to allow the user to check the name
    return  file#returns the file name from within the function to allow other functions outside the scope of this function to use the file name

def fileContents(fileNameToAddTo):#defining the function to prompt the user to enter some information into the file 
    fileData = input('What would you like to be inside your file? ')#user enters in what they want to be inside their file
    with open(fileNameToAddTo,'w') as openFile:#opens the file name as defined in outside functions or outside the scope of this function.
        openFile.write(fileData)#opens the file as defined in the upper line as "openFile" and writes the information typed in by user from "fileData"
        openFile.close()#closes the file 
        print('You have entered:',fileData,' into your file.')#prints what has been entered into the file so user can check

def readFile(fileToRead):#defining the function to read the contents of the file. the parameters are the file name to enter to be read.
    with open(fileToRead,'r') as fileRead:#opens the file as passed to it from outside the scope of this function and assigns it to vaiable "fileRead"
        readContents = fileRead.read()# reads the contents of the file and assigns it to the value "readContents"
        print('I have read the file contents and it says: ',readContents)#prints what the system has read so that the user can ensure the file was written and read properly
        fileRead.close()#closed the file 
    

def createFile():#defined the main function that calls the other individual functions in a simple organized way
    file = getFileName()#we are defining the name of the file using function name "getFileName". Important to assign the value to "file"
    fileContents(file)#calls function fileContents to get the information for file. we pass the file to it so that the proper file is opened
    readFile(file)#calls function to read the contents of the file as defined in previous steps. Must call the correct file to ensure the right info is read.
    

createFile()#This is actually the only code running or being initiated by the system.One word, one fucntion with many built in functions to do a large amount of things. 

  


