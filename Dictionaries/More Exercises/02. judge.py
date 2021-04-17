END = "no more time"

def read_input():
    result = []

    while True:
        line = input()

        if line == END:
            break
        result.append(line)

    return result

def calc_contests_statistics(data):
    result = {}

    for line in data:
        username, contest_name, points = line.split(" -> ")
        points = int(points)

        if contest_name not in result:
            result[contest_name] = {}

        if username not in result[contest_name]:
            result[contest_name][username] = points
        else:
            current_points = result[contest_name][username]
            if current_points < points:
                result[contest_name][username] = points

    return result

def get_contest_participants(data):
    participants = []

    for participant_data in data.values():
        for username in participant_data.keys():
            if username not in participants:
                participants.append(username)

    return participants

def get_participant_total_score(data, username):
    score = 0

    for contest in data.values():
        if username in contest:
            score += contest[username]

    return score

def get_participants_standings(data, participants):
    result = {}

    for participant in participants:
        total_score = get_participant_total_score(data, participant)
        result[participant] = total_score

    return result

def calc_individual_statistics(contest_statistics):
    participants = get_contest_participants(contest_statistics)
    participants_scores = get_participants_standings(contest_statistics, participants)

    return participants_scores

def sort_contest_scores(scores):
    return dict(sorted(scores.items(), key=lambda x: (-x[1], x[0])))

def format_scores(contest_name, scores):
    participants_scores = []
    participant_position = 0

    for username, score in scores.items():
        participant_position += 1
        participants_scores.append(f"{participant_position}. {username} <::> {score}")

    return f"{contest_name}: {len(scores)} participants\n"\
            + "\n".join(participants_scores)

def print_contests_results(statistics):

    for contest_name, contest_scores in statistics.items():
        sorted_contest_scores = sort_contest_scores(contest_scores)
        formatted_scores = format_scores(contest_name, sorted_contest_scores)
        print(formatted_scores)

def sort_individual_scores(statistics):
    return dict(sorted(statistics.items(), key=lambda x: (-x[1], x[0])))

def format_standings(individual_scores):
    result = []
    position = 0

    for username, score in individual_scores.items():
        position += 1
        result.append(f"{position}. {username} -> {score}")

    return "Individual standings:\n"\
            + "\n".join(result)

def print_individual_standings(statistics):
    sorted_individual_scores = sort_individual_scores(statistics)
    formatted_standings = format_standings(sorted_individual_scores)
    print(formatted_standings)

input_data = read_input()
contests_statistics = calc_contests_statistics(input_data)
individual_statistics = calc_individual_statistics(contests_statistics)
print_contests_results(contests_statistics)
print_individual_standings(individual_statistics)