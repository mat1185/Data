'''
Name:Matthew Chung
Description: Drink size program for vending machine
'''

size = raw_input("What size drink would you like? Please enter: \n'L' for Large \n'M' for Medium \n'S' for small ")

if((size == 'S') or (size == 's')):
    price = 1
    print("You have ordered a small drink. Thank you.")
elif(size == 'M') or (size == 'm'):
    price = 2
    print("You have ordered a medium drink. Thank you.")
elif(size == 'L') or (size == 'l'):
    price = 3
    print("You have ordered a large drink. Thank you.")
else:
    print("You have entered an invalid selection. Please try again")
    