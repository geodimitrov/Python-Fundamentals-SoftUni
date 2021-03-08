def tribonacci_sequence(n):
    sequence = []
    result = 0

    for i in range(n):
        if i == 0:
            result = 1
        elif i < 3:
            result = sum(sequence[:i])
        else:
            result = sum(sequence[i-3:i])
        sequence.append(result)

    return " ".join(map(str, sequence))

# read number
num = int(input())
print(tribonacci_sequence(num))