import re, json

fields, eyes = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}, {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def read(filename):
    with open(filename, "r") as f:
        data = [i.replace("\n", " ").strip() for i in f.read().split("\n\n")]
    return data

def check_range(item, start, end):
    return int(item) >= start and int(item) <= end

def check_hgt(item):
    s, e = 0, 0
    if "cm" in item:
        s, e = 150, 193
    elif "in" in item: 
        s, e = 59, 76
    else:
        return False
    return check_range(item[:-2], s, e)
    
def check_hcl(item):
    regex = r"#[0-9a-f]{6}"
    return len(re.findall(regex, item)) > 0
    
def check_ecl(item):
    return item in eyes
    
def check_pid(item):
    regex = r"\b([0-9]{9})\b"
    return len(re.findall(regex, item)) > 0
    
def check_all(item):
    try:
        return check_range(item["byr"], 1920, 2002) and check_range(item["iyr"], 2010, 2020) and check_range(item["eyr"], 2020, 2030) and check_hgt(item["hgt"]) and check_hcl(item["hcl"]) and check_ecl(item["ecl"]) and check_pid(item["pid"])
    except Exception as e:
        return False

def check(data):
    count, count2 = 0, 0
    for item in data:
        item_dict = json.loads('{"%s"}' % item.replace(':', '":"').replace(' ', '","'))
        count += not fields - set(re.sub(r":[a-zA-Z0-9#]+|cid","", item).split())
        count2 += check_all(item_dict)
    return count, count2
    
data = read("input4.txt")
count, count2 = check(data)
print(count, count2)
