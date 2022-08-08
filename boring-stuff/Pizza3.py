"""2/8/2022 This program has a Pizza1.py that takes the user inputs calculating the
cost of pizza and the add-ons the user wants. The user can choose the size of pizza and all
the toppings the user wants and the program calculates all the user inputs and display the price of each input 
and the total."""

import pyinputplus as pyip

def main():
    try:
        print("Welcome to Yaya's Pizza Menu")
        num_pizza, pizzaSizePrice,cheesePrice, proteinPrice, olivePrice, pepperPrice, mushroomPrice,userPizzaSize,userCheese,userProtein,userOlive,userPeppers,userMushrooms,pizzaSizePrice,cheesePrice,proteinPrice,olivePrice,pepperPrice,mushroomPrice = inputs()
        Total = processing(pizzaSizePrice,cheesePrice, proteinPrice, olivePrice, pepperPrice, mushroomPrice)
        outputs(num_pizza, userPizzaSize,userCheese,userProtein,userOlive,userPeppers,userMushrooms,pizzaSizePrice,cheesePrice,proteinPrice,olivePrice,pepperPrice,mushroomPrice,Total)
        
    except Exception as err:
        print(err)
        
def inputs():
    try:
        print("How many pizza would you like to order? ")
        num_pizza = get_pos_int()  # call validation function to collect int > 0
        for index in range(num_pizza):  # for loop runs user-specified number of times & collects info on each book
            print("You can choose a pizza size followed by a list of optional toppings")
     
            pizzaSize =pyip.inputMenu(['S', 'M', 'L'], prompt = f"#{index +1} What size would like to order?. S/M/L are the options: \n")
            pizzaSize = pizzaSize.upper()#converts the pizza size input to uppercase
            #stores the size of pizza in a variable
            userPizzaSize = ''
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
                
                userCheese = ''
                if cheeseOption=='C':
                    userCheese ='chedder'
                    cheesePrice=5.75
                elif cheeseOption =='P':
                    userCheese ='Pepper'
                    cheesePrice=3.45
                elif cheeseOption=='S':
                    userCheese= 'Swiss'
                    cheesePrice=7.25
            elif cheese=='NO':
                userCheese='cheese'
                cheesePrice=0.00
                

            protein =pyip.inputYesNo("Would you like protein? Y/N: ")
            protein = protein.upper()#converts protein input to uppercase
            if protein =='YES': 
                print("chose from the following protein options: ")
                proteinOption = pyip.inputMenu(['C','T', 'S'], prompt= 'please enter C/c for chicken , T/t for Tofu, S/s for Shrimp \n')
                proteinOption = proteinOption.upper()#converts protein option input to uppercase
                
                userProtein = ''#stores the type of protein in a variable
                if proteinOption=='C':
                    userProtein ='chicken'
                    proteinPrice=4.75
                elif proteinOption =='T':
                    userProtein ='Tofu'
                    proteinPrice=2.65
                elif proteinOption=='S':
                    userProtein= 'Shrimp'
                    proteinPrice=3.00
                    
            elif protein=='NO':
                userProtein='protein'
                proteinPrice=0.00
                


            olive = pyip.inputYesNo("Would you like olives? Y/N")
            olive = olive.upper()#converts the user olive input to uppercase.

            userOlive =''
            if olive == 'YES':
                userOlive='olives' 
                olivePrice=2.50

            elif olive=='NO':
                userOlive='olives'
                olivePrice=0.00
                


            peppers = pyip.inputYesNo("Would you like peppers? Y/N")
            peppers = peppers.upper()#converts the user peppers input to uppercase.

            userPeppers=''
            if peppers == 'YES':
                userPeppers='peppers' 
                pepperPrice=3.80

            elif peppers =='NO':
                userPeppers='peppers'
                pepperPrice=0.00


            mushrooms = pyip.inputYesNo("Would you like mushrooms? Y/N")
            mushrooms = mushrooms.upper()#converts the user mushrooms input to uppercase.
            userMushrooms=''
            if mushrooms == 'YES':
                userMushrooms='mushrooms' 
                mushroomPrice=1.50

            elif mushrooms =='NO':
                userMushrooms='mushrooms'
                mushroomPrice=0.00
                
        return num_pizza, pizzaSizePrice,cheesePrice, proteinPrice, olivePrice, pepperPrice, mushroomPrice,userPizzaSize,userCheese,userProtein,userOlive,userPeppers,userMushrooms,pizzaSizePrice,cheesePrice,proteinPrice,olivePrice,pepperPrice,mushroomPrice
    except Exception as err:
        print(err)
 
def get_pos_int():  # collect and validate an int > 0
    pos_int = input('Please enter a whole number: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int
        
def processing(pizzaSizePrice,cheesePrice, proteinPrice, olivePrice, pepperPrice, mushroomPrice):
    #adding the total price of inputs
    Total =pizzaSizePrice + cheesePrice + proteinPrice + olivePrice + pepperPrice + mushroomPrice
    return Total

def outputs(num_pizza, userPizzaSize,userCheese,userProtein,userOlive,userPeppers,userMushrooms,pizzaSizePrice,cheesePrice,proteinPrice,olivePrice,pepperPrice,mushroomPrice,Total):
    print(f"Here is your {num_pizza} pizza order")
    total = 0#initializing total 
    for index in range(num_pizza):#looping through number of pizzas
        print('#',index+1)
        
        print(f'{userPizzaSize} .....$.{pizzaSizePrice:<8.2f}')
        print(f'{userCheese} ........$.{cheesePrice:<8.2f} ')
        print(f'{userProtein} .......$.{proteinPrice:<8.2f}')
        print(f'{userOlive} .........$.{olivePrice:<8.2f}')
        print(f'{userPeppers} .......$.{pepperPrice:<8.2f}')
        print(f'{userMushrooms} .....$.{mushroomPrice:<8.2f}')
        print(f'{"Pizza total"}......${Total:<8.2f}\n')
        total+=Total
        
    print(f'Grand total for {index+1} pizzas: ${total}\n')
    print("Thanks for ordering pizza!\n")

main()