for row in range(10):

    for j in range(row):
        print(" ", end=" ")

    for j in range(10 - row):
        print(j, end=" ")

    print()