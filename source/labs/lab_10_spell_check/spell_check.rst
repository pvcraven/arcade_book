.. _lab-10:

Lab 10: Spell Check
===================

This lab shows how to create a spell checker.

Requirements
------------

Write a single program in Python that checks the spelling of the first chapter
of "Alice In Wonderland." First use a linear search, then use a binary search.
Print the line number along with the word that does not exist in the dictionary.

Follow the steps below carefully. If you don't know how to accomplish one step,
ask before moving on to the next step.

Steps to complete
-----------------

1.  Open the Lab 10 - Spell Check directory for your project. There you will find

    * `AliceInWonderLand200.txt` - First chapter of "Alice In Wonderland"
    * `dictionary.txt` - A list of words
    
2.  Start a Python file for your project.
3.  It is necessary to split apart the words in the story so that they may be
    checked individually. It is also necessary to remove extra punctuation and
    white-space. Unfortunately, there is not any good way of doing this with
    what the book has covered so far. The code to do this is short, but a full
    explanation is beyond the scope of this class. Include the following
    function in your program. Remember, function definitions should go at
    the top of your program just after the imports. We'll call this function
    in a later step.

.. code-block:: python
    :caption: Function to split apart words in a string and return them as a list

    import re

    # This function takes in a line of text and returns
    # a list of words in the line.
    def split_line(line):
        return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

This code uses a *regular expression* to split the text apart. Regular
expressions are very powerful and relatively easy to learn. If you'd like to
know more about regular expressions, see:

http://regexone.com/

4.  Read the file ``dictionary.txt`` into an array. Go back to
    :ref:`reading_into_an_array` for example code on how to do
    this. This does *not* have anything to do with the ``import`` command, libraries,
    or modules. Don't call the dictionary ``word_list`` or something generic
    because that will be confusing. Call it ``dictionary_list`` or a different
    term that is specific.
5.  Close the file.
6.  Print ``--- Linear Search ---``
7.  Open the file ``AliceInWonderLand200.txt``
8.  We are *not* going to read the story into a list. Do not create a new list
    here like you did with the dictionary.
9.  Start a ``for`` loop to iterate through each line.
10. Call the ``split_line`` function to split apart the line of text in the
    story that was just read in. Store the list that the function returns in a
    new variable named ``word_list``. Remember, just calling the function won't do
    anything useful. You need to assign a variable equal (``word_list``) to the result.
    If you've forgotten now to capture the return value from a function, see
    :ref:`capturing_returned_values`.
11. Start a nested ``for`` loop to iterate through each word in the words list.
    This should be inside the ``for`` loop that runs through each line in the file.
    (One loop for each line, another loop for each word in the line.)
12. Using a linear search, check the current word against the words in the
    dictionary. See :ref:`linear_search`
    for example code on how to do this. The linear search is just three lines
    long. When comparing to the word to the other words in the dictionary,
    convert the word to uppercase. In your ``while`` loop just use ``word.upper()``
    instead of ``word`` for the key. This linear search will exist inside the ``for``
    loop created in the prior step. We are looping through each word in the
    dictionary, looking for the current word in the line that we just read in.
13. If the word was not found, print the word. Don't print anything if you do
    find the word, that would just be annoying.
14. Close the file.
15. Make sure the program runs successfully before moving on to the next step.
16. Create a new variable that will track the line number that you are on.
    Print this line number along with the misspelled from the prior step.
17. Make sure the program runs successfully before moving on to the next step.
18. Print ``--- Binary Search ---``
19. The linear search takes quite a while to run. To temporarily disable it,
    it may be commented out by using three quotes before and after that block
    of code. Ask if you are unsure how to do this.
20. Repeat the same pattern of code as before, but this time use a binary
    search.
    For the binary search, go back to :ref:`binary_search`.
    Much of the code from the linear search may be copied, and it is
    only necessary to replace the lines of code that represent the linear
    search with the binary search.
21. Note the speed difference between the two searches.
22. Make sure the linear search is re-enabled, if it was disabled while
    working on the binary search.
23. Upload the final program or check in the final program.

Example Run
-----------

.. code-block:: text

    --- Linear Search ---
    Line 3  possible misspelled word: Lewis
    Line 3  possible misspelled word: Carroll
    Line 46  possible misspelled word: labelled
    Line 46  possible misspelled word: MARMALADE
    Line 58  possible misspelled word: centre
    Line 59  possible misspelled word: learnt
    Line 69  possible misspelled word: Antipathies
    Line 73  possible misspelled word: curtsey
    Line 73  possible misspelled word: CURTSEYING
    Line 79  possible misspelled word: Dinah'll
    Line 80  possible misspelled word: Dinah
    Line 81  possible misspelled word: Dinah
    Line 89  possible misspelled word: Dinah
    Line 89  possible misspelled word: Dinah
    Line 149  possible misspelled word: flavour
    Line 150  possible misspelled word: toffee
    Line 186  possible misspelled word: croquet
    --- Binary Search ---
    Line 3  possible misspelled word: Lewis
    Line 3  possible misspelled word: Carroll
    Line 46  possible misspelled word: labelled
    Line 46  possible misspelled word: MARMALADE
    Line 58  possible misspelled word: centre
    Line 59  possible misspelled word: learnt
    Line 69  possible misspelled word: Antipathies
    Line 73  possible misspelled word: curtsey
    Line 73  possible misspelled word: CURTSEYING
    Line 79  possible misspelled word: Dinah'll
    Line 80  possible misspelled word: Dinah
    Line 81  possible misspelled word: Dinah
    Line 89  possible misspelled word: Dinah
    Line 89  possible misspelled word: Dinah
    Line 149  possible misspelled word: flavour
    Line 150  possible misspelled word: toffee
    Line 186  possible misspelled word: croquet
