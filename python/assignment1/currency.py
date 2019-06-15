#assignment 1

#Currency converter, currency info as of 2/18/2019
YuanPerDollar = 0.15
EurosPerDollar = 1.13
dollars = float(input("Enter the amount of dollars you wish to convert:"))
yuan = YuanPerDollar*dollars
euros = EurosPerDollar*dollars
print("$" + str(dollars) + " is " +str(yuan) + " Yuan. Which is also " + str(euros) + " in Euros.")