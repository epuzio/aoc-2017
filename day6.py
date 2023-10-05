##part 1
with open('input.txt') as fp:
    banks = [int(x) for x in fp.readlines()[0].split()]
    combinations = []
    counter = 0
    while banks not in combinations:
        combinations.append(banks[:])
        max_element = max(banks)
        distD = max_element / (len(banks) -1)
        distR = max_element % (len(banks) -1)
        max_idx = banks.index(max_element)
        # print ("max: ", max_element)
        # print ("idx: ", max_idx)
        # print("d: ", distD)
        # print("remainder: ", distR)
        i = max_idx + 1
        banks[max_idx] = 0
        while max_element > 0:
            banks[(i) % len(banks)] += 1
            i += 1
            max_element = max_element - 1
        counter += 1
        print(banks[:])
    # print(counter) ##if part 1
    print(len(combinations) - combinations.index(banks)) ##if part 2