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
    
data = read("input5.txt")
tickets = set()

for item in data:
    row = get_row(item[:7])
    col = get_col(item[7:])
    tickets.add(row * 8 + col)

print(max(tickets))
