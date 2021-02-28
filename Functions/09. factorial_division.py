
# Import math module and use the factorial func
import math

def factorial_division(num_1, num_2):
    factorial_num_1 = math.factorial(num_1)
    factorial_num_2 = math.factorial(num_2)
    result = factorial_num_1 / factorial_num_2
    return (f"{result:.2f}")

num_one = int(input())
num_two = int(input())

print(factorial_division(num_one, num_two))

