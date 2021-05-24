from random import *
from tkinter import *
from corpus import *
from pyperclip import *


def define_name():
    global name
    name = inputtxt.get(1.0, "end-1c")


def create_glow():
    global glow
    glow = choice(dict['citing evidence'])


def create_grow():
    global grow
    grow = choice(dict['organizing handwriting'])


def generate_comment():
    global final_com
    final_com = f'{name}, {choice(glows)} {glow}. {choice(grows_pre)}, {choice(grows_effort)} {grow}.'
    # copy(final_com)
    print(final_com)


# Top level parent window
frame = Tk()
frame.title("TextBox Input")
frame.geometry('400x150')

# Define interface buttons/text boxes
inputtxt = Text(frame, height=2, width=7)
nameButton = Button(frame, text="Input Name", command=define_name)
glowButton = Button(frame, text="Citing Evidence", command=create_glow)
growButton = Button(frame, text="Organizing Handwriting", command=create_grow)
commentButton = Button(frame, text="Generate Comment", command=generate_comment)

# Pack interface buttons/text boxes
inputtxt.pack()
nameButton.pack()
glowButton.pack(side=LEFT)
growButton.pack(side=LEFT)
commentButton.pack(side=LEFT)

# Run the application.
frame.mainloop()


# TODO: Format GUI with name input on top; glows packed beneath; grows packed beneath.

# TODO: Build corpus.

# TODO: Create text output for copying and pasting.

# TODO: Use pyperclip to automatically copy comment upon completion.

# TODO: Incorporate functionality with the Google Classroom API.
