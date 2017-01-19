"""
This is a sample program to show how to draw using functions
"""

import arcade


def draw_grass():
    """
    This function draws the grass.
    """
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)


def draw_pine_tree(position_x, position_y):
    """
    This function draws a pine tree.
    """

    # Draw the trunk
    arcade.draw_rectangle_filled(position_x, position_y + 30, 30, 60, arcade.color.BROWN)

    # Draw three levels of triangles
    arcade.draw_triangle_filled(position_x - 70, position_y + 60,
                                position_x + 70, position_y + 60,
                                position_x, position_y + 150,
                                arcade.color.FOREST_GREEN)
    arcade.draw_triangle_filled(position_x - 70, position_y + 100,
                                position_x + 70, position_y + 100,
                                position_x, position_y + 190,
                                arcade.color.FOREST_GREEN)
    arcade.draw_triangle_filled(position_x - 55, position_y + 150,
                                position_x + 55, position_y + 150,
                                position_x, position_y + 230,
                                arcade.color.FOREST_GREEN)

    # Draw the origin point, just for reference.
    arcade.draw_point(position_x, position_y, arcade.color.RED, 4)


def main():
    """
    This is the main function that we call to run our program.
    """
    arcade.open_window("Drawing with Functions", 800, 600)
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
    arcade.start_render()

    # Draw our pretty landscape
    draw_grass()
    draw_pine_tree(70, 90)
    draw_pine_tree(150, 200)
    draw_pine_tree(320, 180)
    draw_pine_tree(520, 190)
    draw_pine_tree(750, 80)

    arcade.finish_render()
    arcade.run()

# Call the main function to get the program started.
main()
