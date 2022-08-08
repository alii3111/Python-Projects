"""
14/7/2022 This program has a coffee_sales.py file that takes 
asks users to input the cups of drink sold and the price of that drink calculates
and give the total

"""

print("Drink sales for the reporting period.")

cups_of_coffee= int(input('How many cups of coffee sold? '))
price_of_coffee = float(input('Price of coffee? '))
coffee_sales = cups_of_coffee * price_of_coffee

cups_of_Tea_sold = int(input('How many cups of Tea sold? '))
price_of_Tea = float(input('Price of Tea? '))
Tea_sales = cups_of_Tea_sold * price_of_Tea

cups_of_Cuppoccino= int(input('How many cups of Cuppoccino sold? '))
price_of_cuppoccino= float(input('Price of Cuppoccino? '))
Cuppoccino_sales = cups_of_Cuppoccino * cups_of_Cuppoccino 

all_total =  (cups_of_coffee + cups_of_Tea_sold + price_of_cuppoccino)
total = coffee_sales + Tea_sales + Cuppoccino_sales

print('{:<14}{:>3}{:>10}{:>4}{:>10}{:>5}'.format('Drink Type', 'Cups Sold', '', 'Price', '', 'Total'))
print('{:<14}{:>5}{:>12}{:>5.2f}{:>14}{:>6.2f}'.format('Coffe', cups_of_coffee, '$', price_of_coffee, '$', coffee_sales))
print('{:<14}{:>5}{:>12}{:>5.2f}{:>14}{:>6,.2f}'.format('Tea', cups_of_Tea_sold, '$', price_of_Tea, '$', Tea_sales))
print('{:<14}{:>5}{:>12}{:>5.2f}{:>14}{:>6.2f}'.format('Cuppoccino', cups_of_Cuppoccino, '$', price_of_cuppoccino, '$', Cuppoccino_sales))
print('{:<9}{:>13.2f}{:>28}{:>7.2f}'.format( 'Total',  all_total, '$', total))
