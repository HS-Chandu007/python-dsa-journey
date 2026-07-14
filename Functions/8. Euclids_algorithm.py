
# PROBLEM: EUCLIDS ALGORITHM FOR FINDING LCM

def euclids(a: int, b: int):
    while b != 0:
        remainder = a % b
        
        a = b
        
        b = remainder   
    return a

a = euclids(4, 6)
print(a)
    