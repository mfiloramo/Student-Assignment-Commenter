from random import *
from tkinter import *
from corpus import *
from pyperclip import *
from pprint import *


def define_name():
    global name
    name = inputtxt.get(1.0, "end-1c")


def create_glow(text):
    global glow
    glow = choice(skills_dict[text])


def create_grow(text):
    global grow
    grow = choice(skills_dict[text])


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

glow_dict = {}
grow_dict = {}

for a, b in zip(skills_dict.keys(), range(1, 17)):
    glow_dict[b] = Button(frame, text=a, command=lambda: create_glow(b))
    grow_dict[b] = Button(frame, text=a, command=lambda: create_grow(b))

# Position the buttons within the GUI.
list_rows = (1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4)
list_cols = (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

for w, x, y, z in zip(glow_dict.values(), grow_dict.values(), list_rows, list_cols):
    w.grid(row=y, column=z)
    x.grid(row=y+8, column=z)

commentButton = Button(frame, text="Generate Comment", command=generate_comment)

# Grid-align text input and define_name button.
inputtxt.grid(row=0, column=2)
nameButton.grid(row=0, column=3)

# Grid-align Glow Section label.
# glowLabel = Label(frame, text="Glows")
# glowLabel.grid(row=4, column=3, pady=10)

# Grid-align "Grow" section label
# growLabel = Label(frame, text="Grows")
# growLabel.grid(row=6, column=3, pady=10)

# Grid-align generate_comment button.
commentButton.grid(row=14, column=2, pady=10)

# Run the application.
frame.mainloop()


# TODO: Develop corpus.

# TODO: Format GUI with name input on top; glows packed beneath; grows packed beneath.

# TODO: Create text output for copying and pasting.

# TODO: Reorganize file structure.

# TODO: Incorporate functionality with the Google Classroom API.

# TODO: Create an executable of the application with API functionality.
