
# create constants

R_HIGH = range(81, 126)
R_MEDIUM = range(51, 81)
R_LOW = range(1, 51)

# introduce input variables
fires_data = input().split('#')
water = int(input())
effort = 0
put_out_fire = []

for element in fires_data:
    type_fire, value = element.split(" = ")
    value = int(value)
    
    if type_fire == "High" and value not in R_HIGH:
        continue
    elif type_fire == "Medium" and value not in R_MEDIUM:
        continue
    elif type_fire == "Low" and value not in R_LOW:
        continue
    
    if water >= value:
        water -= value
        effort += value * 0.25
        put_out_fire.append(value)    

        
print ("Cells:")
for value in put_out_fire:
    print (f" - {value}")

print(f"Effort: {effort:.2f}")
print (f"Total Fire: {sum(put_out_fire)}")
