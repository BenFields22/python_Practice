#program to calculate an order cost and give shipping costs and format number to look like a monetary value

userinput = float(input('What is the amount for your purchase? '))
shipping = 0
if userinput < 50:
    print('That will be an additional $10')
    userinput = userinput + 10
    print('your new total is now $%.2f' % userinput)
    shipping = 10

else:
    print('You qualify for free shipping')

print('Thank you for your order.\n Your total is ${0:,.2f} and your shipping costs are ${1:,.2f}'.format(userinput,shipping))


