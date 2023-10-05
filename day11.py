inputs = list([])
from sys import stdin
count = list([0,0,0,0,0,0])
total = 0
for line in stdin:
    inputs = line.split(",")
for c in inputs:
    if c == 'nw': count[0] += 1
    if c == 'n': count[1] += 1
    if c == 'ne': count[2] += 1
    if c == 'sw': count[3] += 1
    if c == 's': count[4] += 1
    if c == 'se': count[5] += 1

    directions = dict({'nw' : count[0] - min(count[0], count[3]), 'n' : count[1] - min(count[1], count[4]), 'ne' : count[2] - min(count[2], count[5]), 'se' : count[3] - min(count[0], count[3]), 's' : count[4] - min(count[1], count[4]), 'sw' : count[5] - min(count[2], count[5])})
    print(directions)
    minval = min(e for e in directions.values() if e > 0)
    currtotal = sum(directions.values()) - minval
    if(currtotal > total):
        total = currtotal
    print(currtotal)
print(total)

# #part 1
# inputs = list([])
# from sys import stdin
# for line in stdin:
#     inputs = line.split(",")
# count = list([inputs.count('nw'), inputs.count('n'), inputs.count('ne'), inputs.count('se'), inputs.count('s'), inputs.count('sw')])
# p = dict({'nw' : count[0], 'n' : count[1] , 'ne' : count[2], 'se' : count[3], 's' : count[4], 'sw' : count[5]})
# print(p)
# print(count)
# directions = dict({'nw' : count[0] - min(count[0], count[3]), 'n' : count[1] - min(count[1], count[4]), 'ne' : count[2] - min(count[2], count[5]), 'se' : count[3] - min(count[0], count[3]), 's' : count[4] - min(count[1], count[4]), 'sw' : count[5] - min(count[2], count[5])}) #works until here

# minval = min(e for e in directions.values() if e > 0)
# medval = min(e for e in directions.values() if e > minval)
# maxval = max(directions.values())
# total = (maxval + (medval - minval) + minval)
# print(total)









# inputs = list([])
# from sys import stdin
# n = 0, nw = 0, ne = 0, s = 0, sw = 0, se = 0
# for line in stdin:
#     for char in line
#         inputs.append() = line.split(",")