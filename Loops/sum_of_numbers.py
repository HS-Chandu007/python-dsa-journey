
# SUM OF NUMBERS

num = int(input('Enter the number: '))
total_sum = 1

while num != 0:
    digit = num % 10
    total_sum = total_sum + digit
    num = num // 10
    
print(f'Sum of digits: {total_sum}')