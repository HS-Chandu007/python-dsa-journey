
# PROBLEM: CHECK INPUT NUMBER FOR POSTIVE, NEGATIVE OR ZERO

n = int(input('Enter the number: '))

if n > 0:
    print(f'{n} is postive number')
elif n < 0:
    print(f'{n} is negative number')
else:
    print(f'{n} is zero')