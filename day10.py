from sys import stdin
numlistsize = 256
numlist = list(range(numlistsize))
for line in stdin:
    line = line.replace(",","")
    inputs = [int(x) for x in line.split()]
skipsize = 0
currentposition = 0
for length in inputs:
    if length + currentposition <= numlistsize: #no wrap
        toreverse = numlist[currentposition:currentposition+length]
        toreverse.reverse()
        temp = numlist[0:currentposition] + toreverse + numlist[currentposition+length:numlistsize]
        numlist = temp
    if length + currentposition > numlistsize: #wrap
        startindex = length - (numlistsize - currentposition)
        toreverse = numlist[currentposition:numlistsize] + numlist[0:startindex]
        toreverse.reverse()
        temp = toreverse[length-startindex:length] + numlist[startindex:currentposition] + toreverse[0:length-startindex]
        numlist = temp
    currentposition = (currentposition + skipsize + length) % numlistsize
    skipsize += 1
print('numlist:',numlist)












# if length + currentposition <= numlistsize: #no wrap
#         toreverse = numlist[currentposition:length]
#         toreverse.reverse()
#         numlist = numlist[0:currentposition], toreverse, numlist[currentposition+length:-1]
#     if length + currentposition > numlistsize: #wraps around
#         startindex = (currentposition + length) % numlistsize
#         toreverse = numlist[currentposition:-1] 
#         #numlist[0:startindex])
#         toreverse.reverse()
#         numlist = toreverse[0:startindex], numlist[startindex:currentposition], toreverse[currentposition:-1]
   

    

