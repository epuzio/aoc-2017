#part 2, brute force
checksums = []
with open("text.txt", "r") as f:
    for line in f.readlines():
        elements = list(line.split())
        i = 0
        for e1 in elements:
            print(e1)
            i = i+1
            for e2 in elements[i:len(elements)]:
                print(" ", e2)
                if (int(e1) > int(e2)):
                    if (int(e1)%int(e2) == 0):
                        print("appending: ", e1, " ", e2)
                        checksums.append(int(e1)/int(e2))
                        break
                if (int(e1) < int(e2)):
                    if(int(e2)%int(e1) == 0):
                        print("appending 2: ", e1, " ", e2)
                        checksums.append(int(e2)/int(e1))
                        break
print(sum(checksums))











#part 1
# checksums = []
# with open("text.txt", "r") as f:
#     for line in f.readlines():
#         l = list(line.split())
#         currL = 0
#         currS = 999999999999
#         for num in l:
#             if (int(num) > currL):
#                 currL = int(num) 
#             if (int(num) < currS):
#                 currS = int(num) 
#         checksums.append(currL - currS)
# print(sum(checksums))
    

