# create the class
class Party:
    def __init__(self):
        self.people = []
# create an instance of the class
party = Party()

#start adding people by reading the line
while True:
    line = input()
    if line == "End":
        break
    party.people.append(line)

print(f'Going: {", ".join(party.people)}')
print(f"Total: {len(party.people)}")