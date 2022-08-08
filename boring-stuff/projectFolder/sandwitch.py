"""
 22/7/2022 This program asks the user on several
inputs and validates them using pyinputplus module

"""

import pyinputplus as pyip

def main():  
    
    breadType =['wheat', 'white', 'sourdough']
    pyip.inputMenu(breadType, "What type of bread do you want: \n")
    proteinType =['chicken', 'turkey', 'ham', 'tofu']
    pyip.inputMenu(proteinType, "What type of protein do you want: \n")
    response = pyip.inputYesNo("Do you want a cheese, type yes/no: ")
    if response =='no':
        print('Thanks for using my program')
        quit()
    cheeseType = ['cheddar', 'Swiss', 'mozzarella']
    pyip.inputMenu(cheeseType, "What type of cheese do you want: \n")
    pyip.inputYesNo('Do you want mayo?: ')
    pyip.inputYesNo('Do you want Swiss?: ')
    pyip.inputYesNo('Do you want mozzarella?: ')
    print("How many sandwitches do you want?: ")
    pyip.inputNum(greaterThan=1)
    quit()

main()