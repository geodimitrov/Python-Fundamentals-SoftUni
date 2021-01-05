#!/usr/bin/env python
# coding: utf-8

# In[19]:


data = input()

language_submissions = {}
students_scores = {}

while not data == "exam finished":
    
    if "banned" in data:
        username = data.split("-")[0]
        del students_scores[username]
    
    else:
        username, language, points = data.split("-")
        points = int(points)
        if username not in students_scores:
            students_scores[username] = []
        students_scores[username].append(points)
    
        if language not in language_submissions:
            language_submissions[language] = 0
        language_submissions[language] += 1
        
    
    data = input()

for student, score in students_scores.items():
    students_scores[student] = max(score)

print("Results:")
for student, score in sorted(students_scores.items(), key= lambda x: (-x[1], x[0])):
    print (f"{student} | {score}")

print("Submissions:")
for language, count in sorted(language_submissions.items(), key=lambda x: (-x[1], x[0])):
    print(f"{language} - {count}")


# In[ ]:




