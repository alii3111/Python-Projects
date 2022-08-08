""" 25/7/2022 This program has dictionary_file.py 
  it uses a file format that enables a user to read and append files

"""
def main():
    try:
        countries = {'CA': 'Canada', 'US': 'United States', 'MX': 'Mexico'}
        display_menu()
        while True:
            command = input('Command: ')
            command = command.lower()
            if command == 'view':
                view(countries)
            elif command == 'add':
                add(countries)
           
            elif command == 'exit':
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n')
            
            
    except KeyError:
        print('Key Error ')



def display_menu():
    print('COMMAND MENU')
    print('view - View country name')
    print('add - Add a country')
    print('exit - Exit program')
    print()


def view(countries):
    display_codes(countries)
    country_code = input('Enter country code to view: ')
    country_code = country_code.upper()
    if country_code in countries:
        country_name = countries[country_code]
        myFile=open('index.txt', 'w')
        myFile.write( country_name)
        myFile.close()
        
        print('Country name: ' + country_name + '.\n')
    else:
        print('There is no country with that code. \n')


def add(countries):
    display_codes(countries)
    country_code = input('Enter new country code to add: ')
    country_code = country_code.upper()
    if country_code in countries:
        country_name = countries[country_code]
        print(country_name + ' is already using this code. \n')
    else:
        country_name = input('Enter country name: ')
        country_name = country_name.title()
        countries[country_code] = country_name
        myFile=open('index.txt', 'a')
        myFile.write( country_name)
        myFile.close()
        print (country_name + ' was added. \n')



def display_codes(countries):
    country_codes = list(countries.keys())
    country_codes.sort()
    line = 'Country codes: '
    for country_code in country_codes:
        line += country_code + ' '
    print(line)


if __name__ == '__main__':
    main()

