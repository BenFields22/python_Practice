#code to calculate the total to charge for an order from an online store in canada

order = float(input('What was the cost of your order? '))

input('Thank you for shopping at FB Trade. Please press ENTER to finsh checking out.')



print('Thank you! Just confirming that your order was ${0:,.2f}'.format(order))
alberttax = .0005
onnbns = .0013
othertax1 = .0006
othertax2 = .0005


Country = input('What country are you from? ').upper()

if Country == 'CANADA':
    print('You have to pay tax on this order')
    province = input('what province are you from? ').upper()
    if province == 'ALBERTA':
        order = order + (order*alberttax)
        print('You must pay a General sales tax of .05%')
        print('Your total comes out to be ${0:,.2f}'.format(order))
         
    elif province == 'ONTARIO' or province =='NEW BRUNSWICK' or province =='NOVA SCOTIA':
        order = order + (order*onnbns)
        print('You must pay a harmonized sales tax of .13%')
        print('Your total comes out to be ${0:,.2f}'.format(order))
    else:
        print('You must pay a .06% provincial sales tax and a .05% General Sales Tax')
        order = order + (order*othertax1)+(order*othertax2)
        print('Your total comes out to be ${0:,.2f}'.format(order))

else:
    print('You do not have to pay any taxes on this order')
    print('Your total comes out to be ${0:,.2f}'.format(order))

print('Thank you and have a nice day.')



 




