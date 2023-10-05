##part 2
indicies = [int(x) for x in open("input.txt", "r")]
i = 0
steps = 0
# print(indicies)
while(i < len(indicies)):
    prev = i
    i = i + indicies[i] #jump
    if(indicies[prev] >= 3):
        indicies[prev] -= 1 #increase prev
    else:
        indicies[prev] += 1 #increase prev
    steps += 1
    # print(indicies)
print(steps)

# ##part 1
# indicies = [int(x) for x in open("input.txt", "r")]
# i = 0
# steps = 0
# while(i < len(indicies)):
#     prev = i
#     i = i + indicies[i] #jump
#     indicies[prev] += 1 #increase prev
#     steps += 1
# print(steps)