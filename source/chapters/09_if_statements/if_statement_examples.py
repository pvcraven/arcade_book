# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

# Explanation video: http://youtu.be/pDpNSck2aXQ

# Variables used in the example if statements
a = 4
b = 5
c = 6

# Basic comparisons
if a < b:
    print("a is less than b")

if a > b:
    print("a is greater than than b")

if a <= b:
    print("a is less than or equal to b")

if a >= b:
    print("a is greater than or equal to b")

# NOTE: It is very easy to mix when to use == and =.
# Use == if you are asking if they are equal, use =
# if you are assigning a value.
if a == b:
    print("a is equal to b")

# Not equal
if a != b:
    print("a and b are not equal")

# And
if a < b and a < c:
    print("a is less than b and c")

# Non-exclusive or
if a < b or a < c:
    print("a is less than either a or b (or both)")


# Boolean data type. This is legal!
a = True
if a:
    print("a is true")

if not a:
    print("a is false")

a = True
b = False

if a and b:
    print("a and b are both true")

a = 3
b = 3
c = a == b
print(c)

# These are also legal and will trigger as being true because
# the values are not zero:
if 1:
    print("1")
if "A":
    print("A")

# This will not trigger as true because it is zero.
if 0:
    print("Zero")

# Comparing variables to multiple values.
# The first if statement appears to work, but it will always
# trigger as true even if the variable a is not equal to b.
# This is because "b" by itself is considered true.
a = "c"
if a == "B" or "b":
    print("a is equal to b. Maybe.")

# This is the proper way to do the if statement.
if a == "B" or a == "b":
    print("a is equal to b.")

# Example 1: If statement
temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
print("Done")

# Example 2: Else statement
temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
else:
    print("It is not hot outside")
print("Done")

# Example 3: Else if statement
temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is not hot outside")
print("Done")

# Example 4: Ordering of statements
# Something with this is wrong. What?
temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
elif temperature > 110:
    print("Oh man, you could fry eggs on the pavement!")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is ok outside")
print("Done")

# Comparisons using string/text
# The input statement will ask the user for input and put it in user_name.
user_name = input("What is your name? ")
if user_name == "Paul":
    print("You have a nice name.")
else:
    print("Your name is ok.")
