class Zoo:
    animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result = f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {self.animals}"
        elif species == "fish":
            result = f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {self.animals}"
        elif species == "bird":
            result = f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {self.animals}"
        return result

zoo_name = input()
zoo = Zoo(zoo_name)
lines = int(input())
for line in range(lines):
    species, name = input().split()
    zoo.add_animal(species, name)

animal_type = input()
print(zoo.get_info(animal_type))