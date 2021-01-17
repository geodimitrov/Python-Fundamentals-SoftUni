#create a func to find num of elements in each set
def find_numbers():
    nums = tuple(map(int, input().split()))
    return nums
#create a func to fill in the sets
def fill_set(count):
    s = set([])
    for _ in range(count):
        s.add(input())
    return s
#create func to find the intersection of the sets, use intersection method
def find_intersection(s1, s2):
    result = s1.intersection(s2)
    for el in result:
        print(el)

n, m = find_numbers()

set_one = fill_set(n)
set_two = fill_set(m)
find_intersection(set_one, set_two)
