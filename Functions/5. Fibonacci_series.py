
# PROBLEM: PRINT FIBONACCI SERIES

def fibonacci(n: int):
    prev = 0
    cur = 1
    for i in range(n):
        print(prev)
        
        next = prev + cur
        prev = cur
        cur = next

fibonacci(5)
    