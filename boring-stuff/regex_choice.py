""" 
18/7/2022 This Program has regex_choice.py file
and allow users to input a number that may or may not have a negative at the first position or a float
and prints the number and tells them if it is invalid 

"""

import re #imports regex module

num_source = input('Enter a number like -12.34: ') #this variable stores the user inputs

find_num = re.compile(r"[-]?(\d*\.\d+|\d+)") #creates regular expression characters

new_match= find_num.match(num_source) #matches the user inputs with the regex created in the compile above

if new_match:
    print(f"Here is the number: {num_source}")
    
else:
    print("This is not a valid number")