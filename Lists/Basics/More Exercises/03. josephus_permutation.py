# read the input
sequence = "1 2 3 4 5 6 7".split()

ll = [3, 6, 2]

K = 3
result = [] #to store the removed elements and their order

for i in range(2, len(sequence), i + K):
    result.append(sequence.pop(i))

print(result)
print(sequence)