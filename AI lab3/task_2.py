import sys

# FIRST FIT ALGORITHM CODE
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

# FIRST FIT DECREASING ALGORITHM CODE
def firstFitDecreasing(groups, miniBusCapacity):
    temp = sorted(groups, reverse = True)
    temp = firstFit(temp, miniBusCapacity)
    return temp

# FULL BIN PACKING ALGORITHM CODE
def fullBinPacking(groups, miniBusCapacity):
    bins = []
    groupCopy = groups.copy()
    for _ in range(len(groups)):
        if not groupCopy:
            break
        temp = []
        maximum = max(groupCopy)
        temp.append(maximum)
        groupCopy.remove(maximum)
        for g in groupCopy[:]:
            if sum(temp) + g <= miniBusCapacity:
                temp.append(g)
                groupCopy.remove(g)
        bins.append(temp)  

    return bins


groups = [14, 4, 3, 2, 2, 18, 4, 23, 8, 27, 19, 3, 26, 30, 35, 32]
miniBusCapacity = 50
while(True):
    print("Enter 1 for First Fit")
    print("Enter 2 for First Fit Decreasing")
    print("Enter 3 for Full Bin Packing")
    choice = int(input())

    if choice == 1:
        print(f"\n\nFirst Fit algorithm is {firstFit(groups, miniBusCapacity)}\n\n")
    elif choice == 2:
        print(f"\n\nFirst Fit Decreasing algorithm is {firstFitDecreasing(groups, miniBusCapacity)}\n\n")
    elif choice == 3:
        print(f"\n\nFull Bin Packing algorithm is {fullBinPacking(groups, miniBusCapacity)}\n\n")
    else:
        print("Invalid choice")
        while(True):
            print("Enter 1 for again")
            print("Enter 0 for exit")
            choice1 = int(input())
            if choice1 == 1:
                break
            elif choice1 == 0:
                sys.exit()
            else:
                print("Invalid choice try again")
