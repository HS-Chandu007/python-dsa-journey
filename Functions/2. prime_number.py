
# PROBLEM: CHECK IS THE GIVEN NUMBER IS PRIME OR NOT
    
def is_prime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True
        
a = is_prime()
print(a)