import arcade


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
