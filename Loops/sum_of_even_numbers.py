
# Problem 4 — Sum of Even Numbers

# First approach

n = 10

total = 0

for i in range(2, n+1, 2):
    total += i

print(total)

# Second approach

total2 = 0

for i in range(1, n+1):
    if i % 2 == 0:
        total2 += i
        
print(total2)