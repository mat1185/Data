'''
Name: Matthew Chung
Description: Bank application
'''
#open text file
with open("UserInformation.txt") as f:
    #lists for data in file
    userName = []
    userPass = []
    userBal = []
    for each in f:
        #split on space between words
        part = each.split()
        userName.append(str(part[0]))
        userPass.append(str(part[1]))
        userBal.append(float(part[2]))
        
    #starting index for stepping through list
    index = 0
    def uName(x):
        for each in range(len(userName)):
            #if name is correct assign the index to that position in the list to match against password, current balance
            if x == userName[each]:
                index = each
                return index
            else:
                print("Username is invalid please try again")
                #rerun validation from beginning if username does not match
                userNames()
            
    def passWordCheck(x):
        #check password against position in index
        if x == userPass[index]:
            pass
        else:
            print("Password does not match, please try again")
            #if password does not match against return to beginning prompt
            passWord()
                
    def curBalance():
        #returns current balance as requested
        print("Current Balance is: ", userBal[index])
    def deposit(x):
        #add given amount to current balance
        userBal[index]+=x
    def withdrawal(x):
        #subtract given amount to current balance
        userBal[index]-=x
        
    def choice():
        #menu options
        input = str(raw_input("Type D to deposit money \n \
                                Type W to withdraw money \n \
                                Type B to display Balance \n \
                                Type C to change user, display user name \n \
                                Type E to exit \n"
            )).upper()
        return input
    
    def userNames():
        #match against user names list
        user = str(raw_input("Please enter your username:"))
        uName(user)
        return user
    
    def passWord():
        #check input against password list
        pWord = str(raw_input("Please enter your password:"))
        passWordCheck(pWord)
        return pWord
    
    #begin program logic start with user name prompt then password verification and menu inputs
    user = userNames()
    pWord = passWord()
    input = choice()
    
    while input != 'E' or input!='e':
        if input == 'D':
            amt = float(raw_input("Please enter the amount you would like to deposit: "))
            deposit(amt)
            input = choice()
        if input == 'W':
            amt = float(raw_input("Please enter the amount you would like to withdrawal: "))
            withdrawal(amt)
            input = choice()
        if input == 'B':
            curBalance()
            input = choice()
        if input == 'C':
            print("Current username: ", user)
            user = userNames()
            pWord = passWord()
            input = choice()
        if input == 'E' or input=='e':
            break
        else:
            print("Invalid input please try again or type 'E' to exit.")
        
        #begin setting up lists for output
        a = 1
        for z in len(range(userName)):
            out = "line" & a & "=[]"
            a +=1
        #line1=[]
        #line2=[]
        #line3=[]
            y=0
            #had to convert from columns to rows
            for x in userName:
                out.append(str(userName[y]))
                out.append(str(userPass[y]))
                out.append(str(userPass[y]))
                y+=1
            for each in out:
                f.write(each)
            f.write("\n")
            # for each in line2:
            #     f.write(each)
            # f.write("\n")
            # for each in line3:
            #     f.write(each)
        