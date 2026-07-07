# PRODUCT OF NUMBERS

num = int(input('Enter the number: '))
total_product = 1

while num != 0:
    digit = num % 10
    total_product = total_product * digit
    num = num // 10
    
print(f'Product of digits: {total_product}')
