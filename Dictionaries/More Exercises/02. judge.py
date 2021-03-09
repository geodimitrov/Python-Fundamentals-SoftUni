# def find_participants(contest_name, contests_data):
#     return sum([1 for data in contests_data.values() if contest_name in data])
#
# def sort_dict_by_contest(contest_name, contests_data):
#     return dict(sorted(contests_data.items(), key=lambda x: contest_name))
#
# def print_contests(contests, contests_data):
#    for contest in contests:
#        participants = find_participants(contest, contests_data)
#        sorted_dict = sort_dict_by_contest(contest, contests_data)
#        print(f"{contest}: {participants} participants")
#        print(sorted_dict)
#
#        # print(f"{position}. {username} <::> {points}")
#
#
# def print_participants():
#     pass
#
# STOP = "no more time"
#
# contests_data = {}
# contests = []
#
# # read input
# while True:
#     line = input()
#     if line == STOP:
#         break
#
#     username, contest_name, points = line.split(" -> ")
#     # add the contests to a list to keep track of the input order
#     if contest_name not in contests:
#         contests.append(contest_name)
#     # add user
#     if username not in contests_data:
#         contests_data[username] = {}
#     # add contest name and points
#     if contest_name not in contests_data[username]:
#         contests_data[username][contest_name] = int(points)
#     # change contest points if provided points > current points
#     if int(points) > contests_data[username][contest_name]:
#         contests_data[username][contest_name] = int(points)
#
#
# print_contests(contests, contests_data)
# # print_participants()

dd = {'Pesho': {'Algo': 400, 'DS': 150},
        'Gosho': {'Algo': 300},
        'Stamat': {'Algo': 200},
        'Mimi': {'DS': 600}
    }

sorted_dict = dict(sorted(dd.items(), key=lambda x: ))
print(sorted_dict)
