'''
Name: Matthew Chung
Description: Program to count months over budget for gas and electric

'''
#list of months and variables for budget
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
budget = 0
for each in months:
    inputE = float(raw_input("How much was the eletric bill for " + each + "?"))
    inputG = float(raw_input("How much was the gas bill for " + each +"?"))
    if (inputE > 70.00) or (inputG > 30.00):
        budget += 1
        
        
print("Went over budget " + str(budget) + " months this year.")