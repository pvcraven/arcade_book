Classes Constructors and Attributes
===================================

Throughout this course we've been using variables to store *a* value.
We just learned how to store *multiple* values using a list.
The next step is **object-oriented programming**. This type of programming
has three advantages.
One, we can group multiple variables together in a single record. Two, we can
associate functions with that group of data. Three, we'll can use
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
pattern of lower-case for variables and upper-case for classes makes it easy
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

Methods follow this rule too, with one exception. The ``self`` parameter
refers to memory associated with each instance of the class. We can use that
``self`` to create variables that *keep* their value for as long as the object exists.
We call variables that exist as part of the class **attributes**.
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
about. This is not the case.

Take a look at this code:

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

        # This runs, creates a new attribute but with the wrong name.
        my_address.naem = "Dr. Smith"

        # This does work:
        my_address.name = "Dr. Smith"

    main()

This code will run without generating an exception, but it still isn't
correct. Line 15 creates a variable called ``name``, but it is completely
different than the name that is part of ``Address``. So we think we've set
the name, but we haven't.

Line 18 does refer to ``Address``, but not ``my_address``. Frustratingly it
runs without alerting us to an error, but the code isn't modifying
``my_address``. Instead it sets something called a static variable,
which we'll talk about later.

Think of it this way. If you are in a room of people, saying "Age is 18" is
confusing. Saying "Human's age is 18" is also confusing. Saying "Sally's
age is 18" is ideal, because you are saying which instance of human you
are referring to. You have to do this with programming, even if there is
only one human in the room.

Line 22 runs, but it creates a new attribute called ``naem`` instead of setting
the desired attribute ``name``.

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

Take a look at this code, where we represent a dog using
a class.
Unfortunately, there's a terrible problem with the code. When we create
a dog, the dog has no name. Dogs should have names!
`Only horses in the desert can have no name <https://en.wikipedia.org/wiki/A_Horse_with_No_Name>`_.

.. code-block:: python
    :linenos:
    :emphasize-lines: 4

    class Dog():
        def __init__(self):
            """ Constructor. Called when creating an object of this type. """
            self.name = ""


    def main():
        my_dog = Dog()


    main()

We can modify the code in our constructor to keep this from happening.
First, let's add a ``print`` statement to our ``__init__`` to demonstrate
that it is really being called.

.. code-block:: python
    :linenos:
    :emphasize-lines: 5

    class Dog():
        def __init__(self):
            """ Constructor. Called when creating an object of this type. """
            self.name = ""
            print("A new dog is born!")


    def main():
        # This creates the dog
        my_dog = Dog()

When the program is run, it will print this:

.. code-block:: text

    A new dog is born!

When a Dog object is created on line 10, the ``__init__`` function is "magically"
called and the message is printed to the screen.

We can add a parameter to our constructor, so that it requires us to pass in a
name for the dog. Try running this code.

.. code-block:: python
    :linenos:
    :emphasize-lines: 2, 4

    class Dog():
        def __init__(self, new_name):
            """ Constructor. Called when creating an object of this type. """
            self.name = new_name
            print("A new dog is born!")


    def main():
        # This creates the dog
        my_dog = Dog()


    main()

You should get an error that looks like:

.. code-block:: text

  File "c:/my_project/test.py", line 10, in main
    my_dog = Dog()
  TypeError: __init__() missing 1 required positional argument: 'new_name'

The computer is saying it is missing a value for the ``new_name`` parameter. It
won't let the dog be created without a name. We can fix that up by adding a
name when we create the dog.

.. code-block:: python
    :linenos:
    :emphasize-lines: 10

    class Dog():
        def __init__(self, new_name):
            """ Constructor. Called when creating an object of this type. """
            self.name = new_name
            print("A new dog is born!")


    def main():
        # This creates the dog
        my_dog = Dog("Fluffy")


    main()

Notice in line 4 we take the value that was passed in as a parameter and assign
``self.name`` to have that same value. Without this line, the dog's name
won't get set.

As programmers sometimes get tired of making up variable names, it is completely normal
to see code like this:

.. code-block:: python
    :linenos:
    :emphasize-lines: 2, 4

    class Dog():
        def __init__(self, name):
            """ Constructor. Called when creating an object of this type. """
            self.name = name
            print("A new dog is born!")


    def main():
        # This creates the dog
        my_dog = Dog("Fluffy")


    main()

Though it may seem strange at first, we have two variables at work, not one.
The first variable is
``name``, and that variable is assigned as a parameter when we call the ``Dog``
constructor. It goes away as soon as the ``Dog`` constructor is done, and is
forgotten about. The second variable is ``self.name``, and that variable
is complete different than ``name``. Its value will stay after the constructor
is done.

Typing Attributes
-----------------


Data Classes
------------

It is common to write code like this:

.. code-block:: python
    :linenos:

    class Address:
        def __init__(self,
                     name: str = "",
                     line1: str = "",
                     line2: str = "",
                     city: str = "",
                     state: str = "",
                     zip_code: str = ""
                     ):
            self.name: str = name
            self.line1: str = line1
            self.line2: str = line2
            self.city: str = city
            self.state: str = state
            self.zip_code: str = zip_code


It seems like the code is twice as long as it needs to be.
If your ``__init__`` method is only going to take in data
fields and assign attribute values, you can use a **dataclass**.

Starting with Python 3.8, you can write the same thing using only:

.. code-block:: python
    :linenos:

    @dataclass
    class Address:
        name: str = ""
        line1: str = ""
        line2: str = ""
        city: str = ""
        state: str = ""
        zip_code: str = ""