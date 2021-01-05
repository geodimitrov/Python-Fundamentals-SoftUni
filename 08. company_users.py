#!/usr/bin/env python
# coding: utf-8

# In[10]:


data = input()

companies = {}

while not data == "End":
    company_name, employee_id = data.split(" -> ")
    
    if company_name not in companies:
        companies[company_name] = []
        companies[company_name].append(employee_id)
    else:
        if employee_id not in companies[company_name]:
            companies[company_name].append(employee_id)
        
    
    data = input()
    
sorted_companies = sorted(companies.items(), key=lambda x: (x[0], x[1]))

for company, employee in sorted_companies:
    print(f"{company}")
    for n in employee:
        print(f"-- {n}")


# In[ ]:




