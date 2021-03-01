import re

text = input()
ex = r"^>>(?P<furniture>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<qty>[0-9]+)\b"
furniture = []
total_price = 0

while not text == "Purchase":
    
    text = re.search(ex, text)
    
    if text:
        text = text.groupdict()
        furniture.append(text["furniture"])
        total_price += float(text["price"]) * int(text["qty"])
    
    text = input()

print("Bought furniture:")
for el in furniture:
    print(el)

print(f"Total money spend: {total_price:.2f}" )