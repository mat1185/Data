''' 
    Name: Matthew Chung
    Description: Calculating Exam Scores Using For Loops
'''

name = raw_input("What is your name?")
exam1 = int(input("What is the first exam score?"))
exam2 = int(input("What is the second exam score?"))
exam3 = int(input("What is the third exam score?"))

average = ((exam1 + exam2 + exam3)/3)
if (average > 100):
    print(name)
    print("You have input an invalid score, please try again")
    
elif(average > 98):
    print(name)
    print("Average grade is an A+")
    
elif(average > 95):
    print(name)
    print("Average grade is an A")
    
elif(average > 91):
    print(name)
    print("Average grade is an A-")
    
elif(average > 88):
    print(name)
    print("Average grade is a B+")
    
elif(average > 84):
    print(name)
    print("Average grade is a B")
    
elif(average>80):
    print(name)
    print("Average grade is a B-")
    
elif(average > 75):
    print(name)
    print("Average grade is a C+")
    
elif(average > 70):
    print(name)
    print("Average grade is a C")
    
elif(average > 60):
    print(name)
    print("Average grade is a D")
    
else:
    print(name)
    print("Average grade is NC")
    
