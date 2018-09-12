"""
This is a sample program to show how to draw using functions
"""

import arcade


def draw_grass():
    """
    This function draws the grass.
    """
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)


arcade.open_window(800, 600, "Drawing with Functions")
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()

# Call our function to draw the grass
draw_grass()

arcade.finish_render()
arcade.run()
