
# Solution 1

def find_perf_number(number):
    sum_nums = 0
    
    for num in range(1, number):
        if number % num == 0:
            sum_nums += num
            
    if sum_nums == number:
        print ("We have a perfect number!")
    else:
        print ("It's not so perfect.")
        
number_input = int(input())
find_perf_number(number_input)


# Solution 2

def find_perf_number(n):
    divisors = []
    
    for num in range(1, n):
        if n % num == 0:
            divisors.append(num)
            
    if sum(divisors) == n:
        return True
    
    return False
        
number = int(input())

if find_perf_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
