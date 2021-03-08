
def valid_contest_and_password(contests_data, contest, password):
    if contest in contests_data:
        return contests_data[contest] == password

def best_candidate(students_data):
    best_score = 0
    best_candidate = ""
    for student, contests_score in students_data.items():
        total_points = 0
        for score in contests_score.values():
            total_points += int(score)
        if total_points > best_score:
            best_score = total_points
            best_candidate = student
    return f"Best candidate is {best_candidate} with total {best_score} points."

def print_result(students_data):
    print ("Ranking:")
    for student, contest_data in sorted(students_data.items()):
        print(student)
        sorted_contest_data = dict(sorted(contest_data.items(), key=lambda x: (x[1], x[0]), reverse=True))
        for contest, score in sorted_contest_data.items():
            print(f"#  {contest} -> {score}")

contests_data = {}
students_data = {}

# read the input
while True:
    line = input()
    if line == "end of contests":
        break
    contest_name, contest_password = line.split(":")
    contests_data[contest_name] = contest_password

# read the submissions
while True:
    submission = input()
    if submission == "end of submissions":
        break

    contest, password, username, points = submission.split("=>")
    #check if contest and password are valid
    if valid_contest_and_password(contests_data, contest, password):
        if username not in students_data:
            students_data[username] = {}

        if contest not in students_data[username]:
            students_data[username][contest] = points
            continue

        if points > students_data[username][contest]:
            students_data[username][contest] = points

print(best_candidate(students_data))
print_result(students_data)
