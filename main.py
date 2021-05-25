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
    final_com = f'{name}, {choice(glows_pre)} {glow}. {choice(grows_pre)}, {choice(grows_effort)} {grow}.'
    copy(final_com)
    print(final_com)


# Top level parent window
frame = Tk()
frame.title("Assignment Commenter")
frame.geometry('600x400')

# Define interface buttons/text boxes
inputtxt = Text(frame, height=1, width=15)
nameButton = Button(frame, text="Input Name", command=define_name)
citeButton_glow = Button(frame, text="Citing Evidence", command=lambda: create_glow("Citing Evidence"))
citeButton_grow = Button(frame, text="Citing Evidence", command=lambda: create_grow("Citing Evidence"))
orgButton_glow = Button(frame, text="Organizing Handwriting", command=lambda: create_glow("Organizing Handwriting"))
orgButton_grow = Button(frame, text="Organizing Handwriting", command=lambda: create_grow("Organizing Handwriting"))


commentButton = Button(frame, text="Generate Comment", command=generate_comment)

# Grid-align text input and define_name button.
inputtxt.grid(row=0, column=3)
nameButton.grid(row=1, column=3)

# Grid-align Glow Section label.
glowLabel = Label(frame, text="Glows")
glowLabel.grid(row=4, column=3, pady=10)

# Grid-align "Glow" section buttons.
citeButton_glow.grid(row=5, column=1, padx=10, pady=10)
orgButton_glow.grid(row=5, column=2)

# Grid-align "Grow" section label
growLabel = Label(frame, text="Grows")
growLabel.grid(row=6, column=3, pady=10)

# Grid-align "Grow" section buttons.
orgButton_grow.grid(row=7, column=2)
citeButton_grow.grid(row=7, column=1)

# Grid-align generate_comment button.
commentButton.grid(row=8, column=3, pady=10)

# Run the application.
frame.mainloop()


# TODO: Develop corpus.

# TODO: Format GUI with name input on top; glows packed beneath; grows packed beneath.

# TODO: Create text output for copying and pasting.

# TODO: Reorganize file structure.

# TODO: Incorporate functionality with the Google Classroom API.

# TODO: Create an executable of the application with API functionality.
