f = open('graph.txt', 'r')

data = dict()
used = dict()

line = f.readline()
while line:
    line = line.replace(" ", "").replace("\n", "")
    splitted = line.split(":")
    key = splitted[0]
    values = splitted[1].split(",")
    data[key] = values
    for value in values:
        if (data.get(value) == None):
            data[value] = [key]
        elif (key not in data[value]):
            data[value].append(key)
    line = f.readline()


def dfs(key):
    used[key] = True
    for value in data[key]:
        if(used.get(value) == None):
            dfs(value)

def find_components():
    res = 0
    for key in data.keys():
        if (used.get(key) == None):
            res += 1
            dfs(key)
    return res


print(find_components())