import arcade

# Create a window
arcade.open_window("Lab 05 - Loopy Lab", 1200, 600)

arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

arcade.start_render()

# Draw squares on bottom
arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

# Draw squares on top
arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)

# Section 1
for row in range(30):
    for column in range(30):
        x = 0  # Instead of zero, calculate the proper x location using column
        y = 0  # Instead of zero, calculate the proper y location using row
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 2
# Use the modulus operator and an if statement to select the color
# Don't loop from 30 to 60 to shift everything over, just add 300 to x.

# Section 3
# Use the modulus operator and an if statement to select the color

# Section 4
# Use the modulus operator and an if statement to select the color

# Section 5

# Section 6

# Section 7

# Section 8

arcade.finish_render()

arcade.run()
