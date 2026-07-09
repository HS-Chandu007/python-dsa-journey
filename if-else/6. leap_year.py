
# PROBLEM: LEAP YEAR

n = int(input('Enter the year: '))

if n % 400 == 0 or n % 4 == 0 and n % 100 != 0:
    print(f'{n} is a Leap year')
else:
    print(f'{n} is not a Leap year')