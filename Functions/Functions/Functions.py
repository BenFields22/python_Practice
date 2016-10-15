def main():
    names = ['christopher','Ben','Chris']
    nextGuest = input('Please enter the next guest')
    names.append(nextGuest)
    
    listNames(names)
   
    return

def listNames(names):
    for i in names:
        print(i)
    return



main()

