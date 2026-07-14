
# PROBLEM: GCD GREATEST COMMOM DIVISOR

        
def GCD(a: int, b: int):
    
    values = []
    for i in range(1, b):
        if a % i == 0 and b % i == 0:
            values.append(i)
        
    return max(values)


a = GCD(8, 20)
print(a)
