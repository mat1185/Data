'''
Name: Matthew Chung
Description: money collection interface for vending machine
'''


drink1 = float(input("Coca-cola is $1.50. If you would like a Coca-Cola how much money will you input?"))

if (drink1 > 1.50):
    change = drink1 - 1.50
    print("Your change is $", change, ". Thank you - enjoy your drink!")
else:
    print("You did not enter enough money, please enter more than $", drink1, ".")