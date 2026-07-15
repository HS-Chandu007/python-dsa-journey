numbers = [5, 8, 2, 9, 3]

minimum = numbers[0]
maximum = numbers[0]

for i in numbers:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
        
print(f"Minimum in Array: {minimum}")
print(f"Maximum in Array: {maximum}")