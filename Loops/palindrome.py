
# PALINDROME NUMBER

num = int(input('Enter the number: '))
check_num = num
rev = 0

while num != 0:
    digit = num % 10
    num = num // 10
    rev = (rev * 10) + digit
    
    
if rev != check_num:
    print("Not Palindrome.")
else:
    print('Palindrome Number.')