#CTI-110
#M5T2 - Bug Collector
#William Cox
#18 October 2017


def main():
    
#this is my accumulator
    totalbugs = 0
# Range goes up to upper limit but does no include it
    for day in range(1, 8):
        print("enter the bugs collected on day", day)
        bugs = int(input())
        totalbugs += bugs
    print("you collected a total of", totalbugs, "bugs")

    
main()
    
    
