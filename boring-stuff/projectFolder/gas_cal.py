"""
14/7/2022 This program has a gas_cal.py file that takes 
asks users to input the number of miles they drove, the number of gallons
they used and the price of each gallon and do some calculations based on that
and give them output

"""

miles = int(input("How many miles did you drove?: "))
gallons = int(input("How many gallons of gas did you use?: "))
price = float(input("How much was your gas per gallon?: "))

MPG = miles / gallons
Trip_cost = gallons * price

print("Here is some fun fact about your trip!")
print('{:<15}{:>5}'.format('MPG', MPG))
print('{:<15}{:>5}'.format('Trip_cost', Trip_cost))
