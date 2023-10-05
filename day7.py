##PART 2
from sys import stdin
tree = dict([])
weights = dict([])
curr = ""

for line in stdin:
    line = line.replace(",","")
    elements = line.split()
    if(len(elements) > 2):
        tree.update({elements[0]: elements[3:len(elements)]})
    weights.update({elements[0]: elements[1]})
print(tree)
print(weights)
curr = "xegshds"
prev = curr
while curr != None:
    leafWeights = set([])
    for e in tree.get(curr):
        if(leafWeights.get(weights.get(e))):
            leafWeights.remove(weights.get(e)): 
        else:
            leafWeights.add(weights.get(e)): 
    if(len(leafWeights) == 1):
        prev = curr
        curr = 
    if(len(leafWeights) == 0): #all weights are same
        print(curr)
        break

        








# ##PART 1
# from sys import stdin
# mapping = dict([])
# curr = ""

# for line in stdin:
#     line = line.replace(",","")
#     elements = line.split()
#     curr = elements[0] #just to have something
#     if(len(elements) > 2):
#         for e in range(3, len(elements)):
#             mapping.update({elements[e]: elements[0]})
# while curr != None:
#     prev = curr
#     curr = mapping.get(curr)
# print(prev)
        