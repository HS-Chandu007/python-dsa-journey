
# PROBLEM: TRIANGLE TYPE

a = int(input('Enter A: '))
b = int(input('Enter B: '))
c = int(input('Enter C: '))

if a + b > c and a + c > b and b + c > a:
    
    if a == b and b == c:
        print('Equilateral')
    elif a == b or a == c or b == c:
        print('Isoceles')
    else:
        print('Scalene')
else:
    print('Invalid Triangle')