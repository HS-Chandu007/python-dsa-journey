
numbers = [5, 8, 2, 9, 3]
target = int(input("Enter the Target: "))

for i in numbers:
    if i == target:
        print(f"Target Found: {i}")
        break
else:
    print("Target Not Found")