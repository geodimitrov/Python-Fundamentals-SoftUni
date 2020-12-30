#!/usr/bin/env python
# coding: utf-8

# In[22]:



obtained = False
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

while obtained == False:
    data = input().split()
    
    for i in range(0, len(data), 2):
        material = data[i + 1].lower()
        quantity = int(data[i])
        
        
        if material in key_materials:
            key_materials[material] += quantity
            
            if key_materials[material] >= 250:
                if material == "shards":
                    print("Shadowmourne obtained!")
                elif material == "fragments":
                    print("Valanyr obtained!")
                elif material == "motes":
                    print("Dragonwrath obtained!")
                key_materials[material] -= 250
                obtained = True
                break
    
        else:
            if material not in junk:
                junk[material] = quantity
            else:
                junk[material] += quantity
        
sorted_key_materials = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))

for material, quantity in sorted_key_materials:
    print(f"{material}: {quantity}")

sorted_junk = sorted(junk.items(), key=lambda x: x[0])

for junk, quantity in sorted_junk:
    print(f"{junk}: {quantity}")


# In[ ]:




