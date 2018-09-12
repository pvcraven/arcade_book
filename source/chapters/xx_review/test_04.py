# Write a function called how_is_the_temperature that returns a string based
# on the temperature passed into it.
# Try to get this to work based on temperature ranges, rather than exact
# temperatures.



# --- Tests. Do not change anything below this line. ---
# Write your code above the line to pass all the tests.

if how_is_the_temperature(95) == "Hot":
    print("Test 1 passed")
else:
    print("Test 1 failed")

if how_is_the_temperature(85) == "Warm":
    print("Test 2 passed")
else:
    print("Test 2 failed")

if how_is_the_temperature(70) == "Great":
    print("Test 3 passed")
else:
    print("Test 3 failed")

if how_is_the_temperature(50) == "Cool":
    print("Test 4 passed")
else:
    print("Test 4 failed")

if how_is_the_temperature(30) == "Cold":
    print("Test 5 passed")
else:
    print("Test 5 failed")
