
# always import the regex module

import re

text = input()

nums = []

while text:
    
    match = re.findall(r"\d+", text)
    
    if match:
        nums.extend(match)
    
    text = input()
    
print(*nums, sep=" ")

