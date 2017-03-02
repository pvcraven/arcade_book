# Create a class called bird, with the attributes x and change_x, and a method
# called "move". Have it pass the tests below.



# --- Tests. Do not change anything below this line. ---
# Write your code above the line to pass all the tests.

my_bird = Bird()
if my_bird.x == 0:
    print("Test 1 passed")
else:
    print("Test 1 failed")

if my_bird.change_x == 0:
    print("Test 2 passed")
else:
    print("Test 2 failed")

my_bird.change_x = 5
my_bird.move()
my_bird.move()

if my_bird.x == 10:
    print("Test 3 passed")
else:
    print("Test 3 failed")
