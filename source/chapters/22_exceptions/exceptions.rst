Exceptions
==========

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/HDH5S3qXcCc" frameborder="0" allowfullscreen></iframe>

When something goes wrong with your program, do you want to keep the user from
seeing a red Python error message? Do you want to keep your program from
hanging? If so, then you need *exceptions*.

Exceptions are used to handle abnormal conditions that can occur during the
execution of code. Exceptions are often used with file and network operations.
This allows code to gracefully handle running out of disk space, network
errors, or permission errors.

Vocabulary
----------

There are several terms and phrases used while working with exceptions.
Here are the most common:

* **Exception**: This term could mean one of two things. First, the condition
  that results in abnormal program flow. Or it could be used to refer to an
  object that represents the data condition. Each exception has an object
  that holds information about it.
* **Exception handling**: The process of handling an exception to normal
  program flow.
* **Catch block or exception block**: Code that handles an abnormal condition
  is said to "catch" the exception.
* **Throw or raise**: When an abnormal condition to the program flow has been
  detected, an instance of an exception object is created. It is then "thrown"
  or "raised" to code that will catch it.
* **Unhandled exception or Uncaught exception**: An exception that is thrown,
  but never caught. This usually results in an error and the program ending or
  crashing.
* **Try block**: A set of code that might have an exception thrown in it.

Most programming languages use the terms "throw" and "catch." Unfortunately
Python doesn't. Python uses "raise" and "exception." We introduce the
throw/catch vocabulary here because they are the most prevalent terms in the
industry.

Exception Handling
------------------

The code for handling exceptions is simple. See the example below:

.. code-block:: python
    :linenos:
    :caption: Handling division by zero

    # Divide by zero
    try:
        x = 5 / 0
    except:
        print("Error dividing by zero")

On line two is the ``try`` statement. Every indented line below it is part of the
"try block." There may be no unindented code below the ``try`` block that doesn't
start with an ``except`` statement. The ``try`` statement defines a section of code
that the code will attempt to execute.

If there is any exception that occurs during the processing of the code the
execution will immediately jump to the "catch block." That block of code is
indented under the ``except`` statement on line 4. This code is responsible for
handling the error.

A program may use exceptions to catch errors that occur during a conversion
from text to a number. For example:

.. code-block:: python
    :caption: Handling number conversion errors
    :linenos:

    # Invalid number conversion
    try:
        x = int("fred")
    except:
        print("Error converting fred to a number")

An exception will be thrown on line 3 because "fred" can not be converted to
an integer. The code on line 5 will print out an error message.

Below is an expanded version on this example. It error-checks a user's input
to make sure an integer is entered. If the user doesn't enter an integer, the
program will keep asking for one. The code uses exception handling to capture
a possible conversion error that can occur on line 5. If the user enters
something other than an integer, an exception is thrown when the conversion
to a number occurs on line 5. The code on line 6 that sets ``number_entered`` to
``True`` will not be run if there is an exception on line 5.

.. code-block:: python
    :caption: Better handling of number conversion errors
    :linenos:

    number_entered = False
    while not number_entered:
        number_string = input("Enter an integer: ")
        try:
            n = int(number_string)
            number_entered = True
        except:
            print("Error, invalid integer")

Files are particularly prone to errors during operations with them. A disk
could fill up, a user could delete a file while it is being written, it could
be moved, or a USB drive could be pulled out mid-operation. These types of
errors may also be easily captured by using exception handling.

.. code-block:: python
    :linenos:
    :caption: Checking for an error when opening a file

    # Error opening file
    try:
        my_file = open("myfile.txt")
    except:
        print("Error opening file")

Multiple types of errors may be captured and processed differently. It can be
useful to provide a more exact error message to the user than a simple "an
error has occurred."

In the code below, different types of errors can occur from lines 3-6. By
placing ``IOError`` after ``except`` on line 7, only errors regarding Input and
Output (IO) will be handled by that code. Likewise line 9 only handles
errors around converting values, and line 11 covers division by zero errors.
The last exception handling occurs on line 13. Since line 13 does not include
a particular type of error, it will handle any error not covered by the ``except``
blocks above. The "catch-all" ``except`` must always be last.

.. code-block:: python
    :linenos:
    :caption: Handling different types of errors

    # Multiple errors
    try:
        # Open the file
        filename = "myfile.txt"
        my_file = open(filename)

        # Read from the file and strip any trailing line feeds
        my_line = my_file.readline()
        my_line = my_line.strip()

        # Convert to a number
        my_int = int(my_line)

        # Do a calculation
        my_calculated_value = 101 / my_int

    except FileNotFoundError:
        print(f"Could not find the file '{filename}'.")
    except IOError:
        print(f"Input/Output error when accessing the file '{filename}'.")
    except ValueError:
        print("Could not convert data to an integer.")
    except ZeroDivisionError:
        print("Division by zero error.")
    except:
        print("Unexpected error.")

A list of built-in exceptions is available from this web address:

http://docs.python.org/library/exceptions.html

Example: Saving High Score
--------------------------

This shows how to save a high score between games. The score is stored in a file called ``high_score.txt``.

.. code-block:: python
    :linenos:
    :caption: high_score.py

    """
    Show how to use exceptions to save a high score for a game.

    Sample Python/Pygame Programs
    Simpson College Computer Science
    http://simpson.edu/computer-science/
    """


    def get_high_score():
        # Default high score
        high_score = 0

        # Try to read the high score from a file
        try:
            high_score_file = open("high_score.txt", "r")
            high_score = int(high_score_file.read())
            high_score_file.close()
            print("The high score is", high_score)
        except IOError:
            # Error reading file, no high score
            print("There is no high score yet.")
        except ValueError:
            # There's a file there, but we don't understand the number.
            print("I'm confused. Starting with no high score.")

        return high_score


    def save_high_score(new_high_score):
        try:
            # Write the file to disk
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(new_high_score))
            high_score_file.close()
        except IOError:
            # Hm, can't write it.
            print("Unable to save the high score.")


    def main():
        """ Main program is here. """
        # Get the high score
        high_score = get_high_score()

        # Get the score from the current game
        current_score = 0
        try:
            # Ask the user for his/her score
            current_score = int(input("What is your score? "))
        except ValueError:
            # Error, can't turn what they typed into a number
            print("I don't understand what you typed.")

        # See if we have a new high score
        if current_score > high_score:
            # We do! Save to disk
            print("Yea! New high score!")
            save_high_score(current_score)
        else:
            print("Better luck next time.")

    # Call the main function, start up the game
    if __name__ == "__main__":
        main()

Exception Objects
-----------------

More information about an error can be pulled from the *exception object*.
This object can be retrieved while catching an error using the ``as`` keyword.
For example:

.. code-block:: python
    :linenos:
    :caption: Creating an exception

    try:
        x = 5 / 0
    except ZeroDivisionError as e:
        print(e)

The ``e`` variable points to more information about the exception that can be
printed out. More can be done with exceptions objects, but unfortunately that
is beyond the scope of this chapter. Check the Python documentation on-line
for more information about the exception object.

Exception Generating
--------------------

Exceptions may be generated with the ``raise`` command. For example:

.. code-block:: python
    :linenos:
    :caption: Creating an exception

    # Generating exceptions
    def get_input():
        user_input = input("Enter something: ")
        if len(user_input) == 0:
            raise IOError("User entered nothing")

    get_input()

Try taking the code above, and add exception handling for the ``IOError`` raised.

It is also possible to create custom exceptions, but that is also beyond the
scope of this book. Curious readers may learn more by going to:

http://docs.python.org/tutorial/errors.html#raising-exceptions

Proper Exception Use
--------------------
Exceptions should not be used when ``if`` statements can just as easily handle
the condition. Normal code should not raise exceptions when running the
"happy path" scenario. Well-constructed try/catch code is easy to follow
but code involving many exceptions and jumps in code to different handlers
can be a nightmare to debug. (Once I was assigned the task of debugging code
that read an XML document. It generated dozens of exceptions for each line of
the file it read. It was incredibly slow and error-prone. That code should
have never generated a single exception in the normal course of reading a file.)
