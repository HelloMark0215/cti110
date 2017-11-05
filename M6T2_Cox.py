#CTI-110
#M6T2 - feet to inches
#William Cox
#5 November 2017

# constant for the numebr of inches per foot.
inches_per_foot = 12

#main function to create logic for the program
def main():
    #get number of feet from the user
    feet = int(input('Please Enter a distance in feet: '))

    # convert feet to inches
    print(feet, 'feet equals',feet_to_inches(feet), 'inches. ')
    
# feet to inches function converts feet to inches
def feet_to_inches(feet):
    return feet * inches_per_foot
    
    inches = feet_to_inches(1)
    
# last I will call the main function
main()

    
    
    
    
