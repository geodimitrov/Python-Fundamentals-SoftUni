#The only tricky part in this problem is the sorting
data = input()

courses = {}

while not data == "end":
    course_name, student_name = data.split(" : ")
    
    if course_name not in courses:
        courses[course_name] = []    
    courses[course_name].append(student_name)
        
    data = input()

#be careful when you sort
sorted_courses = dict(sorted(courses.items(), key= lambda x: len(x[1]), reverse=True))

for course, students in sorted_courses.items():
    print(f"{course}: {len(students)}")
    for name in sorted(students):
        print(f"-- {name}")