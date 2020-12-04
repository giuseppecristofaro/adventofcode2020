import re

fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

def read(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n\n")
    return data
    
def count(data):
    check = 0
    for item in data:
        check += not fields - set(re.sub(r":[a-zA-Z0-9#]+|cid","", item).split())
    return check
    
data = read("input4.txt")
check = count(data)
print(check)
