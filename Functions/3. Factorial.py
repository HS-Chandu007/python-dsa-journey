
# PROBLEM: PRINT FACTORIAL OF GIVEN NUMBER

def factorial(n: int):
    fact = 1
    while n > 0:
        fact = fact * n
        n = n - 1
    return fact

a = factorial(9)
print(a)