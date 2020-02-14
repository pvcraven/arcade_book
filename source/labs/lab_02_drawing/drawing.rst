.. _lab-02:

Lab 2: Draw a Picture
=====================

Your assignment: Draw a picture.

The goal:

* Practice looking up API documentation - useful for using any code library
* Practice calling functions - a basic building block of all computer programs
* Practice working with RGB colors - used in graphics, web design, and even LED lighting
* Practice commenting and formatting code properly - required to make code maintainable
* Practice working with graphics coordinates - also used in document layout and web design

Requirements
------------

To get full credit:

* Use the same project and repository that you used for Lab 01.
  If you forked your repository from mine, you should already have a folder
  for lab 2. Use that folder, and the ``lab_02.py`` file inside. Otherwise create one.
* Use several different colors.
* Make a coherent picture.
  Don't make abstract art with random shapes, because that doesn't require a full
  application of what we've learned to a real use-case.
* Use multiple types of graphic functions. Include
  circles, ellipses, rectangles, lines, polygons and more in your drawing.
  It is certainly
  possible to make great art with just squares, but the point of the lab is to
  practice using multiple functions.
* Use a single blank line in your code to break up logical sections.
  For example, when drawing
  a tree, put a blank line ahead of, and after. See the example code below.
* Use comments effectively. For example, when drawing a tree, put a comment at
  the start of those drawing commands that says ``# Draw a tree``. Remember
  to put one space after the ``#`` sign.
* Put spaces after commas for proper "style."
* Use PyCharm to inspect your code for warnings. Fix warnings that you encounter.

Tips
----

To select new colors use: https://www.google.com/search?q=color+picker

Copy the values for Red, Green, and Blue from the color picker.
Do not worry about colors for hue, saturation, or brilliance.

Keep in mind the order of code. Shapes drawn first will be at the "back."
Shapes drawn later will be drawn on top of the other shapes.

Also, remember you can look up the available commands, called the "API" at:
https://arcade.academy

Example Lab
-----------

.. image:: final_program.png

.. literalinclude:: final_program.py
    :language: python
    :linenos:

Other Examples
--------------

Here are some images from prior years:

.. raw:: html

    <!-- Create your slider and add images -->
    <button class="btn prev"><span class="fa fa-arrow-circle-left"></span> Prev Image</button>
    <button class="btn next">Next Image <span class="fa fa-arrow-circle-right"></span></button>
    <br />
    <div id="slider">
        <img src="../../_static/lab_02_images/001.png" alt="">
        <img data-src="../../_static/lab_02_images/002.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/003.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/004.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/005.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/006.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/007.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/008.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/009.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/010.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/011.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/012.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/013.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/014.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/015.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/016.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/017.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/018.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/019.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/020.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/021.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/022.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/023.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/024.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/025.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/026.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/027.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/028.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/029.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/030.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/031.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/032.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/034.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/035.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/036.png" src="" alt="">
        <img data-src="../../_static/lab_02_images/037.png" src="" alt="">
    </div>

    <!-- Include slider JS file -->
    <script src="//cdnjs.cloudflare.com/ajax/libs/ideal-image-slider/1.5.1/ideal-image-slider.min.js"></script>
    <!-- Create your slider -->
    <script>
    var slider = new IdealImageSlider.Slider({
      selector: '#slider',
      onStart: function(){
        console.log('onStart');
      }
    });
    document.querySelector('.prev').addEventListener('click', function(e){
        e.preventDefault();
        // Use the previousSlide() API method
        slider.previousSlide();
    });
    document.querySelector('.next').addEventListener('click', function(e){
        e.preventDefault();
        // Use the nextSlide() API method
        slider.nextSlide();
    });
    </script>

Turn In
-------

Refer back to :ref:`git-quick-ref` for a reminder on how to turn in this lab.
You need to do a:

* ``git add *``
* ``git commit -m "Lab 02"``
* ``git push``
* Find the lab on ``github.com``
* Copy the URL
* Go to the class website and turn in the lab.

Remember, if there are errors on the lab that you want to correct and get full
credit for, you can. Once corrected, go through all the steps above. You must
resubmit the lab to the class website (not just upload to git) otherwise I don't
get notified to look at the lab again. You have 7 days (to the hour and minute)
to submit the lab again.