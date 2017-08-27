#CTI-110
#M3T1_AreasOfRectangles
#William Cox
#27 August 2017

# This program asks for input on the length and width of two rectangles.
# The program will tell the user which rectangle has the greater area,
# or if the two rectangles have equal area.


#1st variable is the length of the 1st rectangle
rectangleonelength = int(input("What is the length of rectangle 1? "))

#2nd Variable is the width of the 1st rectangle
rectangleonewidth = int(input("What is the width of rectangle 1? "))
                    
#3rd Variable is the Area of the 1st rectangle
Areaofrectangleone = rectangleonelength * rectangleonewidth

#4th Variable is the length of the 2nd rectangle
rectangletwolength = int(input("What is the length of rectangle 2? "))

#5th Variable is the width of the 2nd rectangle
rectangletwowidth = int(input("What is the width of rectangle 2? "))

#6th Variable is the Area of the 2nd rectangle
Areaofrectangletwo = rectangletwolength * rectangletwowidth

if Areaofrectangleone > Areaofrectangletwo:
    print("The Area of rectangle one is bigger than the Area of Rectangle Two")
elif Areaofrectangletwo > Areaofrectangleone:
    print("The Area of rectangle two is bigger than the Area of rectangle one")
else:
    print("The Area of the two rectangles are equal")

print("\n")
print("The areas of each rectangle will be printed below")
print("the area of rectangle one is", Areaofrectangleone)
print("The area of rectangle two is", Areaofrectangletwo)



