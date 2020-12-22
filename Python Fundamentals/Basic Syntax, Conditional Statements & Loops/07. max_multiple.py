
# 1. Introduce variables
divisor = int(input())
bound = int(input())
N = bound

# 2. Run a while loop that checks which is the largest int number (N) divisible by the divisor. Start from bound
while bound % divisor != 0:
    bound -= 1
    N = bound

# 3. Print result
print (N)
