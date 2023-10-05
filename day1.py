int total = 0
int inp = list(input())
halflen = int(len(inp)/2)
for c in range(halflen):
    if inp[c] == inp[c+halflen]:
        total = total + (inp[c]*2)
print(total)
