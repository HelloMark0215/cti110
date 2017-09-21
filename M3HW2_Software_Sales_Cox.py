#CTI-110
#M3H2 - Software Sales
#William Cox
#20 September 2017

# This program will calculate bulk discounts based on the number of packages purchased.

def main():
# defining Raw values
    quantity = float(input( "please enter the number of packages bought: "))
    SoftwarePackage = 99
# next we define the discount amounts based upon how many packages purchased
    if quantity < 10:
        discount = 0;
    elif quantity < 20:
        discount = 0.1
    elif quantity < 50:
        discount = 0.2
    elif quantity < 100:
        discount = 0.3
    else:
        discount = 0.4
# Next we will provide totals based on bulk discounts

    Subtotal = SoftwarePackage * quantity
    DiscountAmount = discount * Subtotal
    Total = Subtotal - DiscountAmount
    
# below we are going to display the formatted amounts to the user

    
    print( "Amount of dicount: $" + format( DiscountAmount, ",.2f" ))
    print( "Total Amount: $" + format( Total, ",.2f" ))

main()


    
    

