#CTI-110
#M5H3 - Factorial
#William Cox
#17 October 2017


def main():
    
    n = int(input('Enter a nonnegative integer? '))
    fact = 1
    i = 2
    if n < 0:
        print ("sorry you must inter a nonnegative number")
    else:
        while i <= n:
            fact = fact * i
            i = i + 1
        print ("The factorial of", n , "is" ,fact)
    
main()
    
    
