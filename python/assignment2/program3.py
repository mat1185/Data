'''
Name: Matthew Chung
Description: program displaying various drinks as well as options to select them
'''

typeOfdrink = int(input("Which type of drink would you like? \nPress 1 for Arizona iced Tea a small is $1.00, medium $2.00, large $3.00\
                            \nPress 2 for a Coca-Cola, a small is $1.50, medium is $3.00, large is $4.50\
                            \nPress 3 for a Water, a small is $0.75, medium is $1.50, large is $2.25\
                            \nPress 4 for a Orange Juice, a small is $2.00, medium is $4.00, large is $6.00"))
if(typeOfdrink == 1):
    cost = 1.00
    print("You have selected Arizona Iced Tea, a small costs $"+ str(cost)+ ".")
elif(typeOfdrink == 2):
    cost = 1.50
    print("You have selected Coca-Cola, a small costs $"+ str(cost)+ ".")
elif(typeOfdrink == 3):
    cost = 0.75
    print("You have entered a Water, a small costs $"+ str(cost)+ ".")
elif(typeOfdrink == 4):
    cost = 2.00
    print("You have entered a Orange Juice, a small costs $"+ str(cost)+ ".")
else:
    print("You have made an invalid selection please try again.")
    
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
    