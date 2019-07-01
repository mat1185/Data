'''
Name: Matthew Chung
Description: List Menu operations
'''
studentFullName=["Mike navarro","Miguel saba","Maria Rami"]
input = 0
print(', '.join(studentFullName))
def choice ():
    input = int(raw_input("Press 1 if you would like to add an item to the end of the list \n \
                            Press 2 if you would like to Remove an item from the list\n \
                            Press 3 if you would like to Insert an item to the list \n \
                            Press 4 if you would like to find the maximum \n \
                            Press 5 if you would like to find the minimum\n \
                            Press 6 if you would like to sort the list in descending order \n \
                            Press 7 if you would like to exit \n \
                            Please make a selection..."))
    return input
input = choice()
while input < 7:
    if input == 1:
        item = str(raw_input("Please enter what you would like to add to the list: "))
        studentFullName.append(item)
        print("New list is now: ")
        print(', '.join(studentFullName))
        input = choice()
    elif input == 2:
        remove = str(raw_input("What would like to remove?"))
        studentFullName.remove((remove))
        print("New list is now: ")
        print(', '.join(studentFullName))
        input = choice()
    elif input == 3:
        insert = str(raw_input("Please enter what would you like to add to the list: "))
        position = int(raw_input("At what position would you like to add this to the list: "))
        position = position -1
        studentFullName.insert((position), (insert))
        print("New list is now: ")
        print(', '.join(studentFullName))
        input = choice()
    elif input == 4:
        print(max(studentFullName))
        input = choice()
    elif input == 5:
        print(min(studentFullName))
        input = choice()
    elif input == 6:
        studentFullName.sort(reverse=True)
        print("New list is now: ")
        print(', '.join(studentFullName))
        input = choice()
    elif (input > 6):
        break
        