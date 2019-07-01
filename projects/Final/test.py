with open("UserInformation.txt") as f:
    userNames = []
    userPass = []
    userBal = []
    for each in f:
        part = each.split()
        userNames.append(part[0])
        userPass.append(part[1])
        userBal.append(part[2])
    print(userNames)
    print(userPass)
    print(userBal)