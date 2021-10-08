.. _classes_chapter:

Classes, Constructors, and Attributes
=====================================

.. image:: ../../images/video.svg
    :class: video-image-h1
    :target: https://youtu.be/7BfXwcapLFQ
    :alt: Video link

* Video: https://youtu.be/7BfXwcapLFQ
* Slides: https://slides.com/paulcraven/14-classes-constructors-and-attributes/

.. image:: construction.svg
    :width: 35%
    :class: right-image

Throughout this course we've been using variables to store *a* value.
We just learned how to store *multiple* values using a list.
The next step is **object-oriented programming**. This type of programming
has three advantages.
One, we can group multiple variables together in a single record. Two, we can
associate functions with that group of data. Three, we can use
something called **inheritance** which allows us to take a base set of code
and extend it, without needing to rewrite it from scratch.

Using Classes and Objects to Group Data
---------------------------------------

.. image:: character.svg
    :width: 15%
    :class: right-image

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

As our game expands, we might start adding more character attributes, such as
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
program needs to package up all those data fields for easy management.

Defining Classes
----------------

A better way to manage multiple data attributes is to define a structure
to hold the information. We can give that "grouping" of information a
name, like *Character* or *Address*. This can be easily done in Python and any
other modern language by using a **class**. Each data item we group into
the class is called a **field**, **attribute**, or **instance variable**. These
terms may be used interchangeably, as they mean the same thing.

.. _define-class:

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

https://api.arcade.academy/en/latest/arcade.html

For each of those examples, you can click on the "source" link and quickly
go to the source code for that function or class.

.. _define-init-method:

Defining the Init Function
^^^^^^^^^^^^^^^^^^^^^^^^^^

Any time we create a new instance of a class, we need code that will create our
attributes (variables) and set them to default values. In Python, this is the ``__init__``
method.

This strangely named method needs a bit of explanation.

First, any function in a class is called a **method**, rather than a function. This
helps us keep straight what is in a class, and what isn't.

Second, the initialization method is a **magic method** that is called automatically.
Yes, Python programmers actually call methods that are automatically invoked
"magic methods."

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

.. _define-attributes:

Defining Class Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: healthbar.png
    :width: 25%
    :class: right-image


Remember back to our chapter on functions, that any variable created inside a function
is forgotten about after the function is done running? If you want to keep anything,
you need to return it as a value.

Methods follow this rule too, with one exception. The ``self`` parameter
refers to memory associated with each instance of the class. We can use that
``self`` to create variables that *keep* their value for as long as the object exists.
We call variables that exist as part of the class either attributes,
fields, or instance variables. The terms mean the same thing.
Attributes must be set to a default value. That value is often 0, an empty string,
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

    class Address:
        """ Hold all the fields for a mailing address. """
        def __init__(self):
            """ Set up the address fields. """
            self.name = ""
            self.line1 = ""
            self.line2 = ""
            self.city = ""
            self.state = ""
            self.zip = ""

In the code above, ``Address`` is the class name. The variables in the class
are the attributes.

.. sidebar:: Constructor?

    There is some debate about calling ``__init__`` a constructor. In some languages
    a constructor is called *before* the computer sets aside memory for the object.
    In Python the
    ``__init__`` method is actually called *after* this happens. For our purposes,
    the distinction is not important.

The ``__init__`` is a special method that you may also hear referred to
as a **constructor**. If you are programming in other languages, the term
constructor is a generic term used to refer to whatever that language's
equivalent to the ``__init__`` method is.

The ``self.`` is kind of like the pronoun *my*. When inside the class
``Address`` we are talking about *my* name, *my* city, etc. We don't want to
use ``self.`` outside the class. Why? Because just like the pronoun "my," it means someone
totally different when said by a different person!

Creating Objects
----------------

.. image:: address.svg
    :width: 25%
    :class: right-image

The class code *defines* a class but it does not actually create an **instance**
of one. The code told the computer what fields an address has,
but we don't actually have an address yet.
We can define a class without creating one just like we can define a function
without calling it.

To create an instance of the ``Address`` class, we use the following code:

.. code-block:: python
    :linenos:

    def main():
        # Create an address
        home_address = Address()

We need a variable that will point to our address. In this case, we've called it
``home_address``.
We'll set that variable equal to the new instance of the class we create.
We create an new instance by
using the name of the class (Address), followed by parentheses.
This will "magically"
call the ``__init__`` method which will set up fields/attributes for the class.

In this case, ``Address`` is a class. It defines what an address looks like.
The ``home_address`` variable points to an **object**. An object is an instance of
a class. It is the actual address. As another example, "Human" is a class, while
"Samantha" and "Pete" are instances of the class.

You can set the object's attributes using the dot operator. First, use
the variable that points to our object, immediately follow that with a period,
then the attribute name.

.. code-block:: python
    :linenos:

    def main():
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

Attributes are not limited to being simple strings and numbers!
If you have a class that represents a graph, you can store all the data
points in an attribute that is a list.
Attributes can even be other objects. An object that represents a player
character in an adventure could have an attribute with another object that
represents a magical hat.

Common Mistakes Creating Objects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first common mistake when creating an object is to forget the parentheses:

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

Another mistake is on line 22. That line also runs fine, but it creates a new attribute
called ``naem`` instead of setting the desired attribute ``name``.

Using Objects in Functions
--------------------------

Putting lots of data fields into a class makes it easy to pass data in and out
of a function. In this example, the function takes in an address as a
parameter and prints it out on the screen. It is not necessary to pass
parameters for each field of the address.

.. code-block:: python
    :linenos:
    :caption: Passing in an object as a function parameter


    def print_address(address):
        """ Print an address to the screen """

        print(address.name)
        # If there is a line1 in the address, print it
        if len(address.line1) > 0:
            print(address.line1)
        # If there is a line2 in the address, print it
        if len(address.line2) > 0:
            print( address.line2 )
        print(address.city + ", " + address.state + " " + address.zip)


    def main():
        # ... code for creating home_address and vacation_home_address
        # goes here.
        print_address(home_address)
        print()
        print_address(vacation_home_address)


    main()

.. _customize-constructor:

Customizing the Constructor
---------------------------

.. image:: dog.svg
    :width: 20%
    :class: right-image

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
            """ Constructor """
            self.name = ""


    def main():
        # This creates the dog
        my_dog = Dog()
        print(f"The dog's name is: {my_dog.name}")


    main()

We can modify the code in our constructor to keep this from happening.
First, let's add a ``print`` statement to our ``__init__`` just
to demonstrate that it is really being called.

.. code-block:: python
    :linenos:
    :emphasize-lines: 5

    class Dog():
        def __init__(self):
            """ Constructor """
            self.name = ""
            print("A new dog is born!")


    def main():
        # This creates the dog
        my_dog = Dog()
        print(f"The dog's name is: {my_dog.name}")

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
            """ Constructor """
            self.name = new_name
            print("A new dog is born!")


    def main():
        # This creates the dog
        my_dog = Dog()
        print(f"The dog's name is: {my_dog.name}")


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
            """ Constructor """
            self.name = new_name
            print("A new dog is born!")


    def main():
        # This creates the dog
        my_dog = Dog("Fluffy")

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
            """ Constructor """
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

.. _address-class-example-with-init:

Address Class With Init Parameters
----------------------------------

Here's another example, this time with our ``Address`` class. We supply
the address attributes as part of our ``__init__`` when our address is created.

.. code-block:: python
    :linenos:

    class Address:
        def __init__(self, line1, line2, city, state, zip, country):
            self.line1 = line1
            self.line2 = line2
            self.city = city
            self.state = state
            self.zip = zip
            self.country = country


    def main():
        # This creates the address
        my_address = Address("701 N. C Street",
                             "Carver Science Building",
                             "Indianola",
                             "IA",
                             "50125",
                              "USA")


    main()

Typing Attributes
-----------------

It is possible to tell Python what *type* of data
should be stored in a class attribute. This allows a programmer to use a tool like
``mypy`` and catch errors earlier in the development process.

In this example, we are adding a type definition to the ``name`` attribute on
line 3. We do this by following the variable name with a colon, and adding ``str``
which is the abbreviation for the **string** data type.

.. code-block:: python
    :linenos:
    :emphasize-lines: 3

    class Person:
        def __init__(self):
            self.name: str = "A"


    mary = Person()
    mary.name = 22

By assigning a number to the ``name`` attribute on line 7, we are storing the wrong kind
of data. The program runs, but if we use the ``mypy`` tool, it will give us an
error saying we've made a mistake:

.. code-block:: text
    :linenos:

    test.py:7: error: Incompatible types in assignment (expression has type "int", variable has type "str")
    Found 1 error in 1 file (checked 1 source file)

Typing is great for large programs, and for programs where we want to make sure
to catch all the errors we can before shipping to customers.

As we are just learning programming, it can be distracting to try adding typing
to our programs at this stage. But we will be both looking and using, other people's code
which does use typing. Therefore
it is important to know what typing is, even if we don't need to use it ourselves until
later.

.. _data-classes:

Data Classes
------------

When creating a class and a constructor to define a set of fields,
we end up with code that looks like this:

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

This code is repetitive, as we state the fields twice.
If your ``__init__`` method is only going to take in data
fields and assign attribute values, you can simplify your code by
using a **dataclass**.

Starting with Python 3.8, you can write the same thing using only this code:

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

This makes the code a lot easier to both write, and to read.

Static Variables
----------------

.. image:: cat.svg
    :width: 20%
    :class: right-image

Class attributes are also called instance variables because they can be
different for each instance of the class. If you have five instances of
the ``Dog`` class, each instance will have its own name.

In a few rare cases, we want to share data between *all* instances of a
class. In this example with a ``Cat`` class, we have a ``population`` variable. This variable is
*not* different for each cat.

.. code-block:: python
    :linenos:
    :emphasize-lines: 2, 6, 13

    class Cat:
        population = 0

        def __init__(self, name):
            self.name = name
            Cat.population += 1

    def main():
        cat1 = Cat("Pat")
        cat2 = Cat("Pepper")
        cat3 = Cat("Pouncy")

        print("The cat population is:", Cat.population)

    main()

In this case we use ``Cat.population`` to keep track of our cat population, and the
program will print out the correct count of 3.

Variables that *don't* change for each instance of a class, are called
**class variables** or **static variables**. The terms mean the same thing and
can be used interchangeably.

You refer to a static variable by using the class name ``Cat`` rather than any of the
instance names like ``cat1``.

Static variables aren't used that often. The only reason we are introducing them here
is that it is not unusual for students to accidentally use a static variable instead of
an instance variable. In fact, Python makes it a bit too easy to 'blend' the two concepts
together.

For example, we can also print a static variable not just by using the class name, but also
by using the instance name:

.. code-block:: python
    :linenos:

    print("The cat population is:", Cat.population)
    print("The cat population is:", cat1.population)

When we are reading code and come across a variable like ``Cat.population``,
we immediately know it is static. How? All class
names start with a capital letter, so ``Cat`` is a class. The only attributes that we can
refer to with a class, rather than an instance, are static variables. So ``population`` must
be static. If we use ``cat1.population``, a programmer reading that code might mistakenly assume
it is an instance variable rather than a static variable, so that makes debugging really hard.
To reduce confusion, always refer to static variables using the class name.

In this example, I set population to 4, and each print statement says population is 4. This is
confusing because I set one variable and the others change. If I just use ``Cat.population`` to
refer to the population, then I remove that confusion.

.. code-block:: python
    :linenos:

    Cat.population = 4
    print("The cat population is:", Cat.population)
    print("The cat population is:", cat2.population)
    print("The cat population is:", cat1.population)

Here's where it gets really wild. As we just saw, I can print a static variable
by referring to it with an instance, rather than by the class name. I shouldn't,
but I can.

What if, instead of printing, I assign a value that way?

.. code-block:: python
    :linenos:

    Cat.population = 4
    cat3.population = 5
    print("The cat population is:", Cat.population)
    print("The cat population is:", cat1.population)
    print("The cat population is:", cat2.population)
    print("The cat population is:", cat3.population)

In this case ``Cat.population``, ``cat1.population``, and ``cat2.population`` all refer to the
same static variable. But once I *assign* a value to ``cat3.population`` it creates a brand-new
*instance* variable. So all the other cats use the static population value, while ``cat3`` uses
a new instance variable with the same exact name as the static variable. The static variable
is **shadowed** by the instance variable. Therefore when we print ``cat3.population`` we
get a 5. That type of bug is *very* hard to find.

For our purposes, we won't need to use static variables, we only introduce them so that
you can better understand some confusing errors people occasionally run into.

Review
------

In this chapter we learned how to bundle together several related data items
into a **class**. We call these **class attributes**, **instance variables**, or **fields**.
Each instance of a class is an **object**.
Functions defined in a class are called **methods**. A special **magic method**
called when an object is created is the ``__init__`` method, which
is used to set up instance variables and assign them their initial values.

Inside the class we refer to instance variables by putting ``self.`` in front
of them, such as ``self.name``. Outside the class, we need to use a variable
that refers to the class, such as ``customer.name``.

Using classes helps simplify our code. We can use classes to represent:

* Characters in a video game, with attributes for health, speed, and armor.
* Graphs, with attributes for heading, size, and data.
* A customer order, with a list as an attribute for each item in the order.

**Data classes** can be used to make it easier to define a class with a lot of attributes.
**Typing** can be used to make sure we don't put the wrong type of data in an
attribute.
**Static variables** are attributes that don't change from object
to object.

Review Questions
^^^^^^^^^^^^^^^^

#. What are the three main advantages of object-oriented programming?
#. What keyword is used to define a new class?
#. All class names should start with an upper-case or lower-case letter?
#. Where do the comments for a class go? What kind of comments do you use?
   Why is there a standard?
#. What is the difference between a function and a method?
#. What three different terms can be used to refer to data that is tied to a
   a class?
#. What is a magic method?
#. What is a dunder method?
#. All class methods should have start with the same parameter. What is that
   parameter?
#. What is the name of the method in a class where we define our attributes?
#. When defining a class attribute, what needs to go right before it?
#. What is a constructor?
#. What is the difference between a class and an object?
#. What are the common mistakes when creating instances (objects) of a class?
#. How can we make sure our attributes are assigned when the object is created?
#. What is the point of adding "typing" to a class?
#. What is a data class?
#. What are static variables?

Lab 6: Text Adventure
^^^^^^^^^^^^^^^^^^^^^

In :ref:`lab-06`, you'll use a class to represent a room in an text adventure. You'll
use attributes to store the room description, and which rooms are north, south,
east and west of it. You'll use a list to store all the rooms in your adventure.
