My final project for CS50 is a Flask web application that, through Python, highlights sentences a different color depending on its length.
It is inspired by Gary Provost's quote, which is displayed upon the website first booting up.
The purpose of this website is to help improve the quality of writing by checking for sentence length variety,
which can prevent writing from sounding boring or monotonous.

The frame of the website is made by using week 9's lab, birthday, which I modified into the final project.
I referred to finance as well in order to make sure the jinja code was correct.
As such, the project uses the standard Flask layout:

In the static folder are the favicon and the styles.css files.
The favicon, or the shortcut icon, is a public domain feather in an ink drawing, the source of which is linked in index.html.
The styles.css folder contains various self made css classes.
In comments are the left and right classes, which I initially wanted to use in order to have the input and output window side by side.
I decided against using them as layering the input and output on top of each other would make it easier to scale and more readable on smaller devices.

In the templates folder is the sole html file, index.html.
The idea behind file was pretty cut and dry,and aside from various css designs (like the aforementioned side-by-side windows and smaller decisions like font size),
the idea behind this file has stayed largely identical to when I first idealized the website. 
It consists of a paragraph area with jinja if statements to control the highlight color of the output text depending on sentence length. 
Additionally, there is a text area containing input and a button that reloads the page to update said output text.

app.py contains the source code which generates the website's html.
It works by taking an input text, splitting it into sentences that are then stored in a list,
taking that list and creating a dictionary with the lengths of every sentence,
and then using that to generate a highlighted output per index.html's if-else statements.

And finally, the requirements.txt file documents the required imports for the program to run. 
