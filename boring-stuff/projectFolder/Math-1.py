"""
14/7/2022 This program has Math.py file 
that uses math function to evaluate some numbers using math functions
"""

import math

print("Here are some fun math fact ...")
A = 7.89
B = 54.345395
C = math.sqrt(2)
D = math.sin(7)
E = math.pi


print(f'{A} with decimal cutt of = ' , math.floor(A)) # cut off 7.89 to 7

print(f'{B} rounded to 3 decimal places = ' , float("{0:.3f}".format(B))) # round 54.345395 to 54.345

print(f"The square of 2 = {C}") # calculate the square root of 2

print(f"The sin of 7 = {D}") # calculate the sin of 7

print(f"The Value of pi = {E}")  # display the value of pi

print('The value of pi rounded to 3 decimal places = ' , float("{0:.3f}".format(E))) # display pi rounded to 3 decimal places
