
# Count the no.of digits in the input

num = int(input('Enter the number: '))
count = 0

while num != 0:
    print(num)
    num = num // 10
    count += 1
    
print("No.of Digits: ", count)  