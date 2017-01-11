#Bach Tran
#Project: Calculate cost per square inch of pizza, breakdown change,

#define function main()
def main():
    squareinchpizza()    #the pizza
    print("\n\n\n\n\n")     #separating program
    breakdownchange()    #the change
    print("\n\n\n\n\n")     #separating program
    booksale()           #the book
    
#function to check if the input was correct type
def checkinput(outtype,str):
    while True: #infinite loop ask to enter correct type of variable
        inputvalue=input(str)
        try:
            #this is for checking which type of variable do i want to check
            if outtype=='float':
                inputvalue=float(inputvalue)
            elif outtype=='int':
                inputvalue=int(inputvalue)
            return inputvalue
        #wrong input type will result this
        except ValueError:
            print("This is not a number")

#function to calculate price per square inch of a pizza
def squareinchpizza():
    print("This is a program to calculate the price per inch square of a pizza")
    r=checkinput(str="Type in the size (diameter) ",outtype="float")/2           #Getting the size
    cost=round(checkinput(str="Type in the price ",outtype="float"),2)           #Getting price (USD)
    area=r**2*3.14                #Calculate area of the pizza  
    cost_inch=cost/area           #Calculate the cost per square inch
    #print out the result
    print("The cost per square inch of the",r*2,"inch(es) pizza with the price of",cost,"is $",round(cost_inch,2)) 

#functiopn to breakdown to change    
def breakdownchange():
    print("This is a program to calculate the change out of cash")
    cash=round(checkinput(str="Please enter the amount you want to break down.(The amount will be rounded to nearest 0.01!!!)\n",outtype="float"),2)    #Asking for the amount
    print("You entered: $",cash)    #This step to reprint the entered amount to clarify
    q=breakdown(cash,0.25);     cash=round(cash-q*0.25,2);print(q,"\t",cash)   #Break to quarters, then calculate the amount left
    d=breakdown(cash,0.1);      cash=round(cash-d*0.1,2);print(d,"\t",cash)   #Break to dimes, then calculate the amount left
    n=breakdown(cash,0.05);     cash=round(cash-n*0.05,2);print(n,"\t",cash)   #Break to nickel, then calculate the amount left
    p=breakdown(cash,0.01);     cash=round(cash-p*0.01,2);print(p,"\t",cash)   #Break to pennies, then calculate the amount left
    #print out result
    print("With $",round(q*0.25+d*0.1+n*0.05+p*0.01,2),"We will have:\n",q,"Quarters\n",d,"Dimes\n",n,"Nickels\n",p,"Pennies\n")
    #i use round to avoid weird calculation

#A function to breakdown cash
def breakdown(cash,value):
    return int(round(cash-round(cash%value,2),2)/value)

#function to display booksale and its total price
def booksale():
    print("This is a program to calculate and display book sale")
    Name=input("Please enter the name of the book: ") #asking book's name
    while True:     #infite loop asking proper quantity (avoid negative quantity)
        Quan=checkinput(str="Enter the quantity of the book: ",outtype="int")
        if Quan>0:
            break
        else:
            print("Invalid quantity!!!")
    Price=round(checkinput("float","Enter the price of the book: "),2)
    Subtotal=round(Price*Quan,2)
    Tax=round(Subtotal*3/100,2)
    print("\n\n\n",\
    Name,"\tPrice $",Price,"\tX\t",Quan,"(Quantity)\n\n\n\
    \t\t\tSubtotal\t\t$",Subtotal,"\n\
    \t\t\tTax(3%)\t\t$",Tax,"\n\
    \t\t\tTotal\t\t$",round(Subtotal+Tax,2))

#call main
main()
