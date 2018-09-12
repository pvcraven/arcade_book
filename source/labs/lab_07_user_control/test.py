# Question 6 - Make a list zero

# What you are given
my_list = [3, 4, 2, 54, 11, 9]

# Code to set to zero
for i in range(len(my_list)):
    my_list[i] = 0

# And additional print statement to show it works
print(my_list)



# Question 8 - Sum a list

# Code you are given:
daily_cars_sold_list = [5, 3, 0, 2, 4, 3]

# Correct answer:
total_cars_sold = 0
for daily_cars_sold in daily_cars_sold_list:
    total_cars_sold += daily_cars_sold

# And additional print statement to show it works
print(total_cars_sold)