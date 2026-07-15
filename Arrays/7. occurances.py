
numbers = [5, 8, 2, 9, 3, 8, 8, 1]
target = int(input('Enter the Target: '))
occurances = 0

for i in numbers:
    if i == target:
        occurances += 1
        
    
print(f'Total occurances: {occurances}')
    