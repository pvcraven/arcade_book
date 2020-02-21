Classes Constructors and Attributes
===================================

Throughout this course we've been using variables to store *a* value.
We just learned how to store *multiple* values using a list.
The next step is **object-oriented programming**. This type of programming
has three advantages.
One, we can group multiple variables together in a single record. Two, we can
associate functions with that group of data. Third, we'll use
something called **inheritance** which allows us to take a base set of code
and extend it, without needing to rewrite it from scratch.

Using Classes and Objects to Group Data
---------------------------------------

Grouping related data together using object-oriented programming
can simplify our code.
For example, think of an adventure game.
Each character in an adventure game needs data, such as a name,
what they look like, how many hit points they have, their armor,
and how fast they can move.

Without classes, our Python code to store the information might look like
this:

.. code-block:: python
    :linenos:

    name = "Link"
    outfit = "Green"
    max_hit_points = 50
    current_hit_points = 50
    armor_amount = 6
    max_speed = 10

In order to do anything with this character, we'll need to pass all that data to a function.
With so many parameters, that function gets complex and hard to manage.

.. code-block:: python
    :linenos:

    def display_character(name, outfit, max_hit_points, current_hit_points, armor, max_speed):
        print(name, outfit, max_hit_points, current_hit_points)

As our game expands, we might start adding more character attributes, such
weapons, magic, special abilities, and more. To do that we'd have
to go through each function
in our program that works with the player character and redo the parameters.

Keeping all these data points organized becomes difficult very quickly.
How do
we keep a monster's hit points separated from the player's hit points?
Because when we add monsters to the game, they'll have their own
attributes. In fact, just about every item in an adventure game has
attributes.

There needs to be a better way. Somehow our
program needs to package up those data fields for easy management.

Defining Classes
----------------

A better way to manage multiple data attributes is to define a structure
to hold the information. We can give that "grouping" of information a
name, like *Character* or *Address*. This can be easily done in Python and any
other modern language by using a **class**.

Defining the Class
^^^^^^^^^^^^^^^^^^

Let's code an example using our adventure character. First, we tell the computer
we are defining a class with the ``class`` keyword, and then we give the class a name
that starts with a capital letter. Just like with functions and loops, we end
the statement with a colon, and everything associated with the class will be
indented below it:

.. code-block:: python
    :linenos:

    class Character:

Unlike variables, all class names should start with a capital letter.
While you *can* use a lower-case variable, you never should. Following this
pattern of lower-case for variables and upper-case for classes make it easy
to tell which is which.

Next, we normally put into triple-quote comments a description of the class.

.. code-block:: python
    :linenos:

    class Character:
        """
        This is a class that represents the player character.
        """

Yes, the code will run fine without any comments. It is optional.
However good documentation is important to maintainable
code, even if you are the only person using the code.

The cool feature about creating comments this way,
is the text can be pulled out automatically to form a website
for your API documentation.
All the classes and functions in the Arcade library's API are
created with these comments. You can see the result here:

https://arcade.academy/arcade.html

For each of those examples, you can click on the "source" link and quickly
go to the source code for that function or class.

Defining the Init Function
^^^^^^^^^^^^^^^^^^^^^^^^^^

Any time we create a new instance of a class, we need code that will create our
attributes (variables) and set them to default values. In Python, this is the ``__init__``
method.

This strangely named method needs a bit of explanation.

First, any function in a class is called a **method**, rather than a function. This
helps us keep straight what is in a class, and what isn't.

Second, the initialization method is a **magic method** that is called automatically.
Yes, Python programmers actually call methods that are automatically called
"magic."

Third, to signify a method is magic, Python surrounds the method name with double
underscores. Two underscores in the front, and two underscores in the back.
The short-name for double-underline is **dunder**, and these
magic methods are also known as **dunder methods**.

.. code-block:: python
    :linenos:

    class Character:
        """
        This is a class that represents the player character.
        """
        def __init__(self):
            """ This is a method that sets up the variables in the object. """

The most common mistakes people make when typing this in is to use only one underscore
before and after the ``init``, and to forget that there is a space between ``def`` and the
first underscore.

All methods in a class have at least one parameter, and the first parameter is always
``self``. We'll explain about ``self`` in the next section.

Defining Class Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^

Remember back to our chapter on functions, that any variable created inside a function
is forgotten about after the function is done running? If you want to keep anything,
you need to return it as a value.

Methods in classes follow this rule as well, with one exception. The ``self`` parameter
refers to memory associated with each instance of the class. We can use that
``self`` to create variables that *keep* their value for as long as the object exists.
We call variables these that exist as part of the class **attributes**.
They must be set to an default value. That value is often 0, an empty string,
or the special value ``None``.

.. code-block:: python
    :linenos:

    class Character:
        """
        This is a class that represents the player character.
        """
        def __init__(self):
            """ This is a method that sets up the variables in the object. """
            self.name = ""
            self.outfit = ""
            self.max_hit_points = 0
            self.current_hit_points = 0
            self.armor_amount = 0
            self.max_speed = 0

In the example above, if we had failed to put ``self.`` in front,
the computer would completely forget about the variables once the ``__init__`` function
was done.

Here's another example, we are defining a class called ``Address`` which has
attributes for each field of a US mailing address.

.. code-block:: python
    :linenos:

    class Address():
        """ Hold all the fields for a mailing address. """
        def __init__(self):
            """ Set up the address fields. """
            self.name = ""
            self.line1 = ""
            self.line2 = ""
            self.city = ""
            self.state = ""
            self.zip = ""

In the code above, ``Address`` is the class name. The variables in the class,
such as ``name`` and ``city``, are called **attributes** or **fields**.

.. sidebar:: Constructor?

    There is some debate about calling ``__init__`` a constructor. In some languages
    a constructor is called *before* the computer sets aside memory for the object.
    In Python the
    ``__init__`` method is actually called *after* this happens. For our purposes,
    the distinction is not important.

The ``__init__`` is a special function that you may also hear referred to
as a **constructor**. If you are programming in other languages, the term
constructor is a generic term used to refer to whatever that language's
equivalent to the ``__init__`` method is.

The ``self.`` is kind of like the pronoun *my*. When inside the class
``Address`` we are talking about *my* name, *my* city, etc. We don't want to
use ``self.`` outside the class. Why? Because just like the pronoun "my," it means someone
totally different when said by a different person!

Creating Objects
----------------

The class code *defines* a class but it does not actually create an **instance**
of one. The code told the computer what fields an address has,
but we don't actually have an address yet.
We can define a class without creating one just like we can define a function
without calling it.

To create an instance of the ``Address`` class, we use the following code:

.. code-block:: python
    :linenos:

    # Create an address
    home_address = Address()

We need a variable that will point to our address. In this case, we've called it
``home_address``. Then we follow that with parentheses, which will "magically"
call the ``__init__`` method where we set up the fields/attributes for the class.

In this case, ``Address`` is a class. It defines what an address looks like.
The ``home_address`` variable points to an **object**. An object is an instance of
a class. It is the actual address. As another example, "Human" is a class, while
"Samantha" and "Pete" and instances of the class.

You can set the attributes with the class using the dot operator. First, use
a variable that points to our object, then a period, followed by the attribute
name.

.. code-block:: python
    :linenos:

    # Create an address
    home_address = Address()

    # Set the fields in the address
    home_address.name = "John Smith"
    home_address.line1 = "701 N. C Street"
    home_address.line2 = "Carver Science Building"
    home_address.city = "Indianola"
    home_address.state = "IA"
    home_address.zip = "50125"

A second variable can be created that points to a completely different instance
of the ``Address`` class:

.. code-block:: python
    :linenos:

    # Create another address
    vacation_home_address = Address()

    # Set the fields in the address
    vacation_home_address.name = "John Smith"
    vacation_home_address.line1 = "1122 Main Street"
    vacation_home_address.line2 = ""
    vacation_home_address.city = "Panama City Beach"
    vacation_home_address.state = "FL"
    vacation_home_address.zip = "32407"

    print("The client's main home is in " + home_address.city)
    print("His vacation home is in " + vacation_home_address.city)

Common Mistakes Creating Objects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first common mistake when creating objects is to forget the parentheses:

.. code-block:: python
    :linenos:

    # ERROR - Forgot the parentheses after Address
    home_address = Address

The terrible thing about this mistake is that the program won't stop or give
you an error. Try running the example we just created with the two different
addresses. Take out the parentheses. The program runs without error, but
both the vacation home and the home address say we are in Panama City! That's
because without the parentheses we don't create a new address, we just use the
same block of memory and write the new information over the old, so everything
points to the same address.

Another very common mistake when working with classes is to forget to specify which
instance of the class you want to work with. If only one address is created, it
is natural to assume the computer will know to use that address you are talking
about. This is not the case. See the example below:

.. code-block:: python
    :linenos:

    class Address:
        def __init__(self):
            self.name = ""
            self.line1 = ""
            self.line2 = ""
            self.city = ""
            self.state = ""
            self.zip = ""

    def main():
        # Create an address
        my_address = Address()

        # Alert! This does not set the address's name!
        name = "Dr. Smith"

        # This doesn't set the name for the address either
        Address.name = "Dr. Smith"

        # This does work:
        my_address.name = "Dr. Smith"

    main()

This code will run without generating an exception, but it still isn't
correct. Line 15 creates a variable called ``name``, but it is completely
different than the name that is part of ``Address``. So we think we've set
the name, but we haven't.

Line 18 does refer to ``Address``, but not ``my_address``. Frustratingly it
runs without alerting us to an error, but the code isn't modifying
``my_address``. Instead it starts treating our ``Address`` class
as an object, which the class goes along with.

Think of it this way. If you are in a room of people, saying "Age is 18" is
confusing. Saying "Human's age is 18" is also confusing. Saying "Sally's
age is 18" is ideal, because you are saying which instance of human you
are referring to. You have to do this with programming, even if there is
only one human in the room.

Using Objects in Functions
--------------------------

Putting lots of data fields into a class makes it easy to pass data in and out
of a function. In this example, the function takes in an address as a
parameter and prints it out on the screen. It is not necessary to pass
parameters for each field of the address.

.. code-block:: python
    :linenos:
    :caption: Passing in an object as a function parameter

    # Print an address to the screen
    def print_address(address):
        print(address.name)
        # If there is a line1 in the address, print it
        if len(address.line1) > 0:
            print(address.line1)
        # If there is a line2 in the address, print it
        if len(address.line2) > 0:
            print( address.line2 )
        print(address.city + ", " + address.state + " " + address.zip)


    def main():
        print_address(home_address)
        print()
        print_address(vacation_home_address)


    main()

Customizing the Constructor
---------------------------

There's a terrible problem with our class for Dog listed below. When we create
a dog, by default the dog has no name. Dogs should have names! We should not
allow dogs to be born and then never be given a name. Yet the code below allows
this to happen, and that dog will never have a name.

.. code-block:: python
    :linenos:

    class Dog():
        def __init__(self):
            self.name = ""


    def main():
        my_dog = Dog()


    main()

Python doesn't want this to happen. That's why Python classes have a special
function that is called any time an instance of that class is created. By
adding a function called a constructor, a programmer can add code that is
automatically run each time an instance of the class is created. See the
example constructor code below:


.. code-block:: python
    :linenos:

    class Dog():
        def __init__(self):
            """ Constructor. Called when creating an object of this type. """
            self.name = ""
            print("A new dog is born!")


    def main():
        # This creates the dog
        my_dog = Dog()

The constructor starts on line 2. It must be named ``__init__``. There are
two underscores before the init, and two underscores after.
A common mistake is to only use one.

The constructor must take in self as the first parameter just like other
methods in a class. When the program is run, it will print:

.. code-block:: text

    A new dog is born!

When a Dog object is created on line 8, the ``__init__`` function is automatically called and the message is printed to the screen.

Typing Attributes
-----------------


Data Classes
------------

