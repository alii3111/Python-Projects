""" Yahya Muhumed 14/7/2022 this program summarizes cost of a list
of books, giving each book a number. """

import pyinputplus as pyip

print('This program summarizes a book list.')  # print intro


def main():  # call functions and save results under key variable names.
    try:  # generic exception handling - turn off during development
        num_books, price_list, title = inputs()
        total, average = processing(price_list)
        outputs(num_books, price_list, total, average, title)
        restart = input('Need more books? Enter y or n: ')  # restart feature
        if restart == 'y':
            print('OK, let\'s create a new list.')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:  # turn off during development
        print(err)  # turn off during development


def inputs():  # collect info needed from the user.
    print('Enter the number of books that you need ')  # user sets the list length/ repetitions of the for loop
    num_books = pyip.inputInt()  # call validation function to collect int > 0
    price_list = []  # create list to save prices
    for index in range(num_books):  # for loop runs user-specified number of times & collects info on each book
        title = input(f"Enter the name of book #{index +1}: ")
        print(f'Enter the cost of {title}, to the nearest dollar: ')
        book_cost = pyip.inputNum(allowRegexes=[r'($)+', r'zero'], max=100)  # call validation function to collect int > 0
        price_list.append(book_cost)  # build price list
    return num_books, price_list, title




def processing(price_list):  # use the list to calculate summary data
    total = sum(price_list)
    average = round(total / len(price_list), 2)
    return total, average


def outputs(num_books, price_list, total, average,title):  # display information about each book, and summary info
    print(f'Info on {num_books} Books Needed')
    print(f'{"Book #":<10}{"Price":>10}')
    for index in range(len(price_list)):
        print(f'{title}\t   ${price_list[index]:>8.2f}')
    print(f'{"Total":<10} ${total:>8.2f}')
    print(f'{"Average":<10} ${average:>8.2f}')


main()  # call main to start or restart program.