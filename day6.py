def read(filename):
	with open(filename, "r") as f:
		data = f.read().split("\n\n")
	return data

def count(data):
    count_1, count_2 = 0, 0
    for item in data:
        count_1 += len(set(item.replace("\n", "")))
        current = [set(i) for i in item.split()]
        count_2 += len(current[0].intersection(*current[1:]))
    return count_1, count_2

data = read("input6.txt")
c1, c2 = count(data)
print("count_1:", c1, "count_2:", c2)

