"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# Tree trunk
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

# Tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# Another tree, with a trunk and ellipse for top
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)
arcade.draw_arc_filled(200, 370, 60, 80, arcade.csscolor.BISQUE, 0, 90)

# Another tree, with a trunk and triangle for top
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(300, 400, 270, 320, 330, 320, arcade.csscolor.DARK_GREEN)

# Another tree, with a trunk and triangle for top
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(400, 370, 60, 80, arcade.csscolor.DARK_GREEN, 0, 180)


# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
