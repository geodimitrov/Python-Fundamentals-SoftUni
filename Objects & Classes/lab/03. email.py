# create the class
class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

# create the methods
    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

#start reading the emails info
emails_info = []
while True:
    line = input()
    if line == "Stop":
        break
    sender, receiver, content = line.split() #extract the data by splitting the line, create object
    email = Email(sender, receiver, content)
    emails_info.append(email)

# read the indices of the sent emails
sent_emails = [int(el) for el in input().split(", ")]

# call the send() method for the sent emails (using their indices)
for index in sent_emails:
    emails_info[index].send()

# call the get_info method for all emails in the list
for email in emails_info:
    print(email.get_info())