for i in range(1, 10):
    for j in range(1, 10):
        # Extra space?
        if i * j < 10:
            print(" ", end="")

        print(i * j, end=" ")

    # Move down to the next row
    print()