#create a func to fill in the set of elements
def create_set_elements(count):
    list = []
    for _ in range(count):
        for el in input().split():
            list.append(el)
    return set(list)

#create a func that prints the result
def print_result(set):
    for el in set:
        print(el)

n = int(input())
elements = create_set_elements(n)
print_result(elements)
