Unicorn HAT Words
=================

This library contains several utility modules to display words on the Unicorn HAT.
It relies on the regular 'unicornhat' module, as well as 'numpy', 'time', 'datetime', 'random', 'sys'.
It is unknown whether there is any implicit support for the Sense HAT or the Scroll pHat.

Like all GPIO projects, you usually need sudo rights to run these modules.

Since the HAT is an 8x8 matrix, and letters easily take up 5x5 pixels or more, this
library contains a number of variations to cram more info into less space. The most
obvious variation is a matrix banner; others are the 'panner', which pans over multiple
lines of text, and 'quatro', which uses different shades of the same color to display
up to four partially overlapping characters at the same time (very useful for a clock).

All of the major modules have a 'main' function to demo themselves.

Font files
----------

Various font files are available. The '45font' files are 4x5; the '55font' files are
5x5. The 'mixfont' mixes 4x5 and 5x5. The fonts can be compiled into a Python string using
'compilefont.py'.

If I recall correctly, only the 5x5 fonts are used actively, through 'fonts.py'.


Colors
------

'colors.py' is a minimal module that can provide a randomly chosen, agreeable pastel color palette
as input to the other modules.


Matrix
======

The 'matrix.py' module allows you to write matrix texts. It has three major modes, represented by methods of the same name:

* matrix - scrolls text to the left
* rocket - scrolls text upwards
* panner - scrolls from the top left to the bottom right of a text, which is set over multiple lines by means of the 'width' parameter


Quatro
======

The 'quatro.py' module writes up to four letters at the same time, using different shades
of the same color to distinguish the individual, overlapping letters. These are the main
methods:

* word - Write a string, four letters at the same time
* num - Write a number, e.g. 1234
* twonums - Write two numbers, e.g. 12 and 34


Applications
============

Clock
-----

The 'clock.py' module displays the year, date and time using Quatro.


Typotron
--------

Type anything, and it gets displayed in Matrix form.

