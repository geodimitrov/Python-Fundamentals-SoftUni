
# Define the broader func & inside of it define the other 2 funcs
def add_and_subtract(num_1, num_2, num_3):
    
    def sum_nums (num_1, num_2):
        return num_1 + num_2
    
    def subtract(num_1, num_2, num_3):
        return sum_nums(num_1, num_2) - num_3
    
    return subtract(num_1, num_2, num_3)
    
                   
num_one = int(input())
num_two = int(input())
num_three = int(input())

print(add_and_subtract(num_one, num_two, num_three))

