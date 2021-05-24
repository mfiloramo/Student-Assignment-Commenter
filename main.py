import keyword
from random import *
from tkinter import *
from corpus import *
from pyperclip import *


def define_name():
    global name
    name = inputtxt.get(1.0, "end-1c")


def create_glow(text):
    global glow
    glow = choice(dict[orgButton_grow.cget('text')])


def create_grow(text):
    global grow
    text = orgButton_grow.cget('text')
    grow = choice(dict[text])


def generate_comment():
    global final_com
    final_com = f'{name}, {choice(glows)} {glow}. {choice(grows_pre)}, {choice(grows_effort)} {grow}.'
    copy(final_com)
    print(final_com)


global name

# Top level parent window
frame = Tk()
frame.title("TextBox Input")
frame.geometry('700x150')

# Define interface buttons/text boxes
inputtxt = Text(frame, height=2, width=7)
nameButton = Button(frame, text="Input Name", command=create_grow)
orgButton_glow = Button(frame, text="organizing handwriting", command=create_glow)
orgButton_grow = Button(frame, text="organizing handwriting", command=create_grow)
citeButton_glow = Button(frame, text="citing evidence", command=create_glow)
citeButton_grow = Button(frame, text="citing evidence", command=create_grow)
commentButton = Button(frame, text="Generate Comment", command=generate_comment)

# orgButton_grow.invoke()

orgButton_grow.cget('text')

# Pack interface buttons/text boxes
inputtxt.pack()
nameButton.pack(side=TOP)

citeButton_glow.pack(side=LEFT)
citeButton_grow.pack(side=LEFT)
orgButton_grow.pack(side=RIGHT)
orgButton_glow.pack(side=RIGHT)

commentButton.pack(padx=10, side=LEFT)

# Run the application.
frame.mainloop()


# TODO: Format GUI with name input on top; glows packed beneath; grows packed beneath.

# TODO: Develop corpus.

# TODO: Create text output for copying and pasting.

# TODO: Incorporate functionality with the Google Classroom API.
