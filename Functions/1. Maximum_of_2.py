
# PROBLEM: WRITE FUNCTION TO RETURN THE MAXIMUM VALUE

def maxfinder(a: int, b: int):
    if a > b:
        return a
    else:
        return b
    

a = maxfinder(a=4, b=0)
print(a)