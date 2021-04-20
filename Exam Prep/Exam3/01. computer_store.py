command = input()

total_price = 0

while not (command == "special" or command == "regular"):
    price = float(command)

    if price < 0:
        print("Invalid price!")
    else:
        total_price += price
    command = input()

taxes = total_price * 0.2
total_price_plus_tax = total_price * 1.2

if total_price == 0:
    print("Invalid order!")
else:
    if command == "special":
        total_price_plus_tax *= 0.9

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_plus_tax:.2f}$")