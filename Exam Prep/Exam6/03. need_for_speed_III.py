n = int(input())

cars = {}

for _ in range(n):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = [mileage, fuel]

def drive_car(list_car_data, car_name, car_distance, used_fuel):
    if used_fuel > list_car_data[car_name][1]:
        print("Not enough fuel to make that ride")
    else:
        list_car_data[car_name][0] += car_distance
        list_car_data[car_name][1] -= used_fuel
        print(f"{car_name} driven for {car_distance} kilometers. {used_fuel} liters of fuel consumed.")

        if list_car_data[car_name][0] >= 100000:
            del list_car_data[car_name]
            print(f"Time to sell the {car_name}!")

def refuel_car(list_car_data, car_name, fuel_to_fill):
    if fuel_to_fill + list_car_data[car_name][1] > 75:
        fuel_used = 75 - list_car_data[car_name][1]
        list_car_data[car_name][1] = 75
    else:
        fuel_used = fuel_to_fill
        list_car_data[car_name][1] += fuel_to_fill
    print(f"{car_name} refueled with {fuel_used} liters")

command = input()

while not command == "Stop":
    command_type, car = command.split(" : ")[:2]

    if command_type == "Drive":
        distance, fuel = command.split(" : ")[2:]
        distance = int(distance)
        fuel = int(fuel)
        drive_car(cars, car, distance, fuel)

    elif command_type == "Refuel":
        fuel = int(command.split(" : ")[2])
        refuel_car(cars, car, fuel)

    elif command_type == "Revert":
        kilometers = int(command.split(" : ")[2])
        cars[car][0] -= kilometers
        if cars[car][0] >= 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars[car][0] = 10000

    command = input()

sorted_cars = dict(sorted(cars.items(), key= lambda x: (-x[1][0], x[0])))

for key, values in sorted_cars.items():
    print(f"{key} -> Mileage: {values[0]} kms, Fuel in the tank: {values[1]} lt.")