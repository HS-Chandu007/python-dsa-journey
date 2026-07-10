
# PROBLEM: PRINT THE POWER OF A NUMBER

def power(base: int, exponent: int, power: int = 1):
    for i in range(1, exponent+1):
        power *= base
    return power

a = power(2, 5)
print(a)

b = power(3, 2)
print(b)