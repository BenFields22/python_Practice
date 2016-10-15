def binaryToNumber():
    binaryNum = input('Please enter a number in binary form: ')
    total = 0
    numLength = len(binaryNum)
    exponent = numLength - 1
    if binaryNum == "":
        print('Im sorry it does not appear you entered a number.\n')
        binaryToNumber()
    else:
        for i in range(0,numLength):
            #print(i)
            currentValue = int(binaryNum[i])
            if currentValue > 1 or currentValue < 0:
                print('Please make sure to enter a binary formated number (e.g. 101010).')
                binaryToNumber()
                return
            else:
                posValue = (currentValue*(2**exponent))
                exponent -= 1
                total = total+posValue
                #print(posValue)
        print('The binary number ',binaryNum, '=',total)
binaryToNumber()





