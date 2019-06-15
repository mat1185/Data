'''
Name: Matthew Chung
Description: Calculating Gross Pay Using For Loop
'''

numOfEmp = input("How many employees are there?")

intOfEmp = int(numOfEmp)

for i in range(intOfEmp):
    name = raw_input("What is the name of this employee?")
    state = raw_input("What state does this employee live in?")
    salary = float(input("What is the net salary of the employee?"))
    if (salary > 100000):
        fedTax = salary*.20
    else:
        fedTax = salary*.15
    if (state == 'CA') or (state == 'NV') or (state == 'AZ') or (state == 'TX'):
        stateTax = salary*.1
    else:
        stateTax = salary*.12
    netSalary = salary - fedTax - stateTax
    print(name)
    print(netSalary)
        
        