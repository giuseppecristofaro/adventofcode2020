def read(filename):
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f.readlines():
            data.append(int(line.strip()))
    return data
    
def search(data):
    for i in range(0, len(data)):
        for j in range(i, len(data)):
            if data[i] + data[j] == 2020:
                print("2020 with 2 numbers: %d %d %d" % (data[i], data[j], data[i] * data[j]))
            for z in range(j, len(data)):
                if data[i] + data[j] + data[z] == 2020:
                    print("2020 with 3 numbers: %d %d %d %d" % (data[i], data[j], data[z], data[i] * data[j] * data[z]))
                
data = read("input1")
search(data)
