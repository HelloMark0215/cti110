#CTI-110
#M3H1 - Age Classifier
#William Cox
#8 September 2017

# This program is going to Tell us a persons age classification based on the users input.

age = float(input("Please enter a persons age: " ))

#If the person is 1 year old or less, he or she is an infant.
if age <= 1:
    print("This person is an infant")
#If the person is older than one year, but younger than 13 years, he or she is a child
elif age < 13:
    print("This person is a child")
#If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
elif age < 20:
    print("This person is a teenager")
#If the person is at least 20 years old, he or she is an adult.
elif age >= 20:
    print("This person is an adult")


    
    

