##part 2
valid = 0
with open("input.txt", "r") as inp:
    for line in inp.readlines():
        allElements = []
        elementsWithoutDuplicates = set([])
        for element in line.split():
            # print(''.join(sorted(element)))
            allElements.append(''.join(sorted(element)))
            elementsWithoutDuplicates.add(''.join(sorted(element)))
        if(len(allElements) == len(elementsWithoutDuplicates)):
            valid += 1
        # print("\n")
print(valid)





# ##part 1
# valid = 0
# with open("test.txt", "r") as inp:
#     for line in inp.readlines():
#         allElements = list(line.split())
#         elementsWithoutDuplicates = set(line.split())
#         if(len(allElements) == len(elementsWithoutDuplicates)):
#             valid += 1
# print(valid)
