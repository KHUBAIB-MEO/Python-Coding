initialVelocity = int(input("Enter the initial velocity: "))
time = int(input("Enter the time: "))
acceleration = int(input("Enter the acceleration: "))
distance = float(initialVelocity * time) + 0.5 * float(acceleration) * time**2
print("The distance is: ", distance)
