"""
Yahya Muhumed 14/7/2022 This program has if-1.py file that checks whether the user input is 
more, less or equal to one dollar
"""

pennies = input("Enter the number of pennies in the jar: ")
if pennies.isnumeric() is False:
    print('Try the program again; it only takes whole numbers.')

else:
    pennies = int(pennies)
    if pennies > 1:
        p_n = "${:.2f}".format(pennies)
        print("You have more than a dollar")
        print(f'you have {p_n} to be exact')
        print("That's all folks")
    elif pennies < 1:
         print("You have less than a dollar")
         print("That's all folks")
        

    else:
     print("You exactly one dollar")
        
    