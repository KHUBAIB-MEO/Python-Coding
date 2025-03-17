def firstFit(groups, miniBusCapacity):
    temp = []
    bin = []
    groupCopy = groups[:]
    for i in range (0, len(groupCopy) - 1):
        for g in groupCopy:
            if sum(temp) + g <= miniBusCapacity:
                temp.append(g)
        if len(groupCopy) != 0:        
            bin.append(temp)
        for i in range (0, len(temp)):
            if groupCopy.__contains__(temp[i]):
                groupCopy.remove(temp[i])
        temp = []
    return bin

groups = [2, 2, 3, 3, 3, 3, 4, 4, 4, 6, 7, 7]
miniBusCapacity = 12
bin = firstFit(groups, miniBusCapacity)
print(f"\n\nFirst Fit algorithm is {bin}")
print(f"total number of bin are {len(bin)}\n\n")