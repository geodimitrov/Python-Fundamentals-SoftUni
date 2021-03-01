data = input()
products = {}

while not data == "buy":
    product, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)
                  
    if product in products:
        if price != products[product][0]:
            products[product][0] = price
        products[product][1] += quantity
    else:
        products[product] = [price, quantity]
    
    data = input()

for key, value in products.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")