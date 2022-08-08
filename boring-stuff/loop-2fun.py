""" Yahya Muhumed 6/13/2019 This counting program allows the user to determine
a start and stop number for our range function. It displays each number
counted, adds each digit to the next & displays the results """

def main():

    # greet the user
    print('Welcome to our counting program.')
    print('It also adds up the digits that you count!')
    start_num, stop_num = inputs()
    total = processing(start_num, stop_num)
    outputs(total)

def inputs():

    # collect user's start number for the counting game
    print('Please enter a small number, 0 or higher')
    start_num = get_pos_int()
    print('Now, enter a larger number that you want to count up to')
    stop_num = get_pos_int() 
    return start_num, stop_num

def get_pos_int():  # collect and validate an int > 0
    pos_int = input('Please enter a whole number: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int


def processing(start_num, stop_num ):
    # run counting program, based on user start and stop number
    total = 0  # initialize an accumulator
    for number in range(start_num, stop_num +1):
        print(number)
        total += number # shorthand for total = total + number
    return total

def outputs(total):
    # display the total accumulated in a sentence
    print(f'The total of all the numbers you counted is: {total:,d}.')


main()