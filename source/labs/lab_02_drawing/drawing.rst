.. _lab-02:

Lab 2: Draw a Picture
=====================

Your assignment: Draw a pretty picture.

The goal:

* Practice looking up API documentation
* Practice calling functions
* Practice working with RGB colors
* Practice commenting and formatting code properly
* Practice working with graphics coordinates

Requirements
------------

To get full credit:

* Use the same project and repository that you used for Lab 01.
  If you forked your repository from mine, you should already have a folder
  for lab 2. Use that folder, and the ``lab_02.py`` file inside. Otherwise create one.
* You must use multiple colors.
* You must have a coherent picture.
  I am not interested in abstract art with random shapes.
* You must use multiple types of graphic functions
  (e.g. circles, rectangles, lines, etc.)
* Use blank lines in the code to break up sections. For example, when drawing
  a tree, put a blank line ahead of, and after.
* Use comments effectively. For example, when drawing a tree, put a comment at
  the start of those drawing commands that says ``# Draw a tree``. Remember
  to put one space after the ``#`` sign.
* Put spaces after commas for proper "style."

Tips
----

To select new colors use:

https://www.google.com/search?q=color+picker

Copy the values for Red, Green, and Blue.
Do not worry about colors for hue, Saturation, or Brilliance.

Please use comments and blank lines to make it easy to follow your program.
If you have 5 lines that draw a robot, group them together with blank lines
above and below. Then add a comment at the top telling the reader what you
are drawing. Refer to the example code at the end of this lab description
to get an idea of how it should be done.

Keep in mind the order of code. Shapes drawn first will be at the "back."
Shapes drawn later will be drawn on top of the other shapes.

Also, remember you can look up the available commands, called the "API" at:

https://arcade.academy

Here is an example image and program:

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

To flip through the images, click the prev/next buttons above the image. The
prev/next buttons below navigate between the different labs.

Turn In
-------

Refer back to :ref:`git-quick-ref` for a reminder on how to turn in this lab.