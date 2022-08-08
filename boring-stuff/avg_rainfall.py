""" Yahye Muhumed 14/7/2022 The program asks a user for the number of years in a multi-year rainfall study.
This determines how many times an outer loop will run, for yearly data. An inner loop will
always run 12 times, to collect a rainfall amount for each month in a given year, and total it up.
The outer loop finishes by calculating each year's avg. & displaying stats. Challenge level:
a multi-year total and avg. for the study period are calculated and displayed.  """

def main():

    num_years, rain_for_month = inputs()
    processing(num_years, rain_for_month)

def inputs():
    print(input('How many years are in your rainfall sample? '))  # validation needed
    num_years = get_pos_int()
    return num_years
   

def get_pos_int():  # collect and validate an int > 0
    pos_int = input('Please enter a whole number: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int

def processing(num_years, rain_for_month):
    multiyear_total = 0  # used for challenge level - initialize 2 study-wide variables
    multiyear_avg = 0  # 2nd study-wide variable
    for year in range(num_years): # outer loop starts - runs 1x for each year
        total_rain_year = 0  # initialize year-level variables
        avg_rain_year = 0.00
        print(f'Rainfall info for year #{year + 1}: ')
        for month in range(12):  # inner loop starts - runs 1x for each month (per year)
            rain_for_month = float(input(f'\tEnter rain for month #{month + 1}: '))  # to validate, use ints
            total_rain_year += rain_for_month  # accumulate each month's rain into yearly total
        avg_rain_year = total_rain_year/12  # back to outer loop - avg. is for the year
        print(f'Total rain in inches for year #{year + 1} = {total_rain_year}')
        print(f'Year #{year + 1} Monthly Avg Rainfall = {avg_rain_year :<.2f}')
        return num_years, total_rain_year

def outcomes(total_rain_year, num_years):
    multiyear_total += total_rain_year  # this accumulates each year's rain into a study total
    multiyear_avg = multiyear_total / num_years / 12  # calc. study avg.
    print(f'\nTotal rain, all years = {multiyear_total} inches')  # display study-level data
    print(f'Average monthly rain, all years = {multiyear_avg} inches')
    print('Thanks for using the program!')  # exit msg.

main()