#CTI-110
#M5H1 - Distance Traveled Loop
#William Cox
#13 October 2017


def main():

# Assuming no delay, the distance that a car travels down the interstate can be calculated with the following formula:
# Distance = Speed * Time

#variable one is the speed traveled
    speed = int(input( "What is the speed of the vehicle in MPH? "))

# Variable two is number of hours traveled
    hourstraveled = int(input("How many hours has it traveled? "))


# I am starting with 1 hour becasue at 0 hours the distance would be 0 miles
    hours = 1

# This variable is required for the inital value of the loop
    distance = speed * hours

    print( '\n' + "Hour" + '\t' + " Distance Traveled" + '\n' + "-------------------------" )  

    while hours <= hourstraveled:
        print (hours , '\t' ,  distance,)
        hours = hours + 1
        distance = speed * hours
    
main()
    
    
