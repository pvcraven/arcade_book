# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

# A while loop can be used anywhere a for loop is used:
i = 0
while i < 10:
    print(i)
    i = i + 1

# This is the same as:
for i in range(10):
    print(i)

# It is possible to short hand the code:
# i = i + 1
# With the following:
# i += 1
# This can be done with subtraction, and multiplication as well.
i = 0
while i < 10:
    print(i)
    i += 1

# What would this print?
i = 1
while i <= 2**32:
    print(i)
    i *= 2

# A very common operation is to loop until the user performs
# a request to quit
quit = "n"
while quit == "n":
    quit = input("Do you want to quit? ")

# There may be several ways for a loop to quit. Using a boolean
# to trigger the event is a way of handling that.
done = False
while not done:
    quit = input("Do you want to quit? ")
    if quit == "y":
        done = True

    attack = input("Does your elf attach the dragon? ")
    if attack == "y":
        print("Bad choice, you died.")
        done = True

value = 0
increment = 0.5
while value < 0.999:
    value += increment
    increment *= 0.5
    print(value)

# -- Common problems with while loops --

# The programmer wants to count down from 10
# What is wrong and how to fix it?
i = 10
while i == 0:
    print(i)
    i -= 1

# What is wrong with this loop that tries
# to count to 10? What will happen when it is run?
i = 1
while i < 10:
    print(i)
