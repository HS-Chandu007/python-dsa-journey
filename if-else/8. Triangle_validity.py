
# PROBLEM: VALIDATE THE TRIANGLE

a = int(input('Enter A: '))
b = int(input('Enter B: '))
c = int(input('Enter C: '))

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print('Invalid Triangle')
      