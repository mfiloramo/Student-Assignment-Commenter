from random import *
from tkinter import *
from corpus import *
from pyperclip import *


def define_name():
    global name
    name = inputtxt.get(1.0, "end-1c")


def create_glow(text):
    global glow
    glow = choice(dict[text])


def create_grow(text):
    global grow
    grow = choice(dict[text])


def generate_comment():
    global final_com
    final_com = f'{name}, {choice(glows)} {glow}. {choice(grows_pre)}, {choice(grows_effort)} {grow}.'
    copy(final_com)
    print(final_com)


# Top level parent window
frame = Tk()
frame.title("TextBox Input")
frame.geometry('700x150')

# Define interface buttons/text boxes
inputtxt = Text(frame, height=2, width=7)
nameButton = Button(frame, text="Input Name", command=define_name)
citeButton_glow = Button(frame, text="citing evidence", command=lambda: create_glow("citing evidence"))
citeButton_grow = Button(frame, text="citing evidence", command=lambda: create_grow("citing evidence"))
orgButton_glow = Button(frame, text="organizing handwriting", command=lambda: create_glow("organizing handwriting"))
orgButton_grow = Button(frame, text="organizing handwriting", command=lambda: create_grow("organizing handwriting"))
commentButton = Button(frame, text="Generate Comment", command=generate_comment)

# Pack interface buttons/text boxes
inputtxt.grid(row=0, column=0)
nameButton.grid(row=1, column=0)

citeButton_glow.grid(row=1, column=1)
citeButton_grow.grid(row=2, column=1)
orgButton_glow.grid(row=1, column=2)
orgButton_grow.grid(row=2, column=2)


commentButton.grid(row=1, column=4)

# Run the application.
frame.mainloop()


# TODO: Format GUI with name input on top; glows packed beneath; grows packed beneath.

# TODO: Develop corpus.

# TODO: Create text output for copying and pasting.

# TODO: Incorporate functionality with the Google Classroom API.
