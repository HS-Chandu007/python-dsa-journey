
# PROBLEM: WRITE A FUCNTION TO CHECK IF A NUMBER IS PALINDROME OR NOT

def reverse_number(n: int):
    
    rev = 0
    while n != 0:
        digit = n % 10
        n = n // 10
        rev = (rev * 10) + digit
    return rev



def palindrome(n: int):
    original = n
    if reverse_number(n) == original:
        return True
    else:
        return False
        
a = palindrome(551561113)
print(a)