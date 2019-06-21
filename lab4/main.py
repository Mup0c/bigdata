import collections

f = open('db2.txt', 'r')

cntr = collections.Counter()
line = f.readline()
while (line):
    cntr[line] += 1
    line = f.readline()
common = cntr.most_common(25)
for val in common:
    print(val[0])
