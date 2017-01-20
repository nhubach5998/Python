# Project:      
# Name:         Bach Tran
# Date:         
# Description:  
# 
# 
#10.50 a pound + shipping
#shipping = 0.86/lb + 1.5
#enter pound and get price
def CostOfCoffee():
    fltPounds = float(input("Enter the desired amount of coffee (in lbs): "))
    fltCost = 10.50 * fltPounds
    fltShippingCost = 0.86 * fltPounds + 1.50
    fltTotal = fltCost + fltShippingCost
    print("""Subtotal : ${0:0.2f}
    Shipping : ${1:0.2f}
    Total : ${2:<}""".format(fltCost,fltShippingCost,fltTotal))

CostOfCoffee()
