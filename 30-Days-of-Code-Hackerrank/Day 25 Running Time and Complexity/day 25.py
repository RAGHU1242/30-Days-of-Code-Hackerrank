import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Read number of test cases
T = int(input())

# Loop over each test case
for _ in range(T):
    n = int(input())
    
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
