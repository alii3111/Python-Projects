""" 1/8/2022 This program contains dictionary_file.py. it uses a logic that allows user to select

a choice command from inputMenu """

import pyinputplus as pyip

def main():
    try:
        display_menu()
        #opens a txt file in a write mode
        myFile = open('test.txt', 'w')
        #writes content to the file
        myFile.write('mouse mickeymouse@gmail.com \n')
        myFile.close()
        while True:
            command = pyip.inputMenu(['view', 'add', 'exit'])
            command = command.lower()
            if command == 'view':
                myFile = open('test.txt', 'r')
                 #reads the test.txt file
                my_data = myFile.read()
                print(my_data)
                #Close the test.txt file
                myFile.close()
            elif command == 'add':
                print('You have chosen to add username & email to the directory \n Use this format ...')
                print('(username email@address.com,username email@address.com \n Seperate each new contact\'s entry with a coma.) dduck donaldduck@gmail.com,rrunner roadrunner@gmail.com')
                #Take input from user and assign it to variables
                print("Enter the user contacts?")
                UserInput =input()
                
                #Open the test.txt file for appending.
                file1 = open('test.txt', 'a+')
                
                #Write the content of the variables to the test.txt file
                file1.write(UserInput +'\n')
                
                #Close the test.txt file
                file1.close()
                                
            elif command == 'exit':
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')


def display_menu():
    print('COMMAND MENU')
    print('view - username/email file')
    print('add - Add username()s /email(s) to the file')
    print('exit - Exit program')
    



if __name__ == '__main__':
    main()

