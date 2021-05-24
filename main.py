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
    copy(final_com)
    # print(final_com)


# Top level parent window
frame = Tk()
frame.title("TextBox Input")
frame.geometry('200x150')

# TextBox Creation
inputtxt = Text(frame, height=2, width=7)
inputtxt.pack()

# Define Name Button
nameButton = Button(frame, text="Input Name", command=define_name)
nameButton.pack()

# Define Glow Button
glowButton = Button(frame, text="Test Glow", command=create_glow)
glowButton.pack(side=LEFT)

# Define Grow Button
growButton = Button(frame, text="Test Grow", command=create_grow)
growButton.pack(side=LEFT)

# Define Generate Comment Button
commentButton = Button(frame, text="Generate Comment", command=generate_comment)
commentButton.pack(side=LEFT)

# Run the application.
frame.mainloop()


# TODO: Format GUI with name input on top; glows packed beneath; grows packed beneath.

# TODO: Build dictionaries and lists.

# TODO: Create text output for copying and pasting.

# TODO: Use pyperclip to automatically copy comment upon completion.

# TODO: Incorporate functionality with the Google Classroom API.
