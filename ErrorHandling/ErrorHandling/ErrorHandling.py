import sys
def enterFirst():
    try:
        return float(input('Please enter the first number: '))
    except:
        print('that is not an acceptable input please try again')
        return enterFirst()
        
def enterSecond():
    try:
       return float(input('please enter the second number: '))
    except:
       print('that is not an acceptable input please try again')
       return enterSecond()
           
def calculate(first,second):     
    try:
        answer = float(first / second)
        print('The answer is: ',answer)
        return answer
    except:
        error = sys.exc_info()[0]
        print('I am sorry something went wrong')
        print(error)
        



first = enterFirst()
second = enterSecond()
calculate(first,second)
