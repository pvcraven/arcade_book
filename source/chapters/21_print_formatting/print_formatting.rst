.. sectnum::
    :start: 21

Print Formatting
================

Here is a quick table for reference when doing text formatting. For a detailed explanation of how text formatting works, keep reading.


.. list-table:: Example Formatting Commands
   :widths: 15 15 20 40
   :header-rows: 1

   * - Number
     - Format
     - Output
     - Description
   * - ``x = 3.1415926``
     - ``print(f"{x:.2f}")``
     - ``3.14``
     - 2 decimal places
   * - ``x = 3.1415926``
     - ``print(f"{x:+.2f}")``
     - ``+3.14``
     - 2 decimal places with sign
   * - ``x = -1``
     - ``print(f"{x:+.2f}")``
     - ``-1.00``
     - 2 decimal places with sign
   * - ``x = 3.1415926``
     - ``print(f"{x:.0f}")``
     - ``3``
     - No decimal places (will round)
   * - ``x = 5``
     - ``print(f"{x:0>2d}")``
     - ``05``
     - Pad with zeros on the left
   * - ``x = 1000000``
     - ``print(f"{x:,}")``
     - ``1,000,000``
     -  Number format with comma separator
   * - ``x = 0.25``
     - ``print(f"{x:.2%}")``
     - ``25.00%``
     - Format percentage
   * - ``x = 1000000000``
     - ``print(f"{x:.2e}")``
     - ``1.00e+09``
     - Exponent notation
   * - ``x = 11``
     - ``print(f"{x:>10d}")``
     - ``........11``
     - Right aligned
   * - ``x = 11``
     - ``print(f"{x:<10d}")``
     - ``11........``
     - Left aligned
   * - ``x = 11``
     - ``print(f"{x:^10d}")``
     - ``....11....``
     - Center aligned



Decimal Numbers
---------------

Try running the following program, which prints out several random numbers.

.. code-block:: python
    :linenos:
    :caption: Print an unformatted list of numbers

    import random

    for i in range(10):
        x = random.randrange(120)
        print("My number: ", x)

The output is left justified and numbers look terrible:

.. code-block:: text

    My number:  30
    My number:  2
    My number:  101
    My number:  3
    My number:  44
    My number:  111
    My number:  100
    My number:  48
    My number:  27
    My number:  92

We can use string formatting to make the list of numbers look better by
right-justifying them. The first step is to use the "Literal String
Interpolation" on the string. See below:

.. code-block:: python

    import random

    for i in range(10):
        x = random.randrange(120)
        print(f"My number: {x}")

This gets our program closer to right-justifying the number, but we aren't
quite there yet. See how the string starts with ``f``?

The string will not print out the curly braces ``{}`` but instead replace
them with the value in ``x``. The output (below) looks just like what we had before.

.. code-block:: text
    :caption: The output:

    My number: 23
    My number: 92
    My number: 102
    My number: 19
    My number: 85
    My number: 114
    My number: 37
    My number: 101
    My number: 35
    My number: 18

To right justify, we add more information about how to format the number
to the curly braces ``{}``:

.. code-block:: python
    :linenos:
    :caption: Right justified list of numbers

    import random

    for i in range(10):
        x = random.randrange(120)
        print(f"My number: {x:3}")


.. code-block:: text
    :caption: The output:

    My number:  37
    My number: 108
    My number: 117
    My number:  55
    My number:  19
    My number:  97
    My number:  78
    My number:  12
    My number:  29
    My number:   0

This is better; we have right justified numbers! But how does it work?
The ``:3`` that we added isn't exactly intuitive. Looks like we just
added a random emoji.

Here's the breakdown: The ``{ }`` tells the computer we are going to format a
number. Inside we put the variable we want to format, ``x`` in this case.
After the variable, we put a ``:`` to tell the computer we are about to give it
formatting information.

In this case we give it a 3 to specify a field width of three characters. The
field width value tells the computer to try to fit the number into a field
three characters wide. By default, it will try to right-justify numbers and
left-justify text.

Even better, the program no longer needs to call ``str( )`` to convert the
number to a string! Leave the string conversions out.

What if you had large numbers? Let's make bigger random numbers:

.. code-block:: python
    :linenos:
    :caption: Bigger numbers that are hard to read

    import random

    for i in range(10):
        x = random.randrange(100000)
        print(f"My number: {x:6}")

This gives output that is right justified, but still doesn't look good.

.. code-block:: text
    :caption: The output:

    My number:  89807
    My number:   5177
    My number:  24067
    My number:  19887
    My number:  54155
    My number:  49288
    My number:  31412
    My number:  49633
    My number:  43406
    My number:  37398

Where are the commas? This list would look better with separators between each
three digits. Take a look at the next example to see how they are added in:

.. code-block:: python
    :linenos:
    :caption: Adding a thousands separator

    import random

    for i in range(10):
        x = random.randrange(100000)
        print(f"My number: {x:6,}")

The output:

.. code-block:: text

    My number: 86,631
    My number: 57,165
    My number: 19,835
    My number: 22,560
    My number: 43,161
    My number: 16,604
    My number: 20,544
    My number: 33,906
    My number: 89,846
    My number: 27,350

We added a comma after the field width specifier, and now our numbers have
commas. That comma must go after the field width specifier, not before. Commas
are included in calculating the field width. For example, 1,024 has a field
width of 5, not 4.

We can print multiple values, and combine the values with text. Run the code
below.

.. code-block:: python
    :linenos:
    :caption: Printing more than one variable at a time

    x = 5
    y = 66
    z = 777
    print(f"A - '{x}' B - '{y}' C - '{z}'")

The program will substitute numbers in for the curly braces, and still print
out all of the other text in the string:

.. code-block:: text

    A - '5' B - '66' C - '777'

Strings
-------

Let's look at how to format strings.

The following list looks terrible.

.. code-block:: python
    :linenos:
    :caption: Terrible looking list

    my_fruit = ["Apples","Oranges","Grapes","Pears"]
    my_calories = [4, 300, 70, 30]

    for i in range(4):
        print(my_fruit[i], "are", my_calories[i], "calories.")

The output:

.. code-block:: text

    Apples are 4 calories.
    Oranges are 300 calories.
    Grapes are 70 calories.
    Pears are 30 calories.

Now try it using the format command. Note how we can put additional text and
more than one value into the same line.

.. code-block:: python
    :linenos:
    :caption: Formatting a list of fruit

    my_fruit = ["Apples", "Oranges", "Grapes", "Pears"]
    my_calories = [4, 300, 70, 30]

    for i in range(4):
        print(f"{my_fruit[i]:7} are {my_calories[i]:3} calories.")

.. code-block:: text
    :caption: The output:

    Apples  are   4 calories.
    Oranges are 300 calories.
    Grapes  are  70 calories.
    Pears   are  30 calories.

That's pretty cool, and it looks the way we want it. But what if we didn't
want the numbers right justified, and the text left justified? We can use the
``<`` and ``>`` characters like the following example:

.. code-block:: python
    :linenos:
    :caption: Specifying right/left alignment

    my_fruit = ["Apples", "Oranges", "Grapes", "Pears"]
    my_calories = [4, 300, 70, 30]

    for i in range(4):
        print(f"{my_fruit[i]:>7} are {my_calories[i]:<3} calories.")

.. code-block:: text
    :caption: The output:

     Apples are 4   calories.
    Oranges are 300 calories.
     Grapes are 70  calories.
      Pears are 30  calories.

Leading Zeros
-------------

This produces output that isn't right:

.. code-block:: python
    :linenos:
    :caption: Terrible looking clock

    for hours in range(1,13):
        for minutes in range(0,60):
            print(f"Time {hours}:{minutes}")


.. code-block:: text
    :caption: The not-very-good output:

    Time 8:56
    Time 8:57
    Time 8:58
    Time 8:59
    Time 9:0
    Time 9:1
    Time 9:2

We need to use leading zeros for displaying numbers in clocks. Rather than
specify a 2 for the field width, instead use 02. This will pad the field with
zeros rather than spaces.

.. code-block:: python
    :linenos:
    :caption: Formatting time output with leading zeros

    for hours in range(1, 13):
        for minutes in range(0, 60):
            print(f"Time {hours:02}:{minutes:02}")


.. code-block:: text
    :caption: The output:

    Time 08:56
    Time 08:57
    Time 08:58
    Time 08:59
    Time 09:00
    Time 09:01
    Time 09:02

Floating Point Numbers
----------------------

We can also control floating point output. Examine the following code and its output:

.. code-block:: python
    :linenos:
    :caption: Formatting float point numbers

    x = 0.1
    y = 123.456789

    print(f"{x:.1}  {y:.1}")
    print(f"{x:.2}  {y:.2}")
    print(f"{x:.3}  {y:.3}")
    print(f"{x:.4}  {y:.4}")
    print(f"{x:.5}  {y:.5}")
    print(f"{x:.6}  {y:.6}")

    print()
    print(f"{x:.1f}  {y:.1f}")
    print(f"{x:.2f}  {y:.2f}")
    print(f"{x:.3f}  {y:.3f}")
    print(f"{x:.4f}  {y:.4f}")
    print(f"{x:.5f}  {y:.5f}")
    print(f"{x:.6f}  {y:.6f}")

.. code-block:: text
    :linenos:
    :caption: And here's the output for that code:

    0.1  1e+02
    0.1  1.2e+02
    0.1  1.23e+02
    0.1  123.5
    0.1  123.46
    0.1  123.457

    0.1  123.5
    0.10  123.46
    0.100  123.457
    0.1000  123.4568
    0.10000  123.45679
    0.100000  123.456789

A format of ``.2`` means to display the number with two digits of precision.
Unfortunately this means if we display the number ``123`` which has three
significant numbers rather than rounding it we get the number in scientific
notation: ``1.2e+02``.

A format of ``.2f`` (note the ``f``) means to display the number with two digits
after the decimal point. So the number 1 would display as ``1.00`` and the number
``1.5555`` would display as ``1.56``.

A program can also specify a field width character:

.. code-block:: python
    :linenos:
    :caption: Specifying a field width character

    x = 0.1
    y = 123.456789

    print(f"My number: '{x:10.1}' and '{y:10.1}'")
    print(f"My number: '{x:10.2}' and '{y:10.2}'")
    print(f"My number: '{x:10.3}' and '{y:10.3}'")
    print(f"My number: '{x:10.4}' and '{y:10.4}'")
    print(f"My number: '{x:10.5}' and '{y:10.5}'")
    print(f"My number: '{x:10.6}' and '{y:10.6}'")

    print()
    print(f"My number: '{x:10.1f}' and '{y:10.1f}'")
    print(f"My number: '{x:10.2f}' and '{y:10.2f}'")
    print(f"My number: '{x:10.3f}' and '{y:10.3f}'")
    print(f"My number: '{x:10.4f}' and '{y:10.4f}'")
    print(f"My number: '{x:10.5f}' and '{y:10.5f}'")
    print(f"My number: '{x:10.6f}' and '{y:10.6f}'")

The format ``10.2f`` does not mean 10 digits before the decimal and two after.
It means a total field width of 10. So there will be 7 digits before the
decimal, the decimal which counts as one more, and 2 digits after.

.. code-block:: text
    :caption: The output:

    My number: '       0.1' and '     1e+02'
    My number: '       0.1' and '   1.2e+02'
    My number: '       0.1' and '  1.23e+02'
    My number: '       0.1' and '     123.5'
    My number: '       0.1' and '    123.46'
    My number: '       0.1' and '   123.457'

    My number: '       0.1' and '     123.5'
    My number: '      0.10' and '    123.46'
    My number: '     0.100' and '   123.457'
    My number: '    0.1000' and '  123.4568'
    My number: '   0.10000' and ' 123.45679'
    My number: '  0.100000' and '123.456789'


Printing Dollars and Cents
--------------------------

If you want to print a floating point number for cost, you use an f. See below:

.. code-block:: python
    :linenos:
    :caption: Specifying a field width character

    cost1 = 3.07
    tax1 = cost1 * 0.06
    total1 = cost1 + tax1

    print(f"Cost:  ${cost1:5.2f}")
    print(f"Tax:    {tax1:5.2f}")
    print(f"-------------")
    print(f"Total: ${total1:5.2f}")

Remember! It would be easy to think that %5.2f would mean five digits, a
decimal, followed by two digits. But it does not. It means a total field width
of five, including the decimal and the two digits after. Here's the output:

.. code-block:: text
    :caption: The output:

    Cost:  $ 3.07
    Tax:     0.18
    -------------
    Total: $ 3.25

Danger! The above code has a mistake that is very common when working with
financial transactions. Can you spot it? Try spotting it with the expanded
code example below:

.. code-block:: python
    :linenos:
    :caption: Specifying a field width character

    cost1 = 3.07
    tax1 = cost1 * 0.06
    total1 = cost1 + tax1

    print(f"Cost:  ${cost1:5.2f}")
    print(f"Tax:    {tax1:5.2f}")
    print(f"-------------")
    print(f"Total: ${total1:5.2f}")

    cost2 = 5.07
    tax2 = cost2 * 0.06
    total2 = cost2 + tax2

    print()
    print(f"Cost:  ${cost2:5.2f}")
    print(f"Tax:    {tax2:5.2f}")
    print(f"-------------")
    print(f"Total: ${total2:5.2f}")

    print()
    grand_total = total1 + total2
    print(f"Grand total: ${grand_total:5.2f}")

.. code-block:: text
    :caption: The output:

    Cost:  $ 3.07
    Tax:     0.18
    ------------
    Total: $ 3.25

    Cost:  $ 5.07
    Tax:     0.30
    -------------
    Total: $ 5.37

    Grand total: $ 8.63

Spot the mistake? You have to watch out for rounding errors! Look at that
example, it seems like the total should be ``$ 8.62`` but it isn't.

Print formatting doesn't change the number, only what is output! If we changed
the print formatting to include three digits after the decimal the reason for
the error becomes more apparent:

.. code-block:: text
    :caption: The output:

    Cost:  $3.070
    Tax:    0.184
    -------------
    Total: $3.254

    Cost:  $5.070
    Tax:    0.304
    -------------
    Total: $5.374

    Grand total: $8.628

Again, formatting for the display does not change the number. Use the round
command to change the value and truly round. See below:

.. code-block:: python
    :linenos:
    :caption: Specifying a field width character

    cost1 = 3.07
    tax1 = round(cost1 * 0.06, 2)
    total1 = cost1 + tax1

    print(f"Cost:  ${cost1:5.2f}")
    print(f"Tax:    {tax1:5.2f}")
    print(f"-------------")
    print(f"Total: ${total1:5.2f}")

    cost2 = 5.07
    tax2 = round(cost2 * 0.06, 2)
    total2 = cost2 + tax2

    print()
    print(f"Cost:  ${cost2:5.2f}")
    print(f"Tax:    {tax2:5.2f}")
    print(f"-------------")
    print(f"Total: ${total2:5.2f}")

    print()
    grand_total = total1 + total2
    print(f"Grand total: ${grand_total:5.2f}")

.. code-block:: text
    :caption: The output:


    Cost:  $ 3.07
    Tax:     0.18
    -------------
    Total: $ 3.25

    Cost:  $ 5.07
    Tax:     0.30
    -------------
    Total: $ 5.37

    Grand total: $ 8.62

The round command controls how many digits after the decimal we round to. It
returns the rounded value but does not change the original value. See below:

.. code-block:: python
    :linenos:
    :caption: Specifying a field width character

    x = 1234.5678
    print(round(x, 2))
    print(round(x, 1))
    print(round(x, 0))
    print(round(x, -1))
    print(round(x, -2))

See below to figure out how feeding the round() function values like -2 for the
digits after the decimal affects the output:

.. code-block:: text
    :caption: The output:

    1234.57
    1234.6
    1235.0
    1230.0
    1200.0

Use in Pygame
-------------
We don't just have to format strings for print statements. The example timer.py
uses string formatting and blit's the resulting text to the screen to make an
on-screen timer:

.. code-block:: python
    :linenos:
    :caption: Specifying a field width character

    # Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes,seconds)

    # Blit to the screen
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250, 250])