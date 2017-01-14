# Project:      Calculation of MPH and loop process
# Name:         Bach Tran
# Date:         01/13/17
# Description:  MainA() will calculate MPH as Miles and Minutes typed in.
#               MainB() will print 2 number entered 6 times

#Define Main A
def MainA():
    print("This program will get miles and minutes travel then calculate MPH\n\n")
    # Getting Miles and Minutes travel
    fltMile = float(input("Type in traveled miles: "))
    fltMin = float(input("Type in traveled minutes: "))
    # Print out calculate MPH by Miles/(Minutes/60)
    print("You traveled",fltMile,"mile(s) in",fltMin,"""minute(s),
    You would have traveled""",round(fltMile/(fltMin/60),2),"MPH")

#Define Main B
def MainB():
    print("This program will get 2 numbers and then print out those 6 times\n\n")
    # Getting 2 numbers
    fltNum1 = input("Enter 1st number: ")
    fltNum2 = input("Enter 2nd number: ")
    # Print out 6 times with loops
    for i in range(6):
        print(fltNum1,"\t",fltNum2)

#call Main A and B
MainA()
MainB()


    