numbers = [int(el) for el in input().split()]

greater_than_average = [n for n in numbers if n > sum(numbers) / len(numbers)]

greater_than_average.sort(reverse=True)

if len(greater_than_average) == 0:
    print("No")

elif len(greater_than_average) < 6:
    greater_than_average = [str(n) for n in greater_than_average]
    print(" ".join(greater_than_average))

else:
    greater_than_average = [str(n) for n in greater_than_average]
    print(" ".join(greater_than_average[:5]))