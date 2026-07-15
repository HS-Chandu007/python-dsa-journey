
# PROBLEM: WRITE A FUNCTION TO REVERSE THE GIVEN NUMBER

def Reverse(n: int):
    
    reversed = 0
    
    while n != 0:
        digit = n % 10
        n = n // 10
        reversed = (reversed * 10) + digit
        
    return reversed


a = Reverse(5456744)
print(a)