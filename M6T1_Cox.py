#CTI-110
#M6T1 - Kilometer Converter
#William Cox
#26 October 2017

CONVERSION_FACTOR = 0.6214

# The main function requests the user
# to input the distance in Kilometers and calls
# the show_miles function to convert it

def main():
    
    # ask for the Kilometers to convert
    kilometers = float(input(" Enter a distance in kilometers: "))
    
    # Display the distance converted to miles.
    show_miles(kilometers)

# The show_miles function converts the parameter km from
# kilometers to miles and displays the result.
def show_miles(km):
    # calculate miles.
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print(km, "kilometers equals", miles, "miles.")
    

# last I have to call the main function    
main()
    
    
