"""
14/7/2022 This program has sale_tax.py 
that calculate the tax of sales
"""


Po_amount = input("What is the total price of your purchase order? $")
state_tax = 5/100 * float(Po_amount)
county_tax = 2.5/100 * float(Po_amount)
Total = float(Po_amount) + state_tax + county_tax
print("Custom Delivery Sales Receipt")

print('{:<14}{:>5}{:>12}'.format('PO Amount', '$', Po_amount,))
print('{:<14}{:>5}{:>12}'.format('State Tax', '$', state_tax))
print('{:<14}{:>5}{:>12}'.format('County Tax',  '$', county_tax,))
print('{:<14}{:>5}{:>12}'.format('Total Cost', '$', Total))
