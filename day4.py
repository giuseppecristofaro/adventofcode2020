import re

fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

def read(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n\n")
    return data
    
def check(data):
    count = 0
    for item in data:
        count += not fields - set(re.sub(r":[a-zA-Z0-9#]+|cid","", item).split())
    return count
    
data = read("input4.txt")
count = check(data)
print(count)
