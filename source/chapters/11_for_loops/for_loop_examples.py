"""
Sample For Loops
"""

# Print 'Hi' 10 times
for i in range(10):
    print("Hi")

# Print 'Hello' 5 times and 'There' once
for i in range(5):
    print("Hello")
print("There")

# Print 'Hello' 'There' 5 times
for i in range(5):
    print("Hello")
    print("There")

# Print the numbers 0 to 9
for i in range(10):
    print(i)

# Two ways to print the numbers 1 to 10
for i in range(1, 11):
    print(i)

for i in range(10):
    print(i + 1)

# Two ways to print the even numbers 2 to 10
for i in range(2, 12, 2):
    print(i)

for i in range(5):
    print((i + 1) * 2)

# Count down from 10 down to 1 (not zero)
for i in range(10, 0, -1):
    print(i)

# Print numbers out of a list
for i in [2, 6, 4, 2, 4, 6, 7, 4]:
    print(i)

# What does this print? Why?
for i in range(3):
    print("a")
    for j in range(3):
        print("b")

# What is the value of a?
a = 0
for i in range(10):
    a = a + 1
print(a)

# What is the value of a?
a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1
print(a)

# What is the value of a?
a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)

# What is the value of sum?
sum = 0
for i in range(1, 101):
    sum = sum + i
