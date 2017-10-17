#CTI-110
#M5H2 - Running Total Loop
#William Cox
#16 October 2017


def main():

# accumulator is going to start with 0 
    runningtotal = 0
    number = 0
# each time a number is greater than 0 it will ask for a new number
# each time a new positive number is entered it will be added to the total
# as soon as a negative number is entered the loop is ended

    while number >= 0:
        number = int(input( "Enter a number? " ))
        if number >= 0: runningtotal += number
    if number < 0:
        print("Total: " ,runningtotal)
    
main()
    
    
