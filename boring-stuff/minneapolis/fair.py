"""Yahya Muhumed 14/7/2022  This program calculates & displays
regular, overtime and gross pay - using a table format.
Challenge - adapt it to fit regular and rush bus fares. """

# define variables & amounts provided
reg_rate = 15.34
ot_rate = reg_rate * 1.5
reg_hours = 40
ot_hours = 10

# calculate gross pay, saving detail for reg & ot pay
reg_pay = round(reg_hours * reg_rate, 2)
ot_pay = round(ot_hours * ot_rate, 2)
gross_pay =  reg_pay + ot_pay
total_hours = reg_hours + ot_hours

# display the regular, OT and total pay in a table.
print(f'Total pay for {total_hours} hours = ${gross_pay:,.2f}.')
print('{:<14}{:>5}{:>12}{:>5}{:>14}{:>6}'.format('Type', 'Hours', '', 'Rates', '', 'Total'))
print('{:<14}{:>5}{:>12}{:>5.2f}{:>14}{:>6.2f}'.format('Regular', reg_hours, '$', reg_rate, '$', reg_pay))
print('{:<14}{:>5}{:>12}{:>5.2f}{:>14}{:>6,.2f}'.format('Overtime', ot_hours, '$', ot_rate, '$', ot_pay))
