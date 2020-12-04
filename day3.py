def read(filename):
    data = []
    with open(filename, "r") as f:
        for row in f:
            for i in row.split():
                data.append(i)
    return data

def is_a_tree(x, y):
    return data[x][y] == "#"

def is_a_square(x, y):
    return data[x][y] == "."

def go_down(x, y, d, r):
    return x+d, (y+r) % len(data[0])

def is_goal(y):
    return y == len(data) - 1

data = read("input3.txt")
rr = [[1,1],[1,3],[1,5],[1,7],[2,1]]
t = 1

for i,j in rr:
    squares, trees, x, y = 0, 0, 0, 0
    while not is_goal(x):
        x, y = go_down(x, y, i, j)
        if is_a_square(x, y):
            squares+=1
        elif is_a_tree(x, y):
            trees+=1
        else:
            pass
    print("down:", i, "right:", j, "squares:", squares, "trees:", trees)
    t*=trees
print(t)
