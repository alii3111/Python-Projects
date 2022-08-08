"""
14/7/2022 This program has color_mixer.py file that mixes 
2 different colors and produce a result as another color i.e red and blue makes purple.

"""
from logging import exception


print("What happens when you mix 2 different primary colors?")
primary_color = input("Enter a primary color - red, yellow or blue: ")

try: 

    second_color =input('Enter a 2nd primary color, not the same as the first: ')
    if second_color == primary_color:
        input("select a different primary color for color 2: ")
    elif primary_color == 'red' and second_color == 'blue' or primary_color == 'blue' and second_color == 'red':
        print('Nice! Red and blue makes purple!')
        print('Thanks for using the program') 
    elif primary_color =='red' and second_color == 'yellow' or primary_color =='yellow' and second_color == 'red':
        print('Red and yellow makes orange')
        print('Thanks for using the program')
    
except exception:
    print("Please enter the word red, yellow or blue only:")