END_COMMAND = "Season end"

def read_input():
    result = []

    while True:
        line = input()

        if line == END_COMMAND:
            break
        result.append(line)

    return result

def add_player_info_to_repo(repository, name, position, skill):
    if name not in repository:
        repository[name] = {}

    if position in repository[name]:
        curr_skill = repository[name][position]

        if curr_skill < skill:
            repository[name][position] = skill
            return

    repository[name][position] = skill

def execute_commands(data):
    repository = {}

    for line in data:
        split_line = line.split(" -> ")

        if len(split_line) == 1:
            player_one, player_two = line.split(" vs ")
            commence_duel(repository, player_one, player_two)

        else:
            name, position, skill = split_line
            add_player_info_to_repo(repository, name, position, int(skill))

    return repository

def get_player_total_skill_pts(repository, player):
    result = 0

    for skill in repository[player].values():
        result += skill

    return result

def get_into_a_fight(repository, player_one, player_two):
    player_one_total_skill_pts = get_player_total_skill_pts(repository, player_one)
    player_two_total_skill_pts = get_player_total_skill_pts(repository, player_two)

    if player_one_total_skill_pts > player_two_total_skill_pts:
        del repository[player_two]
    elif player_one_total_skill_pts < player_two_total_skill_pts:
        del repository[player_one]

def execute_duel(repository, player_one, player_two):
    for position in repository[player_one]:
        if position in repository[player_two]:
            return get_into_a_fight(repository, player_one, player_two)

def commence_duel(repository, player_one, player_two):
    if player_one in repository and player_two in repository:
        execute_duel(repository, player_one, player_two)

def sort_players_by_skills(repository):
    result = {}
    for player_name in repository:
        total_skill_points = get_player_total_skill_pts(repository, player_name)
        result[player_name] = total_skill_points

    return dict(sorted(result.items(), key=lambda x: (-x[1], x[0])))

def sort_positions_by_player_and_skill(repository, player):
    positions = repository[player]
    sorted_positions = dict(sorted(positions.items(), key=lambda x: (-x[1], x[0])))
    return sorted_positions

def print_result(repository):
    sorted_by_skill = sort_players_by_skills(repository)

    for player, total_skill in sorted_by_skill.items():
        print(f"{player}: {total_skill} skill")
        sorted_positions = sort_positions_by_player_and_skill(repository, player)

        for position, skill in sorted_positions.items():
            print(f"- {position} <::> {skill}")

input_data = read_input()
players_repository = execute_commands(input_data)
print_result(players_repository)