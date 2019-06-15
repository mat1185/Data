''' 
    Name: Matthew Chung
    Description: Assignment 4b calculating judges scores
'''

def findLowest(a):
    x = 10.0
    for each in a:
        if each < x:
            x = each
    return x

def findHighest(b):
    y = 0.0
    for each in b:
        if each > y:
            y = each
    return y

def inp(x):
    if x < 0:
        print("Scores must be positive, enter a non-negative value")
        x = float(raw_input("Please re-enter your value: "))
    return x
         
def calcScore(score1, score2, score3, score4, score5):
    total = score1 + score2 + score3 + score4 + score5
    scores = [score1, score2, score3, score4, score5]
    lowest = findLowest(scores)
    highest = findHighest(scores)
    total = (total - lowest - highest)/3
    print("The performer's final score is: " + str(total))
    
def getJudgeData():
    score1 = float(raw_input("Please enter the first judge's score: "))
    score1 = inp(score1)
    score2 = float(raw_input("Please enter the second judge's score: "))
    score2 = inp(score2)
    score3 = float(raw_input("Please enter the third judge's score: "))
    score3 = inp(score3)
    score4 = float(raw_input("Please enter the fourth judge's score: "))
    score4 = inp(score4)
    score5 = float(raw_input("Please enter the fifth judge's score: "))
    score5 = inp(score5)
    calcScore(score1, score2, score3, score4, score5)

getJudgeData()
      