Creating Functions
==================

Creating Simple Functions
-------------------------

Defining a function is rather easy.

* Start with the keyword ``def``, which is short for "define."
* Next, give the function a name. There are rules for function names. They must:

  * Start with a lower case letter.
  * After the first letter, only use letters, numbers, and underscores.
  * Spaces are not allowed. Use underscores instead.
  * While upper-case letters can be used, function names are normally all
    lower-case.

* After that, we have a set of parenthesis. Inside the parenthesis will go
  **parameters**. We'll explain those in a bit.
* Next, a colon.
* Everything that is part of the function will be indented four spaces.
* Usually we start a function with a multi-line comment that explains what
  the function does.

.. Note::

    Function definitions go *below* the ``import`` statements, and *above* the
    rest of the program. While you can put them somewhere else, you shouldn't.

Below is a program that defines and uses the function twice.


.. code-block:: python
    :linenos:

    def print_hello():
        """ This is a comment that describes the function. """
        print("Hello!")


    print_hello()
    print_hello()


You can define and use multiple functions. But all function definitions should
go before the main code.


.. code-block:: python
    :linenos:

    def print_hello():
        print("Hello!")


    def print_goodbye():
        print("Bye!")


    print_hello()
    print_goodbye()


Actually, almost *all* code should go in a function. It is a good practice
to put the main starting point of your program in a function called ``main``
and call it.

.. code-block:: python
    :emphasize-lines: 9-12, 16
    :linenos:

    def print_hello():
        print("Hello!")


    def print_goodbye():
        print("Bye!")


    def main():
        """ This is my main program function """
        print_hello()
        print_goodbye()


    # Run the main program
    main()


An even better way of writing this is with a check to make sure we are trying
to run this file, and not import it. The statement for this looks a little
weird. In fact, it is weird enough I just look it up and copy/paste it any
time I want to use it. Don't worry about understanding how it works yet.


.. code-block:: python
    :linenos:
    :emphasize-lines: 14-17

    def print_hello():
        print("Hello!")


    def print_goodbye():
        print("Bye!")


    def main():
        print_hello()
        print_goodbye()


    # Only run the main function if we are running this file. Don't run it
    # if we are importing this file.
    if __name__ == "__main__":
        main()


Taking In Data
--------------

Functions are even more powerful if we have them take in data.

Here is a simple example that will take in a number and print it. Notice how
I've created a new variable ``my_number`` in between the parenthesis. This
variable will be given whatever value is passed in. In the example below, it
is given first a ``55``, then ``25``, and finally a ``5``.

.. code-block:: python
    :linenos:

    def print_number(my_number):
        print(my_number)


    print_number(55)
    print_number(25)
    print_number(8)

You can pass in multiple numbers, just separate them with a comma.

.. code-block:: python
    :linenos:

    def add_numbers(a, b):
        print(a, b)


    add_numbers(11, 7)

Occasionally, new programmers want to set the number values inside the
function. This is wrong. Then the function would only work for those values.
The power is in specifying the numbers outside the function. We don't want
the function to be limited to only certain data values.

.. code-block:: python
    :linenos:

    # This is wrong
    def add_numbers(a, b):
        a = 11
        b = 7
        print(a, b)


    add_numbers(11, 7)



Returning and Capturing Values
------------------------------

Functions can not only take in values, functions can return values.

.. _returning-values:

Returning values
^^^^^^^^^^^^^^^^

For example:

Function that returns two numbers added together

.. code-block:: python
    :linenos:

    # Add two numbers and return the results
    def sum_two_numbers(a, b):
        result = a + b
        return result

Note: Return is not a function, and does not use parentheses. Don't do
``return(result)``.

This only gets us half-way there. Because if we call the function now, not
much happens. The numbers get added. They get returned to us. But we do
nothing with the result.

.. code-block:: python

    # This doesn't do much, because we don't capture the result
    sum_two_numbers(22, 15)

.. _capturing_returned_values:

Capturing Returned Values
^^^^^^^^^^^^^^^^^^^^^^^^^

We need to capture the result. We do that by setting a variable equal to
the value the function returned:

.. code-block:: python

    # Capture the function's result into a variable
    # by putting "my_result =" in front of it.
    # (Use whatever variable name best describes the data,
    # don't blindly use 'my_result' for everything.)
    my_result = sum_two_numbers(22, 15)

    # Now that I captured the result, print it.
    print(my_result)

Now the result isn't lost. It is stored in `my_result`
which we can print or use some other way.

Volume Cylinder Example
^^^^^^^^^^^^^^^^^^^^^^^

Function that returns the volume of a cylinder

.. code-block:: python
    :linenos:

    def volume_cylinder(radius, height):
        pi = 3.141592653589
        volume = pi * radius ** 2 * height
        return volume

Because of the return, this function could be used later on as part of an
equation to calculate the volume of a six-pack like this:

.. code-block:: python

    six_pack_volume = volume_cylinder(2.5, 5) * 6

The value returned from volume_cylinder goes into the equation and is
multiplied by six.

There is a big difference between a function that prints a value and a
function that returns a value. Look at the code below and try it out.

.. code-block:: python
    :linenos:

    # Function that prints the result
    def sum_print(a, b):
        result = a + b
        print(result)


    # Function that returns the results
    def sum_return(a, b):
        result = a + b
        return result


    # This prints the sum of 4+4
    sum_print(4, 4)

    # This does not
    sum_return(4, 4)

    # This will not set x1 to the sum
    # It actually gets a value of 'None'
    x1 = sum_print(4, 4)
    print("x1 =", x1)

    # This will set x2 to the sum
    # and print it properly
    x2 = sum_return(4, 4)
    print("x2 =", x1)


When first working with functions it is not unusual to get stuck looking at
code like this:

.. code-block:: python

    def calculate_average(a, b):
        """ Calculate an average of two numbers """
        result = (a + b) / 2
        return result


    # Pretend you have some code here
    x = 45
    y = 56

    # Wait, how do I print the result of this?
    calculate_average(x, y)

How do we print the result of calculate_average? The program can't print
result because that variable only exists inside the function. Instead, use
a variable to capture the result:

.. code-block:: python

    def calculate_average(a, b):
        """ Calculate an average of two numbers """
        result = (a + b) / 2
        return result


    # Pretend you have some code here
    x = 45
    y = 56

    average = calculate_average(x, y)
    print(average)

Documenting Functions
---------------------

Functions in Python typically have a comment as the first statement of the
function. This comment is delimited using three double quotes, and is called a
docstring. A function may look like:

.. code-block:: python

    def volume_cylinder(radius, height):
        """Returns volume of a cylinder given radius, height."""
        pi = 3.141592653589
        volume = pi * radius ** 2 * height
        return volume

The great thing about using docstrings in functions is that the comment can be
pulled out and put into a website documenting your code using a tool like
Sphinx. Most languages have similar tools that can help make documenting your
code a breeze. This can save a lot of time as you start working on larger
programs.

Variable Scope
--------------

The use of functions introduces the concept of scope. Scope is where in the
code a variable is "alive" and can be accessed. For example, look at the code
below:

.. code-block:: python

    # Define a simple function that sets
    # x equal to 22
    def f():
        x = 22


    # Call the function
    f()
    # This fails, x only exists in f()
    print(x)

The last line will generate an error because x only exists inside of the f()
function. The variable is created when ``f()`` is called and the memory it uses is
freed as soon as ``f()`` finishes.

Here's where it gets complicated.
A more confusing rule is accessing variables created outside of the ``f()``
function. In the following code, x is created before the ``f()`` function, and
thus can be read from inside the ``f()`` function.

.. code-block:: python

    # Create the x variable and set to 44
    x = 44


    # Define a simple function that prints x
    def f():
        print(x)


    # Call the function
    f()

Variables created ahead of a function may be read inside of the function only
if the function does not change the value. This code, very similar to the code
above, will fail. The computer will claim it doesn't know what x is.

.. code-block:: python

    # Create the x variable and set to 44
    x = 44


    # Define a simple function that prints x
    def f():
        x += 1
        print(x)


    # Call the function
    f()

Other languages have more complex rules around the creation of variables and
scope than Python does. Because Python is straight-forward it is a good
introductory language.

Pass-by-Copy
------------

Functions pass their values by creating a copy of the original. For example:

.. code-block:: python

    # Define a simple function that prints x
    def f(x):
        x += 1
        print(x)


    # Set y
    y = 10
    # Call the function
    f(y)
    # Print y to see if it changed
    print(y)

The value of y does not change, even though the f() function increases the
value passed to it. Each of the variables listed as a parameter in a function
is a brand new variable. The value of that variable is copied from where it is
called.

This is reasonably straight forward in the prior example. Where it gets
confusing is if both the code that calls the function and the function itself
have variables named the same. The code below is identical to the prior listing,
but rather than use y it uses x.

.. code-block:: python

    # Define a simple function that prints x
    def f(x):
        x += 1
        print(x)


    # Set x
    x = 10
    # Call the function
    f(x)
    # Print x to see if it changed
    print(x)

The output is the same as the program that uses y. Even though both the
function and the surrounding code use x for a variable name, there are
actually two different variables. There is the variable x that exists
inside of the function, and a different variable x that exists outside
the function.

Functions Calling Functions
---------------------------

For each of the examples below, think about what would print. Check to see
if you are right. If you didn't guess correctly, spend to the time to
understand why.

Example 1
^^^^^^^^^

In this example, note that if you don't use a function, it doesn't run.

.. code-block:: python

    # Example 1
    def a():
        print("A")


    def b():
        print("B")


    def c():
        print("C")


    a()

Example 2
^^^^^^^^^

.. code-block:: python

    # Example 2
    def a():
        b()
        print("A")


    def b():
        c()
        print("B")


    def c():
        print("C")


    a()


Example 3
^^^^^^^^^

.. code-block:: python

    # Example 3
    def a():
        print("A")
        b()


    def b():
        print("B")
        c()


    def c():
        print("C")


    a()

Example 4
^^^^^^^^^

.. code-block:: python

    # Example 4
    def a():
        print("A start")
        b()
        print("A end")


    def b():
        print("B start")
        c()
        print("B end")


    def c():
        print("C start and end")


    a()


Example 5
^^^^^^^^^

.. code-block:: python

    # Example 5
    def a(x):
        print("A start, x =", x)
        b(x + 1)
        print("A end, x =", x)


    def b(x):
        print("B start, x =", x)
        c(x + 1)
        print("B end, x =", x)


    def c(x):
        print("C start and end, x =", x)


    a(5)

Example 6
^^^^^^^^^

While line 3 of this example increases ``x``, the ``x`` variable in the function is a different variable than the
``x`` that is in the rest of the program. So that ``x`` never changes.

.. code-block:: python

    # Example 6
    def a(x):
        x = x + 1


    x = 3
    a(x)

    print(x)

Example 7
^^^^^^^^^

This example is similar to the prior example, but we ``return x`` at the end. Turns out, it doesn't matter. Because we
never do anything with the return value. So the global variable ``x`` still doesn't increase. See the next example.

.. code-block:: python

    # Example 7
    def a(x):
        x = x + 1
        return x


    x = 3
    a(x)

    print(x)

Example 8
^^^^^^^^^

This example take the value returned from ``a`` and stores it back into ``x``. How? By doing ``x = a(x)`` instead of
just ``a(x)``.

.. code-block:: python

    # Example 8
    def a(x):
        x = x + 1
        return x


    x = 3
    x = a(x)

    print(x)

Example 9
^^^^^^^^^

.. code-block:: python

    # Example 9
    def a(x, y):
        x = x + 1
        y = y + 1
        print(x, y)


    x = 10
    y = 20
    a(y, x)

Example 10
^^^^^^^^^^

While you can have two ``return`` statements in a function, once you hit the first ``return`` the function ends. In
this case, ``return y`` never runs, because we already returned from the function in the prior line.

.. code-block:: python

    # Example 10
    def a(x, y):
        x = x + 1
        y = y + 1
        return x
        return y


    x = 10
    y = 20
    z = a(x, y)

    print(z)

Example 11
^^^^^^^^^^

This is not something you can do in every programming language. You can return two values by using a comma and listing them.

.. code-block:: python

    # Example 11
    def a(x, y):
        x = x + 1
        y = y + 1
        return x, y


    x = 10
    y = 20
    z = a(x, y)

    print(z)

Example 12
^^^^^^^^^^

If you return two values out of a function, you can capture them this way.

.. code-block:: python

    # Example 12
    def a(x, y):
        x = x + 1
        y = y + 1
        return x, y


    x = 10
    y = 20
    x2, y2 = a(x, y) # Most computer languages don't support this

    print(x2)
    print(y2)

Example 13
^^^^^^^^^^

.. code-block:: python

    # Example 13
    def a(my_data):
        print("function a, my_data =  ", my_data)
        my_data = 20
        print("function a, my_data =  ", my_data)


    my_data = 10

    print("global scope, my_data =", my_data)
    a(my_data)
    print("global scope, my_data =", my_data)

Example 14
^^^^^^^^^^

We will talk more about these next two examples when we talk about "lists" and "classes" later. These examples don't
operate like you might expect at first. Take a look and see what is different. We'll explain why it works differently
later.

.. code-block:: python

    # Example 14
    def a(my_list):
        print("function a, list =  ", my_list)
        my_list = [10, 20, 30]
        print("function a, list =  ", my_list)


    my_list = [5, 2, 4]

    print("global scope, list =", my_list)
    a(my_list)
    print("global scope, list =", my_list)

Example 15
^^^^^^^^^^

.. code-block:: python

    # Example 15
    # New concept!
    # Covered in more detail in a later chapter
    def a(my_list):
        print("function a, list =  ", my_list)
        my_list[0] = 1000
        print("function a, list =  ", my_list)


    my_list = [5, 2, 4]

    print("global scope, list =", my_list)
    a(my_list)
    print("global scope, list =", my_list)
