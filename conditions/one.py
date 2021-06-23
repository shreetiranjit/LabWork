'''
  Price of a house is $1M. If buyer has good credit, they need to put down 10% otherwise
they need to put down 20%.
Print down  payment.
'''
price_of_the_house = 1000000
hasgoodcredit =  True


if hasgoodcredit:
    down_payment = 0.1 * price_of_the_house
    print(f'the down payment with good credit is {down_payment}:')
else :
    down_payment1 = 0.2 * price_of_the_house
    print(f'the down payment with badcredit is {down_payment1}:')
