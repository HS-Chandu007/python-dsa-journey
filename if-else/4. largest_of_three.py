
# PROBLEM: LARGEST OF THREE NUMBERS

n1 = int(input('Enter number 1: '))
n2 = int(input('Enter number 2: '))
n3 = int(input('Enter number 3: '))

if n1 > n2 and n1> n3:
    print(f'{n1} is greater than {n2} and {n3}')
elif n2 > n1 and n2 > n3:
    print(f'{n2} is greater than {n1} and {n3}')
elif n1 == n2 and n2 == n1 and n2 == n3 and n3 == n2:
    print(f'{n1} {n2} {n3} are equall')
else:
    print(f'{n3} is greater than {n1} and {n2}')