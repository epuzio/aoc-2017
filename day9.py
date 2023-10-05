##part 2
score = 0
with open('input.txt') as inp:
    line = inp.readline()
prevchar = '0'
num_open_brace = 0
total_chars_in_garbage = 0
curr_chars_in_garbage = 0
garbage = False
just_set_garbage = False
for char in line:
    if prevchar == '!':
        prevchar = '0'
        continue
    if garbage == False:
        if char == '<':
            garbage = True
            just_set_garbage = True
    if char == '>':
        total_chars_in_garbage += curr_chars_in_garbage
        curr_chars_in_garbage = 0
        garbage = False
    if garbage == True: 
        if char != '!':
            if just_set_garbage == False:
                curr_chars_in_garbage += 1
    prevchar = char
    just_set_garbage = False
print(total_chars_in_garbage)












# ##part 1
# score = 0
# with open('input.txt') as inp:
#     line = inp.readline()
# prevchar = '0'
# num_open_brace = 0

# garbage = False
# for char in line:
#     # print(char, prevchar, garbage)
#     if prevchar == '!':
#         prevchar = '0'
#         continue
#     if char == '<':
#         garbage = True
#     if char == '>':
#         garbage = False
#     if garbage == False:
#         if char == '{':
#             num_open_brace += 1
#         if char == '}':
#             score += num_open_brace
#             num_open_brace -= 1
#     prevchar = char
# print(score)