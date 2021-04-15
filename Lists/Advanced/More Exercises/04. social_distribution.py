
population = list(map(int, input().split(", ")))
min_wealth = int(input())
is_possible_distribution = True

def can_distribute_wealth(population, min_wealth):
    average_wealth = sum(population) // len(population)
    return average_wealth >= min_wealth

for i in range(len(population)):

    if not can_distribute_wealth(population, min_wealth):
        is_possible_distribution = False
        break

    el = population[i]
    if el < min_wealth:
        amount_to_distribute = min_wealth - el
        max_el = max(population)
        if max_el - amount_to_distribute >= min_wealth:
            population[i] += amount_to_distribute
            max_el_index = population.index(max_el)
            population[max_el_index] = max_el - amount_to_distribute

if not is_possible_distribution:
    print("No equal distribution possible")
else:
    print(population)