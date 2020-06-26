for i in range(10):
    # Print leading spaces
    for j in range(10 - i):
        print(" ", end=" ")
    # Count up
    for j in range(1, i + 1):
        print(j, end=" ")
    # Count down
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    # Next row
    print()

for i in range(10):
    # Print leading spaces
    for j in range(i + 2):
        print(" ", end=" ")
    # Count up
    for j in range(1, 9 - i):
        print(j, end=" ")
    # Count down
    for j in range(7 - i, 0, -1):
        print(j, end=" ")
    print()