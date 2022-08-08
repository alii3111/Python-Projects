"""
14/7/2022 This program has area.py file 
that calculate the area of a rectangle by taking user inputs i.e length, width

"""

print("Welcome to the Rectangle Area Calculator!")
unit = input("What is your measurement in unit (in., ft., cm., etc).? ")
length = int(input(f"What is the length of the rectangle in {unit}? "))
width = int(input(f"What is the width of the rectangle in {unit}? "))

Area = length * width

print(f'Your rectangle is {Area} square units')