
numbers = [5, 8, 2, 9, 3, 8, 8, 1, 7, 23]

largest = numbers[0]
second_largest = numbers[0]

for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i
    elif i < largest and i > second_largest:
        second_largest = i
        
        
        

print(largest)
print(second_largest)