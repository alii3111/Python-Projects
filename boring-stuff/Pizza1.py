"""2/8/2022 This program has a Pizza1.py that takes the user inputs calculating the
cost of pizza and the add-ons the user wants. The user can choose the size of pizza and all
the toppings the user wants and the program calculates all the user inputs and display the price of each input 
and the total."""

import pyinputplus as pyip

print("Welcome to Yaya's Pizza Menu")
print("You can choose a pizza size followed by a list of optional toppings")

pizzaSize =pyip.inputMenu(['S', 'M', 'L'], prompt = 'What size would like to order?. S/M/L are the options: \n')
pizzaSize = pizzaSize.upper()#converts the pizza size input to uppercase
userPizzaSize = ''#Initializing a variable for the pizza size
if pizzaSize == 'S':
    userPizzaSize = 'Small pizza'
    pizzaSizePrice = 9.75
elif pizzaSize == 'L':
    userPizzaSize = 'Large pizza'
    pizzaSizePrice = 16.75
elif pizzaSize == 'M':
    userPizzaSize = 'Medium pizza'
    pizzaSizePrice = 11.75
    
print("what toppings would you like to add in order to customize your pizza?")
print("Enter Y or N(yes or no) in the following options:")
cheese =pyip.inputYesNo("Would you like cheese? Y/N: ")
cheese = cheese.upper()#converts cheese input to uppercase
print(cheese)
if cheese =='YES': 
    print("chose from the following cheese options: ")
    cheeseOption = pyip.inputMenu(['C','P', 'S'], prompt= 'please enter C/c for chedder , P/p for PePepperpper Jack, S/s for Swiss \n')
    cheeseOption = cheeseOption.upper()#converts cheese option input to uppercase
    cheesePrice=5.75
    userCheese = ''#Initializing a variable for the cheese type
    if cheeseOption=='C':
        userCheese ='chedder'
    elif cheeseOption =='P':
        userCheese ='Pepper'
    elif cheeseOption=='S':
        userCheese= 'Swiss'
elif cheese=='NO':
    userCheese='Swiss'
    cheesePrice=0.00

protein =pyip.inputYesNo("Would you like protein? Y/N: ")
protein = protein.upper()#converts protein input to uppercase
if protein =='YES': 
    print("chose from the following protein options: ")
    proteinOption = pyip.inputMenu(['C','T', 'S'], prompt= 'please enter C/c for chicken , T/t for Tofu, S/s for Shrimp \n')
    proteinOption = proteinOption.upper()#converts protein option input to uppercase
    userProtein = ''#Initializing a variable for the protein type
    if proteinOption=='C':
        userProtein ='chicken'
        proteinPrice=4.75
    elif proteinOption =='T':
        userProtein ='Tofu'
        proteinPrice=5.75
    elif proteinOption=='S':
        userProtein= 'Shrimp'
        proteinPrice=3.25
        
elif protein=='NO':
    userProtein='Shrimp'
    proteinPrice=0.00


olive = pyip.inputYesNo("Would you like olives? Y/N")
olive = olive.upper()

userOlive =''#Initializing a variable for the olive 
if olive == 'YES':
    userOlive='olives' 
    olivePrice=2.50

elif olive=='NO':
    userOlive='olives'
    olivePrice=0.00


peppers = pyip.inputYesNo("Would you like peppers? Y/N")
peppers = peppers.upper()
userPeppers=''#Initializing a variable for peppers
if peppers == 'YES':
    userPeppers='peppers' 
    pepperPrice=3.70

elif peppers =='NO':
    userPeppers='peppers'
    pepperPrice=0.00


mushrooms = pyip.inputYesNo("Would you like mushrooms? Y/N")
mushrooms = mushrooms.upper()
userMushrooms=''#Initializing a variable for mushrooms
if mushrooms == 'YES':
    userMushrooms='mushrooms' 
    mushroomPrice=1.50

elif mushrooms =='NO':
    userMushrooms='mushrooms'
    mushroomPrice=0.00

#adding the total price of inputs
Total =pizzaSizePrice + cheesePrice + proteinPrice + olivePrice + pepperPrice + mushroomPrice

#printing the outputs of the user
print("Here is your pizza order")
print(f'{userPizzaSize} .....$.{pizzaSizePrice}')
print(f'{userCheese} .....$.{cheesePrice} ')
print(f'{userProtein} .....$.{proteinPrice}')
print(f'{userOlive} .....$.{olivePrice}')
print(f'{userPeppers} .....$.{pepperPrice}')
print(f'{userMushrooms} .....$.{mushroomPrice}\n')

print(f'{"Pizza total":<10} ${Total:<8.2f}')