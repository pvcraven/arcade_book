import arcade


class MyWindow(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(50, 50, 15, arcade.color.AUBURN)

window = MyWindow(640, 480, "Drawing Example")

arcade.run()
