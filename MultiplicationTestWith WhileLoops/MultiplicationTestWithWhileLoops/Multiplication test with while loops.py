one =0
two =0
count=0
attempt =0
numbercorrect = 0
numwrong = 0

Testupto = int(input('To what number would you like to tet your multiplication? '))

while count <Testupto:
    answer =input('what is {0:d} * {1:d}?'.format(one,two))
    
    if int(answer) == one*two:
        print('great work')
        one+=1
        numbercorrect +=1
        if one == 5:
            two+=1

    else:
        print('That is incorrect')
        attempt += 1
        if attempt == 3:
            print('You have used all your attempts.')
            one+=1
            numwrong +=1

    if one == 5:
        one = 0
        count +=1
percent = (numbercorrect/(numbercorrect+numwrong))*100
total = numbercorrect+numwrong
input('You have completed the test. \nYou got {0:d} out of {1:d} correct for a test score of {2:.2f}%'.format(numbercorrect,total,percent))
