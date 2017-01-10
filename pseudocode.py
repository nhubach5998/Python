#Bach Tran
#Project: Calculate cost per square inch of pizza
#define function main()
def main():
    r=float(input("Type in the size (diameter) "))/2    #Getting the size
    cost=float(input("Type in the price "))             #Getting price (USD)
    area=r**2*3.14                                      #Calculate area of the pizza  
    cost_inch=cost/area                                 #Calculate the cost per square inch
    print("The cost per square inch of the",r*2,"inch(es) pizza with the price of",cost,"is ",cost_inch)
main()