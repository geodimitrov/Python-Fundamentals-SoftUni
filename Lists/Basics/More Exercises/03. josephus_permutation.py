# Solution 1 - using recursion
ordered_sequence = []

# Create functions to break down the logic of the problem
def read_input():
    sequence = input().split()
    k = int(input())
    return sequence, k

def josephus_perm(seq, start, k):
    global ordered_sequence
    if len(seq) == 1:
        ordered_sequence.append(seq[0])
        return ordered_sequence
    el_index = (start + k - 1) % len(seq)
    ordered_sequence.append(seq.pop(el_index))
    start = el_index
    return josephus_perm(seq, start, k)

def print_result(result):
    print("[" + ",".join(result) + "]")

initial_sequence, K = read_input()
START = 0

result = josephus_perm(initial_sequence, START, K)
print_result(result)



# Solution 2 - using loops (this is def faster and more efficient)

def read_input():
    sequence = input().split()
    k = int(input())
    return sequence, k

def josephus_perm(seq, start, k):
    result = []

    while seq:
        el_index = (start + k - 1) % len(seq)
        result.append(seq.pop(el_index))
        start = el_index

    return result

def print_result(result):
    print("[" + ",".join(result) + "]")

initial_sequence, K = read_input()
START = 0

new_sequence = josephus_perm(initial_sequence, START, K)
print_result(new_sequence)