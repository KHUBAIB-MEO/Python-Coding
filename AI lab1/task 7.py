sideA = int(input("Enter the first side: "))
sideB = int(input("Enter the second side: "))
sideC = int(input("Enter the third side: "))

if sideA == sideB and sideB == sideC:
    print("Equilateral Triangle")
elif sideA == sideB or sideB == sideC or sideA == sideC:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
