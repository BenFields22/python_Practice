numbercorrect =0
number =0
for i in range(0,4):
    
    for d in range(0,4):
       useranswer = int(input('what is {0:.0f} * {1:.0f}? '.format(i,d)))
       answer = i*d
       number = number +1
       if useranswer == answer:
            print('great job!')
            numbercorrect= numbercorrect +1
       else:
            print("I'm sorry that is incorrect. Please try again")
            

percent = numbercorrect/number
numberwrong = number-numbercorrect

print('You got {0:d} correct and {1:d} incorrect which is a {2:.2f} %'.format(numbercorrect,numberwrong,percent))






