score = input('Enter quiz score – whole number 0-100: ')
# validation block
if score.isnumeric() is False:
    print('Try the program again; it only takes whole numbers.')
else:
    score = int(score) 
    if score >= 90:
        print('Excellent.')
        print("Keep it up.")
    elif score >= 80:
        print('Very Good')
        print("Passed.")
    elif score >= 70:
        print('Good')
        print("Above Average.")
    elif score >= 60:
        print('Fair')
        print("Put a little more effort.")
    elif score >= 50:
        print('Not passing')
        print("May be try again in the future.")
    elif score <= 40:
        print('Grade: Failed.')
        print("Pull up your socks.")
    else:
        print('Your grade is currently undefined.')


year = int(input('What year did Apollo 11 land on the moon? '))
if year == 1969:
    print(f'Correct! {year} is right!')
elif year in range(1959, 1979):
    print("too close")
else:
    print(f'Sorry, {year} is the wrong answer.')
