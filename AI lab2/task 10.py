def rupeesToDollar(rupees):
    rupees = rupees * 0.0036
    return rupees

def rupeesToTurkishLira(rupees):
    rupees = rupees * 0.13
    return rupees

def rupeesToChineseYuan(rupees):
    rupees = rupees * 0.026
    return rupees

def rupeesToUAEdirham(rupees):
    rupees = rupees * 0.012
    return rupees

def rupeesToSaudiRiyal(rupees):
    rupees = rupees * 0.013
    return rupees

rupees = float(input("Enter rupees for conversion: "))

while(1):
    print("Enter 1 for Dollar conversion")
    print("Enter 2 for Turkish Lira conversion")
    print("Enter 3 for Chinese Yuan conversion")
    print("Enter 4 for UAE Dirham conversion")
    print("Enter 5 for Saudi Riyal conversion")
    choice = int(input())

    if choice == 1:
        dollar = rupeesToDollar(rupees)
        print(f"{rupees} in dollar conversion = {dollar}")
    elif choice == 2:
        lira = rupeesToTurkishLira(rupees)
        print(f"{rupees} in lira conversion = {lira}")
    elif choice == 3:
        yuan = rupeesToChineseYuan(rupees)
        print(f"{rupees} in yuan conversion = {yuan}")
    elif choice == 4:
        dirham = rupeesToUAEdirham(rupees)
        print(f"{rupees} in dirham conversion = {dirham}")
    elif choice == 5:
        riyal = rupeesToSaudiRiyal(rupees)
        print(f"{rupees} in riyal conversion = {riyal}")
    else:
        print("Invalid choice")
