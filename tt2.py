#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    a = 5 * no_of_five
    b = 1 * no_of_one
    c = a + b
    five_needed = rupees_to_make // 5
    one_needed = rupees_to_make % 5
    if c >= rupees_to_make:
        if no_of_five >= five_needed & no_of_one >= one_needed:
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        else:
            print(-1)
    #Start writing your code here
    #Populate the variables: five_needed and one_needed


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    else:
        print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(11,5,11)
