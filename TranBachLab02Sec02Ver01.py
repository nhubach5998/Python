# Project:          Program print out 0-9, 1-10, 0-19 (TranBachLab02Sec01Ver01.py)
# Name:             Bach Tran
# Date:             01/17/17
# Description:      This program will print out 0-9, 1-10, 0-9 10-19 in 2 column

#Define the function main
def main():
    # Create a program that uses a loop to print out the numbers 0-9.
    print("This is series from 0 to 9:")
    for i in range(10):
        print(i,end=" ")
    # Then add another loop that prints out the numbers 1-10.
    print("\nThis is series from 1 to 10:")
    for i in range(1,11):
        print(i,end=" ")
    # Then add some more code to print out the numbers 0-9 in one column and the numbers 10-19 in a column next to it
    print("\nThis is series print out 2 column from 0-9 and 10-19:")
    for i in range(10):
        print(i,"\t|\t",i+10)

# Call main
main()
