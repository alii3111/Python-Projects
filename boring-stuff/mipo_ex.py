""" 14/7/2022 this program figures volume of a rectangular
 solid, but more importantly, it provides a model of functions
 talking to each other, int validation, exception handling and restart """

print('This program calculates the volume of a box. ')

def main():
    try:
        length, width, height = inputs()
        volume = processing(length, width, height)
        outputs(volume)
        restart = input('Continue? Enter y or n: ')
        if restart == 'y':
            print('OK, let\'s calculate volume of another box.')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:

        print(err)

def inputs():
    print('What\'s the length of the box? ')
    length = get_pos_int()
    print('What\'s the width? ')
    width = get_pos_int()
    print('What\'s the height? ')
    height = get_pos_int()
    return length, width, height

def get_pos_int():
    pos_int = input('Please enter a whole number: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a whole number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int

def processing(length, width, height):
    volume = length * width * height
    return volume

def outputs(volume):
    print(f'The volume of the object is: {volume} cubic units.' )

main()