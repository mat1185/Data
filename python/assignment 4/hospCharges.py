''' 
    Name: Matthew Chung
    Description: Assignment 4a calculating hospital charges
'''
    
def inpatient(name):
    days = int(raw_input("Please enter the amount of days the patient stayed in the hospital"))
    days = inp(days)
    dayRate = float(raw_input("Please enter the daily rate for this service"))
    dayRate = inp(dayRate)
    hospServices = float(raw_input("Please enter the charges for services(Xrays, lab tests, etc.): "))
    hospServices = inp(dayRate)
    medCharges = float(raw_input("Please enter the charges for medications: "))
    medCharges = inp(medCharges)
    total = days*dayRate + hospServices + medCharges
    print(name + " has a total bill in the amount of: $" + str(total))

def outpatient(name):
    hospServices = float(raw_input("Please enter the charges for services(Xrays, lab tests, etc.): "))
    hospServices = inp(hospServices)
    medCharges = float(raw_input("Please enter the charges for medications: "))
    medCharges = inp(medCharges)
    total = hospServices + medCharges
    print(name + " has a total bill in the amount of: $" + str(total))

def servValid(service):
    
    if (service == 'op') or (service == 'OP'):
        return "op"
    elif (service == 'ip') or (service == 'IP'):
        return "ip"
    else:
        service = raw_input("You have made an invaid selection for service type either 'IP' or 'OP'")
    
def inp(x):
    if x == 0:
        print("Zero is not an acceptable answer, please re-enter a value")
        x = float(raw_input("Please re-enter your value: "))
    return x
    
name = raw_input("Please enter the patient's name:")
service = raw_input("Please enter patient type, for Inpatient input 'IP' for Outpaient input 'OP'")
service = servValid(service);
if service == 'ip':
    inpatient(name)
else:
    outpatient(name)