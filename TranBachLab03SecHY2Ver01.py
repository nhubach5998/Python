# Project:      Calculate price and shipping for coffee
#               and Calculate saving amount needed before retired
# Name:         Bach Tran
# Date:         01/23/2017
# Description:  CostOfCoffee() to calculate coffee cost and shipping cost
#               SavingCalculate() to calculate amount needed monthly to have 1125000 before 68


def CostOfCoffee():
    # Define variables fltPounds is amount coffee need to be entered
    fltPounds = float(input("Enter the desired amount of coffee (in lbs): "))
    # Calculate total and shipping cost
    fltCost = 10.50 * fltPounds
    fltShippingCost = 0.86 * fltPounds + 1.50
    fltTotal = fltCost + fltShippingCost
    # Print out result
    print("\nSubtotal : ${0:0.2f}\n\
    \rShipping : ${1:0.2f}\n\
    \rTotal : ${2:0.2f}\n\n".format(fltCost,fltShippingCost,fltTotal))

CostOfCoffee()

def SavingCalculate():
    # Define variables
    intAge = int(input("Enter current age: "))
    fltSavingAmount = float(input("Enter current amount in your saving account: "))
    # Calculate month left until 68 years old (excluding the birth month case)
    intMonthLeft = (68 - intAge) * 12
    fltSavingAmountLeft = 1125000 - fltSavingAmount
    # Print out result
    print("\n\nYou are {0} years old and you have $ {1} in your saving account.\n\
    \rYou will need to put $ {2:0.2f} into your saving account monthly\n\
    \rto have $ 1,125,000.00 before age of 68\n\n".format(intAge,fltSavingAmount,fltSavingAmountLeft/intMonthLeft))

SavingCalculate()

