# Project:      Draw triangle X (EXTR01)
# Name:         Bach Tran
# Date:         01/23/2017
# Description:  Enter the height and program draw a triangle
def TriangleX():
    # Using 2 loop
    # 1st one go through height
    # 2nd one draw X
    for i in range(1,int(input("Enter height of the triangle: "))+1):
        for j in range(i):
            print("X",end="")
        print(end="\n")

TriangleX()
