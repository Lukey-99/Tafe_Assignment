# Work From Home Tracker

# create array with 7 employees
# 

employees = ["Employee 1", "Employee 2", "Employee 3", "Employee 4", "Employee 5", "Employee 6", "Employee 7"] #Lists employees $eID
employeeID = [(), (), (), (), (),(), ()]
daily1 = [(), (), (), (), ()] # hours worked each day per Employee $
weekly1 = [(), (), (), (), ()] # hours worked each week per Employee $
DOW = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] # days of week $
weekNum = 0
login = ""
eID = 0
choice = ""

def ShowHours():
    print(employees)
    print(str(employeeID))
    print(str(daily1))
    print(str(weekly1))

# how to make it so you cannot input the same EmployeeID twice.
# how to fix if no input was entered for employeeID
def Create():
    eID = 0
    while eID < 7: 
        while True:
            employeeID[eID] = input("Please enter your EmployeeID: ")
            if int(employeeID[eID]) <= 0:
                print("Your employeeID cannot be less than 1")
                continue
            elif int(employeeID[eID]) > 7:
                print("Your employeeID cannot be more than 7")
                continue
            #elif not employeeID[eID]:
                print("You didnt input an appropriate number")
            else:
                #int(weekNum) #why must this be for for "weekNum = input("What week are you entering this data into?: ")" to be reconised?
                break
        #int(weekNum) #refereced before assignment????? 
        weekNum = input("What week are you entering this data into?: ") # either isn't seen or has error (referenced before assignment)  #weekNum blank
        employees[eID] = input("Please enter your first and last name: ") # why does this line get seen and work but one before it doesn't???
        y = 0
        while y < 5:
            while True:
                daily1[y] = input("How many hours did you work in " + DOW[y] + ": ")
                if int(daily1[y]) <= 0:
                    print("you cannot have less or equal to 0 working hours in a day")
                    continue
                elif int(daily1[y]) > 24:
                    print("You cannot have more than 24 working hours in a day")
                    continue
                #elif daily1[y] == '':
                    print("You didnt input an appropriate number")
                else:
                    break
            y = y + 1
            continue 
        eID = eID + 1
        choice = input("Would you like to input another person? y/n: ")
        if choice == "yes" or choice == "Yes" or choice == "y" or choice == "Y":
            continue
        else:
            ShowHours()
            break

#FIX PLEASE 
def loginID():
    r = 0
    choice = input("Would you like to login using an EmployeeID? y/n: ")
    if choice == "yes" or choice == "Yes" or choice == "y" or choice == "Y":
        while True:
            login = input("Whose data do you want to input? Please input EmployeeID: ")
            if int(login) <= 0:
                print("Your employeeID cannot be less than 1")
                continue
            elif int(login) > 7:
                print("your employeeID cannot be more than 7")
                continue
            else:
                break
    else:
        print("Okay please create an account")
        Create()

    while r <= len(employeeID): #please fix this line. "UnboundLocalError: local variable 'employeeID' referenced before assignmnet"
        if login == int(employeeID[r]):
            print("You have logged into" + str(employeeID[r]))
            ShowHours()
        else:
            print("This account has not been created yet, please create an account")
            employeeID = login
            Create()
        r = r + 1

choice = ""
while choice == "":
    choice = input("What would you like to do? Create or Login: ")
    if choice == "Create" or choice == "create":
        Create()
        break
    elif choice == "Login" or choice == "login":
        loginID()
        break
    else:
        print("Please input either 'Create' or 'Login'")
        choice = ""
        continue

total = 0
int(total)
for ele in range(0, len(daily1)):
    total = total + int(daily1[ele])
print("You have worked: " + str(total) + " hours in week" + str(weekNum))

a = 0
        #figure out why it worked until thursday. (stops at "correct amount of hours")
while a < 6: # hours worked each day
    if int(daily1[a]) < 4: #Hours worked too much/too little
        print("Insufficient hours worked on " + DOW[a])
        a = a + 1
    elif int(daily1[a]) > 10:
        print("Too many hours worked on " + DOW[a])
        a = a + 1
    elif 4 < int(daily1[a]) and int(daily1[a]) < 10:
        print("You have worked the right amount of hours on " + DOW[a])
        a = a + 1
    else:
        break

#hours worked each week
if int(total) < 30:
    print("You didn't do enough work this week")
elif int(total) > 40:
    print("You are working too hard!!")
elif 30 < int(total) and int(total) < 40:
    print("You have worked the right amount of hours this week")

k = 0
csv = input("would you like to view the data in a differnet perspective? y/n: ")
if csv == "y" or csv == "Y" or csv == "Yes" or csv == "yes":
    while k < 7:
        print("Week " + str(weekNum) + ", " + str(employeeID[k]) + ", " + employees[k] + ", " + str(daily1[0]) + ", " + str(daily1[1]) + ", " + str(daily1[2]) + ", " + str(daily1[3]) + ", " + str(daily1[4]) + ", " + str(daily1[5]) + ", " + str(daily1[6]))
        k = k + 1
        continue
print("okay enjoy your day")