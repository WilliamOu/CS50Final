“This sentence has five words. Here are five more words. 
Five-word sentences are fine. But several together become monotonous. 
Listen to what is happening. The writing is getting boring. 
The sound of it drones. It’s like a stuck record. The ear demands some variety. 

Now listen. I vary the sentence length, and I create music. Music.
The writing sings. It has a pleasant rhythm, a lilt, a harmony.
I use short sentences. And I use sentences of medium length. 
And sometimes, when I am certain the reader is rested, I will engage him with a sentence of considerable length,
a sentence that burns with energy and builds with all the impetus of a crescendo, 
the roll of the drums, the crash of the cymbals–sounds that say listen to this, it is important.”
- Gary Provost

Deriving inspiration from this quote, my CS50 final is a Flask web application that,
though Python, highlights sentences with different colors depending on their length.

It's an incredibly useful tool, but I have to find an application that performs this function.
Thus I decided to make it myself. Much like the original quote,
the purpose of this website is to help improve the quality of writing by checking for sentence variety,
to help break up sentences that sound either boring or monotonous.
Oh, and the quote is displayed upon the website being launched, alongside a direct citation.

I started the project by using week 9's lab, birthdays, as a Flask template,
as the CS50 academic policy allows for code to be reused,
and I figured it would be much less of a hassle than creating a Flask application from complete scratch.
Throughout the project, I also referred to finance as well in order to make sure the jinja code was correct.
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
Originally, I had planned on using the tokenize function from the nltk import package,
but it required third-party downloads that I could not get working.
I eventually settled on using a function I found in a stack overflow thread (credited in index.html),
which uses a series of regular expressions to split strings into sentences.
Underneath that is the requirements.txt file, which documents the required imports for the program to run.

And that's it. The program is very simple, but it is a strong demonstration of the skills I have learned throughout this course. Thank you CS50 and staff for this wonderful course!
