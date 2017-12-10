#CTI-110
#M6HW2 - Guessing Game
#William Cox
#12 November 2017

# Import the Random Function
import random

def main():
    guessesTaken = 0
    myName = input("Hello! What is your name?: ")

    number = random.randint(1, 100)
    print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')



    while guessesTaken < 10:
        guess = int(input('Take a guess: '))
        guessesTaken = guessesTaken + 1
        if guess < number:
            print('Your guess is too low.') 
        if guess > number:
            print('Your guess is too high.')
        if guess == number:
            break
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Great job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    else :
        guess != number
        number = str(number)
        print('Sorry, ' +myName + ' You failed to guess in your Ten attempts. The number I was thinking of was ' + number)

main()

playagain = input("would you like to play again? y/n: ")

if playagain == "yes" or "YES" or "y" or "Y":
    main()
else:
    print ("Ok thank you for playing")


