.. _lab-12:

Lab 12: Final Lab
=================

There are two options for the final lab.
A "video game option" and a "text adventure option."

Video Game Option
-----------------

This is it! This is your chance to use your creativity and really show off
what you can create in your own game. More than just passing a test, in this
class you actually get to do something, and create something real.

.. raw:: html


    <figure class='video_float_right'><iframe width='400' height='300' src='http://www.youtube.com/embed/videoseries?list=PLUjR0nhln8ubNGhNeapHNyDfKRPeIBCLO' style='border:none;'></iframe><figcaption>Video: Fall 2015 Game Projects</figcaption></figure>

    <figure class='video_float_right'><iframe width='400' height='300' src='http://www.youtube.com/embed/videoseries?list=PLUjR0nhln8uYp9yKJnGdBN-66di_5G4d2' style='border:none;'></iframe><figcaption>Video: Summer 2015 Game Projects</figcaption></figure>

    <figure class='video_float_right'><iframe width='400' height='300' src='http://www.youtube.com/embed/videoseries?list=PLUjR0nhln8ubHF8yQe0kly1_00sM8S8Pv' style='border:none;'></iframe><figcaption>Video: Spring 2015 Game Projects</figcaption></figure>

    <figure class='video_float_right'><iframe width='400' height='300' src='http://www.youtube.com/embed/videoseries?list=PLUjR0nhln8uZmDrHG5TxL_GboYP1I16sr' style='border:none;'></iframe><figcaption>Video: Fall 2014 Game Projects</figcaption></figure>

    <figure class='video_float_right'><iframe width='400' height='300' src='http://www.youtube.com/embed/videoseries?list=PLUjR0nhln8uYkfd5FSGRfPIbA5BbK03Lb' style='border:none;'></iframe><figcaption>Video: Spring 2014 Game Projects</figcaption></figure>

    <figure class='video_float_right'><iframe width='400' height='300' src='http://www.youtube.com/embed/videoseries?list=PLUjR0nhln8uZZjNv16i-v5Sgi_spcoWQS' style='border:none;'></iframe><figcaption>Video: Fall 2013 Game Projects</figcaption></figure>

    <figure class='video_float_right'><iframe width='400' height='300' src='http://www.youtube.com/embed/videoseries?list=PLUjR0nhln8uYtUcblVH0fxKjobSsT32cp' style='border:none;'></iframe><figcaption>Video: Fall 2012 Game Projects</figcaption></figure>

    <figure class='video_float_right'><iframe width='400' height='300' src='http://www.youtube.com/embed/videoseries?list=PL3765F6910B016383' style='border:none;'></iframe><figcaption>Video: Spring 2012 Game Projects</figcaption></figure>


This final lab is divided into three parts. Each part raises the bar on
what your game needs to be able to do.

Requirements for Part 1:
^^^^^^^^^^^^^^^^^^^^^^^^

* Open up a screen.
* Set up the items to be drawn on the screen.
* Provide some sort of rudimentary player movement via mouse, keyboard,
  or game controller.

**Tips:**

* If your program will involve things running into each other, start by using
  sprites. Do not start by using drawing commands, and expect to add in
  sprites later. It won't work and you'll need start over from scratch.
  This will be sad.
* If you are coding a program like mine sweeper or connect four, do *not* use
  sprites. Since collision detection is not needed, there is no need to mess
  with sprites.
* While you can start with and use any of the example game code from the book
  or arcade.academy, don't just turn these in as Part 1.
  You'll need to add a lot before it qualifies.
* `OpenGameArt.org`_ has a lot of images and sounds you can use royalty-free.
* `Kenney.nl`_ has many images and sounds as well.

.. _OpenGameArt.org: http://opengameart.org
.. _Kenney.nl: http://kenny.nl

Requirements for Part 2:
^^^^^^^^^^^^^^^^^^^^^^^^

For Final Lab Part 2, your game should be mostly functional. A person should
be able to sit down and play the game for a few minutes and have it feel like
a real game. Here are some things you might want to add:

* Be able to collide with objects.
* Players can lose the game if something bad happens.
* On-screen score.
* Some initial sound effects.
* Movement of other characters in the screen.
* The ability to click on mines or empty spots.

Requirements for Part 3:
^^^^^^^^^^^^^^^^^^^^^^^^

For the final part, add in the last polish for your game. Here are some
things you might want to add:

* Multiple levels
* Sounds
* Multiple "lives"
* Title and instruction screens
* Background music
* Heat seeking missiles
* Hidden doors
* A "sweep" action in a minesweeper game or the ability to place "flags"

Text Adventure Option
---------------------

Not interested in a video game? Continue your work from the "Adventure!" game.

Requirements for Part 1:
^^^^^^^^^^^^^^^^^^^^^^^^

1. Rather than have each room be a list of ``[description, north, east, south, west]``
   create a ``Room`` class.
   The class should have a constructor that takes in
   ``(description, north, east, south, west)`` and sets fields for the
   description and all of the directions. Get the program working with the new
   class. The program should be able to add rooms like:

.. code-block:: python

    room = Room("You are in the kitchen. There is a room to the east.", None, 1, None, None)
    room_list.append(room)

    room = Room("You are in the living room. There is a room to the west.", None, None, 0, None)
    room_list.append(room)

Later the program should be able to refer to fields in the room:

.. code-block:: python

    current_room = room_list[current_room].north

2. Perhaps expand the game so that a person can travel up and down.
   Also expand it so the person can travel northwest, southwest, northeast, and southeast.
3. Add a list of items in your game.

    1. Create a class called ``Item``.
    2. Add fields for the item's room number, a long description, and a short
       name. The short name should only be one word long. This way the user
       can type ``get key`` and the computer will know what object he/she is
       referring to. The description will be what is printed out. Like
       ``There is a rusty key here.``
    3. Create a list of items, much like you created your list of rooms.
    4. If the item is in the user's room, print the item's description.
    5. Test, and make sure this works.

Requirements for Part 2:
^^^^^^^^^^^^^^^^^^^^^^^^

1. Change your command processing, so rather than just allowing the user to only type in directions, the user will now start having other options. For example, we want the user to also be able to type in commands such as get key, inventory or wave wand.

    1. To do this, don't ask the user What direction do you want to go? Instead ask the user something like What is your command?
    2. Split the user input. We need a variable that is equal to the first command they type, such as get and a different variable equal to the second word, such as key.

        1. Use the split method that's built into Python strings. For example:
           ``command_words = user_command.split(" ")``
           This will split what the user types into a list. Each item
           separated out based on spaces.
        2. Update your code that processes the user typing in directions, to
           check command_words[0] instead of whatever you had before.

2. Add a get command.

    1. Add a check for a get command in your if/elif chain that is now just
       processing directions.
    2. Search the item list until you find an object that matches what the user
       is trying pick up.
    3. If the object isn't found, or if the object isn't in the current room,
       print an error.
    4. If the object is found and it is in the current room, then set the
       object's room number to -1.

3. Add a command for "inventory" that will print every object who's room number
   is equal to -1.
4. Add the ability to drop an object.
5. Add the ability to use the objects. For example "use key" or "swing sword"
   or "feed bear."

Requirements for Part 3:
^^^^^^^^^^^^^^^^^^^^^^^^

Expand the game some more. Try some of these ideas:

1. Create a file format that allows you to load the rooms and objects from a file rather than write code for it.
2. Have monsters with hit points.
3. Split the code up into multiple files for better organization.
4. Remove globals using a main function as shown at the end of the chapter about functions.
5. Have objects with limited use. Like a bow that only has so many arrows.
6. Have creatures with limited health, and weapons that cause random damage and have a random chance to hit.
