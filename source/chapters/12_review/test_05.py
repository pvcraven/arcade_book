# Write a function that figures out if a number is even or odd.
# Make it work for every number, not just the ones we test here.



# --- Tests. Do not change anything below this line. ---
# Write your code above the line to pass all the tests.

if even_or_odd(0) == "Even":
    print("Test 1 passed")
else:
    print("Test 1 failed")

if even_or_odd(1) == "Odd":
    print("Test 2 passed")
else:
    print("Test 2 failed")

if even_or_odd(-1) == "Odd":
    print("Test 3 passed")
else:
    print("Test 3 failed")

if even_or_odd(100) == "Even":
    print("Test 4 passed")
else:
    print("Test 4 failed")

if even_or_odd(1001) == "Odd":
    print("Test 5 passed")
else:
    print("Test 5 failed")
