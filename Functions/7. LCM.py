
# PROBLEM: LCM LEAST COMMON MULTIPLE

def LCM(a: int, b: int):
    
    greater = max(a, b)
    while True:
        if (greater % a == 0) and (greater % b == 0):
            return greater
        greater += 1

a = LCM(4, 6)
print(a)

# SECOND APPROCH 

def GCD(a: int, b: int):
    values = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            values.append(i)
    
    return max(values)

def LCM(a: int, b: int):
    return a * b // GCD(a, b)


a = LCM(5, 56)
print(a)

