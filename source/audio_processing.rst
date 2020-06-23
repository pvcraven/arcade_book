:orphan:

Audio Processing
================

#. Apply noise reduction
#. Graphic Equalization 200Hz @ 6db boost, 4,000MHz @ -3db loss.
#. Compressor = Threshold -18db, Noise Floor -40db, Ratio 2:1, Attack Time 0.2s,
   Release Time 1.0s, un-check 'Make up gain' and 'Compress based on peaks'.
#. Low Pass Filter 10,000Hz @ 24 db roll off. Reduces 'Ssssss' and other high pitched sounds.
#. High Pass Filter 30Hz @ 24 db roll off. Reduces low hums (like a fridge) and gravely voice grumbles.
#. Normalize -1db (this should ALWAYS be your last step).