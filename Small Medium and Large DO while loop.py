x = 0
while True:    #This simulates a Do Loop
    print("Enter you first number.")
    a = int(input())
    print("Enter your second number.")
    b = int(input())
    print("Enter your third number.")
    c = int(input())
    small = a
    if b < small:
        small = b
    if c < small:
        small = c
    large = a
    if b > large:
        large = b
    if c > large:
        large = c
    if a != small and a != large:
        medium = a
    if b != small and b != large:
        medium = b
    if c != small and c != large:
        medium = c
    print("The smallest number is " + str(small))
    print(" Largest number is =" + str(large))
    print("The medium number is =" + str(medium))
    x = x + 1
    if not(x < 3): break   #Exit loop
