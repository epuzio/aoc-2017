##part 1
instructions = []
registers = dict([])
from sys import stdin
for line in stdin:
    elements = line.split() 
    registers.update({elements[0]: 0}) #push back first number
    instructions.append(elements)
curr_max = 0
for e in instructions:
    execute = False #not efficient, delete urself
    if e[5] == ">":
        execute = registers.get(e[4]) > int(e[6])
    elif e[5] == '<':
        execute = (registers.get(e[4]) < int(e[6]))
    elif e[5] == '>=':
        execute = registers.get(e[4]) >= int(e[6])
    elif e[5] == '<=':
        execute = (registers.get(e[4]) <= int(e[6]))
    elif e[5] == "==":
        execute = (registers.get(e[4]) == int(e[6]))
    elif e[5] == "!=":
        execute = (registers.get(e[4]) != int(e[6]))

    if execute == True:
        if e[1] == "inc":
            newval = registers.get(e[0]) + int(e[2])
            registers.update({e[0]: newval})
        elif e[1] == "dec":
            newval = registers.get(e[0]) - int(e[2])
            registers.update({e[0]: newval})
        if newval > curr_max: #part 2
                curr_max = newval

# print(max(registers.values())) #part 1
print(curr_max) #part 2
    