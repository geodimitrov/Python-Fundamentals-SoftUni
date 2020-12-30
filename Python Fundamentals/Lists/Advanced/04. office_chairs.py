
n_rooms = int(input())

room = 0
free_chairs = 0

for i in range(n_rooms):
    chairs = input().split()
    room += 1
    
    if len(chairs[0]) >= int(chairs[1]):
        free_chairs += len(chairs[0]) - int(chairs[1])
    else:
        print(f"{int(chairs[1]) - len(chairs[0])} more chairs needed in room {room}")
        free_chairs += len(chairs[0]) - int(chairs[1])
    
if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")


# In[2]:


x = ["xxxx", 5]
print(len(x[0]))

