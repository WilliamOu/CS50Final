# This project uses week 9's lab (birthday) as a flask template
# The styles template is also heavily revised
# favicon link: https://freesvg.org/feather-quill-and-inkwell-silhouette
import os
import re

from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Helper function that splits text into sentences with the help of regular expressions
# Not sure if I need to document this, but it's been renamed to use camel case instead of underscores
# Function credit: Stack Overflow user D Greenberg, https://stackoverflow.com/questions/4576077/how-can-i-split-a-text-into-sentences
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"
digits = "([0-9])"

def SplitIntoSentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    if "..." in text: text = text.replace("...","<prd><prd><prd>")
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

def GetSentenceLength(sentence):
    # Splits the sentence into an array, then counts the number of elements in the array
    # Credit: https://www.delftstack.com/howto/python/python-count-words-in-string/#:~:text=are%205%20words.-,Use%20the%20count()%20Method%20to%20Count%20Words%20in%20Python,based%20on%20the%20given%20substring.
    return len(sentence.split())

defaultInput = "“This sentence has five words. Here are five more words. Five word sentences are fine. But several together become monotonous. Listen to what is happening. The writing is getting boring. The sound of it drones. It’s like a stuck record. The ear demands some variety.\n\nNow listen. I vary the sentence length, and I create music. Music. The writing sings. It has a pleasant rhythm, a lilt, a harmony. I use short sentences. And I use sentences of medium length. And sometimes, when I am certain the reader is rested, I will engage him with a sentence of considerable length, a sentence that burns with energy and builds with all the impetus of a crescendo, the roll of the drums, the crash of the cymbals–sounds that say listen to this, it is important.”"
tokenizedDefaultInputList = SplitIntoSentences(defaultInput)
# Declares an empty dictionary that will store sentences and their respective lengths
tokenizedDefaultInputDict = {}
for token in tokenizedDefaultInputList:
    # Appends each sentence in the list to the dictionary alongside their respective lengths
    tokenizedDefaultInputDict[token] = GetSentenceLength(token)

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input = request.form.get("input")
        # Splits the text into a list of sentences
        tokenizedInputList = SplitIntoSentences(input)

        # Declares an empty dictionary that will store sentences and their respective lengths
        tokenizedInputDict = {}
        for token in tokenizedInputList:
            # Appends each sentence in the list to the dictionary alongside their respective lengths
            tokenizedInputDict[token] = GetSentenceLength(token)

        return render_template("index.html", tokenizedDict=tokenizedInputDict, output=input, credit="")

    else:
        # Credit simply credits Gary Provost as the person who made the quote the first time the program is loaded
        return render_template("index.html", tokenizedDict=tokenizedDefaultInputDict, output="", credit="- Gary Provost")