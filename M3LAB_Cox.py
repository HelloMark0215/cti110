#CTI-110
#M3LAB - Debugging
#William Cox
#8 September 2017

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses the 10-point grading scale
    
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    
    
    score = float(input('Enter grade: '))

    if score >= A_score:
         print('Your grade is: A')
    elif score >= B_score:
         print('Your grade is: B')
    elif score >= C_score:
         print('Your grade is: C')
    elif score >= D_score:
         print('Your grade is: D')
    else:
        print('Your grade is: F')


# program start
main()

