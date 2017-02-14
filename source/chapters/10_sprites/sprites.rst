.. sectnum::
    :start: 10

.. _sprites:

Sprites
=======

Our games need support for handling objects that collide. Balls bouncing off 
paddles, laser beams hitting aliens, or our favorite character collecting a 
coin. All these examples require collision detection.

The Arcade library has support for sprites. A sprite is a two dimensional 
image that is part of the larger graphical scene. Typically a sprite will 
be some kind of object in the scene that will be interacted with like a car, 
frog, or little plumber guy.

.. image:: sprite.png
	:width: 250px

Originally, video game consoles had built-in hardware support for sprites. 
Now this specialized hardware support is no longer needed, but we still use 
the term "sprite."

Basic Sprites and Collisions
----------------------------

Let's step through an example program that uses sprites. This example shows how 
to create a screen of sprites that are coins, and collect them using a sprite 
that is a character image 
controlled by the mouse as shown in the figure below. The program keeps "score" 
on how many coins have been collected. The code for this example may be found at: 

http://arcade.academy/examples/sprite_collect_coins.html

.. figure:: sprite_collect_coins.png

	Example Sprite Game

Getting the Application Started
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first few lines of our program start off like other games we've done. We 
import a couple libraries. Set a couple constants for the size of the screen,
and a new constant that we will use to scale our graphics to half their original
size.

.. code-block:: Python
    :caption: Start of our sprite example

	import random
	import arcade

	SPRITE_SCALING = 0.5

	SCREEN_WIDTH = 800
	SCREEN_HEIGHT = 600


	class MyApplication(arcade.Window):
	    # --- Class methods will go here

	window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
	window.setup()

	arcade.run()

The Constructor
^^^^^^^^^^^^^^^

What's next? We need to add our methods to the ``MyApplication`` class. 
We'll start with our ``__init__`` method. This is the method we use to 
initialize our variables. Here it is:

.. code-block:: Python
    :caption: Constructor for MyApplication

    def __init__(self, width, height):

    	# Call the parent class initializer
        super().__init__(width, height)

        # Variables that will hold sprite lists
        self.all_sprites_list = None
        self.coin_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

The variables we are creating:

* ``all_sprites_list``:  This is a special list that we will add all our sprites
  to. By having all the sprites in a single list, we can draw them all in a 
  single command.
* ``coin_list``: This is a list of all the coins. We wille be checking if the
  player touches any sprite in this list.
* ``player_sprite``: This points to our player's sprite. It is the sprite
  we will move, and we'll check to see if it 
* ``score``: This keeps track of our score.

We use a command built into the parent ``Window`` class called
``set_mouse_visible`` to make the mouse not visible. Finally we set the 
background color.

The Setup Function
^^^^^^^^^^^^^^^^^^

Next up, we have a ``setup`` method. In the first code example, we have the
code that calls this function near the end: ``window.setup()``. 

This setup code
could be moved into the ``__init__`` method. Why is it separate? Later on
if we want to add the ability to "play again", we can just call the setup 
function. If the code to set up the window is mixed with the code to set 
up the game, then it is more difficult to program that functionality. Here
we start by keeping them separate.

.. code-block:: Python
    :caption: Setup method for our application

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = arcade.Sprite("images/character.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)

        for i in range(50):

            # Create the coin instance
            coin = arcade.Sprite("images/coin_01.png", SPRITE_SCALING / 3)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.all_sprites_list.append(coin)
            self.coin_list.append(coin)

How does this code work?

First, we need some lists to hold our sprites. We could do something like
this:

.. code-block:: Python

    all_sprites_list = []

But wait! ``all_sprites_list`` is an instance variable that's part of our class.
we need to prepend it with ``self.``.

.. code-block:: Python

    self.all_sprites_list = []

However, the Arcade library has a class especially for handling sprite lists.
This class is called ``SpriteList``. So instead of creating an empty list with
``[]``, we will create a new instance of the ``SpriteList`` class:

.. code-block:: Python

    self.all_sprites_list = SpriteList()

Except that doesn't work. Why? ``SpriteList`` is in the Arcade library. We
need to prepend any reference to things in the Arcade library with ``arcade``
of course, so now we have:

.. code-block:: Python

    self.all_sprites_list = arcade.SpriteList()

We need a separate list for just coins. This list won't have the player. We also
need to reset our score to 0.

.. code-block:: Python

    self.coin_list = arcade.SpriteList()

    self.score = 0

Now we need to create out sprite. The name of the class that represents sprites
is called ``Sprite``. It takes two paramters. A path to the image we will be
using, and how big to scale it.

.. code-block:: Python

    self.player_sprite = arcade.Sprite("images/character.png", SPRITE_SCALING)    

.. figure:: character.png
    
    character.png

.. figure:: coin_01.png
    
    coin_01.png
    
The On Draw Method
^^^^^^^^^^^^^^^^^^

The On Mouse Motion Method
^^^^^^^^^^^^^^^^^^^^^^^^^^

The Animate Method
^^^^^^^^^^^^^^^^^^