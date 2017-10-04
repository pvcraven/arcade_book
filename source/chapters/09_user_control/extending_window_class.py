import arcade


class MyWindow(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

window = MyWindow(640, 480, "Drawing Example")

arcade.run()
