num = int(input("Enter number: "))
previous = 0
next = 1
for i in range(1, num):
    print(previous, end=" ")
    result = next
    next = previous + next
    previous = result