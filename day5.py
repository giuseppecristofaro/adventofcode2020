def read(filename):
    with open(filename, "r") as f:
        data = f.readlines()
    return data

def get_row(text):
    text = text.replace("F", "0").replace("B", "1")
    return int(text, 2)
    
def get_col(text):
    text = text.replace("L", "0").replace("R", "1")
    return int(text, 2)
   
def get_tickets(data):
    tickets = set()
    for item in data:
        row = get_row(item[:7])
        col = get_col(item[7:])
        tickets.add(row * 8 + col)
    return list(tickets), max(tickets)

def get_ticket(tickets):
    tickets.sort()
    for index in range(1, len(tickets)-1):
        if tickets[index+1] - tickets[index-1] > 2:
            return tickets[index-1] + 1

data = read("input5.txt")
tickets, max_ticket = get_tickets(data)
ticket = get_ticket(tickets)

print("max ticket:", max_ticket, "my ticket:",ticket)
