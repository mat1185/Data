'''
Name: Matthew Chung
Description: Weekly study program
'''

#list for the days of the week and variables for the program
dow = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
counta = 0
countb = 0
countc = 0
#loop through days of the week and ask user for input for each day
for each in dow:
    input = float(raw_input("How many hours were spent studying on " + each + "?"))
    if (input < 24):
        if (input >8):
            countc +=1
        elif(input > 4):
            countb +=1
        else:
            counta +=1
    else:
        print("Invalid selection, please enter a proper total")

#print out totals for hours spent studying by three categories
print("Amount of days spent studying 0-3 hours: " + str(counta))
print("Amount of days spent studying 4-7 hours: " + str(countb))
print("Amount of days spent studying 8+ hours: " + str(countc))
