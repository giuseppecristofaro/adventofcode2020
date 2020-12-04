import re

def read(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
    return data

def read2(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = f.readlines()
    return data

def check_policy_regex(data):
    regex = r"(\d{1,2}\-\d{1,2}) (\w)(:) (\w+)"
    match = re.findall(regex, data)
    count = 0
    for m in match:
        nm, ch, sc, text = m
        regex = r"\b([%s]{%s})\b" % (ch, nm.replace("-", ","))
        text = re.sub(r"[^%s]" % ch, "", text)
        found = re.findall(regex, text)
        if found:
            count += 1      
    return count

def check_policy(data):
    count = 0
    for line in data:
        nm, ch, text = line.split()
        c1, c2 = nm.split("-")
        c = text.count(ch[0])
        if c >= int(c1) and c <= int(c2):
            count +=1   
    return count

def check_policy_two(data):
    count = 0
    for line in data:
        nm, ch, text = line.split()
        c1, c2 = nm.split("-")
        c1 = int(c1) - 1
        c2 = int(c2) - 1
        if text[c1] == ch[0] and text[c2] != ch[0] or text[c1] != ch[0] and text[c2] == ch[0]:
            count += 1
    return count

data = read("input2.txt")
data2 = read2("input2.txt")
count_regex = check_policy_regex(data)
count1 = check_policy(data2)
count2 = check_policy_two(data2)
print(count_regex)
print(count1)
print(count2)
