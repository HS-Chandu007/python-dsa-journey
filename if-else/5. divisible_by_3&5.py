
# PROBLEM: DIVISIBLE BY 3 & 5

n = int(input('Enter the number: '))

if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
elif n % 3 == 0:
    print('Fizz')
elif n % 5 == 0:
    print('Buzz')
else:
    print(n)