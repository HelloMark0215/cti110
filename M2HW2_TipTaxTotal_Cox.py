#CTI-110
#M2H2 - Tip Tax Total
#William Cox
#26 August 2017

# This program is assuming an 18% Tip and 7% sales tax.

print ("Hello")

#variable one is requesting the user to enter the cost of his/her meal

mealcharge = float(input("please enter only the cost of your meal minus any tips or taxes $"))

# Variable two is calculating the amount of the tip

tip = .18 * mealcharge

# Variable three is calculating the sales tax for the meal

salestax = .07 * mealcharge

# Variable four is calculating the total for the meal
Total = mealcharge + salestax + tip

# next we will display the amount that the customer should pay for his/her tip
print ("Your waiter or waitress did a great job and has earned a tip in the amount of $" + format(tip, ",.2f") + ". Not bad for a job well done!")

#next we will display the amount of the sales tax
print ("Your state sales tax for this meal is $" + format(salestax, ",.2f") + ". Could be worse I suppose.")

#next we will display the total cost of the meal
print ("The total cost for your meal today is $" + format(Total, ",.2f") + ". Please come again soon!")








