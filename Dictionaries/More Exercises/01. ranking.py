def read_contests_info():
    END = "end of contests"
    result = {}

    while True:
        input_line = input()

        if input_line == END:
            break

        contest_name, contest_password = input_line.split(":")
        result[contest_name] = contest_password

    return result

def read_submissions_info():
    END = "end of submissions"
    result = []

    while True:
        input_line = input()

        if input_line == END:
            break

        result.append(input_line)

    return result

def is_valid_contest(contests, contest, password):
    if contest in contests:
        return contests[contest] == password

def update_contest_points(data, user, contest, new_points):
    current_points = data[user][contest]

    if current_points < new_points:
        data[user][contest] = new_points

def update_users_data(data, user, contest, points):
    if user not in data:
        data[user] = {}

    if contest not in data[user]:
        data[user][contest] = points
    else:
        update_contest_points(data, user, contest, points)

def process_submissions(contests, submissions):
    users_data = {}

    for sub in submissions:
        contest_name, contest_password, username, points = sub.split("=>")
        points = int(points)

        if is_valid_contest(contests, contest_name, contest_password):
            update_users_data(users_data, username, contest_name, points)

    return users_data

def get_user_total_points(data):
    total_points = 0

    for value in data.values():
        total_points += int(value)

    return total_points

def get_best_candidate_points(contests_results):
    best_score = 0
    best_candidate = None

    for user in contests_results:
        user_data = contests_results[user]
        user_total_points = get_user_total_points(user_data)

        if user_total_points > best_score:
            best_score = user_total_points
            best_candidate = user

    return best_candidate, best_score

def get_ordered_results_by_name_and_points(results):
    ordered_results = dict(sorted(results.items()))

    for user, user_data in ordered_results.items():
        ordered_user_data = dict(sorted(user_data.items(), key=lambda x: x[1], reverse=True))
        ordered_results[user] = ordered_user_data

    return ordered_results

def get_user_data(results, user):
    return f"{user}\n" + "\n".join(f"#  {contest} -> {points}" for contest, points in results[user].items())

def print_result(contests_results):
    best_candidate, points = get_best_candidate_points(contests_results)
    ordered_results = get_ordered_results_by_name_and_points(contests_results)
    print(f"Best candidate is {best_candidate} with total {points} points.")
    print("Ranking:\n" + "\n".join(get_user_data(ordered_results, user) for user in ordered_results))

contests_info = read_contests_info()
submissions_info = read_submissions_info()
contests_results = process_submissions(contests_info, submissions_info)
print_result(contests_results)