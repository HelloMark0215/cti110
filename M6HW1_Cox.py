#CTI-110
#M6HW1
#William Cox
#12 November 2017

    
def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 +score5)/5
    return average

def determine_grade (userscore):
    if (userscore < 60):
         return "F"
    elif (userscore < 70):
         return "D"
    elif (userscore < 80):
         return "C"
    elif (userscore < 90):
         return "B"
    else:
        return "A"
# I had to create this function to ask for inputs because when I used this in main the other functions could no see them.
def ask_for_scores():
    score1 = float(input('Enter score 1: '))
    score2 = float(input('Enter score 2: '))
    score3 = float(input('Enter score 3: '))
    score4 = float(input('Enter score 4: '))
    score5 = float(input('Enter score 5: '))

    return score1, score2, score3, score4, score5

# define main.. I couldn't figure out how to make the main function ask for the inputs and relay those to other functions.  
def main():

    score1, score2, score3, score4, score5 = ask_for_scores()
    print()
    
    print("score \t Letter Grade")
    print(score1, "\t", determine_grade(score1))
    print(score2, "\t", determine_grade(score2))
    print(score3, "\t", determine_grade(score3))
    print(score4, "\t", determine_grade(score4))
    print(score5, "\t", determine_grade(score5))
    print()
    print("Your average is", calc_average(score1, score2, score3, score4, score5))

# call the main function    
main()



   
    

