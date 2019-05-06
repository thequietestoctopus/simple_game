import arcade
import default_screen


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'PyCom'


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        # set up your game here
        pass


    def on_draw(self):
        """ Render the screen """
        arcade.start_render()
        # your drawing code goes here

        default_screen.draw_grid()


    def update(self, delta_time):
        """ All the logic to move, game logic goes here """
        pass


def main():
    game = MyGame()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

