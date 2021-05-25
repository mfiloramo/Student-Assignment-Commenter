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
# citeButton_glow = Button(frame, text="Citing Evidence", command=lambda: create_glow("Citing Evidence"))
# citeButton_grow = Button(frame, text="Citing Evidence", command=lambda: create_grow("Citing Evidence"))
# orgButton_glow = Button(frame, text="Organizing Handwriting", command=lambda: create_glow("Organizing Handwriting"))
# orgButton_grow = Button(frame, text="Organizing Handwriting", command=lambda: create_grow("Organizing Handwriting"))

test_dicts = {}

# Build a set of buttons.
glow_buttons = []
grow_buttons = []
for a, b in zip(sorted(skills_dict.keys()), range(1, 17)):
    test_dicts[b] = Button(frame, text=a, command=lambda: create_glow(a))

list_rows = (1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4)
list_cols = (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

for x, y, z in zip(test_dicts.values(), list_rows, list_cols):
    x.grid(row=y, column=z)

# for w, x, y, z in zip(glow_buttons, grow_buttons, list_rows, list_cols):
#     w.grid(row=y, column=z, padx=2, pady=5)
#     x.grid(row=y+9, column=z, padx=2, pady=5)

commentButton = Button(frame, text="Generate Comment", command=generate_comment)

# Grid-align text input and define_name button.
inputtxt.grid(row=0, column=3)
nameButton.grid(row=0, column=4)

# Grid-align Glow Section label.
# glowLabel = Label(frame, text="Glows")
# glowLabel.grid(row=4, column=3, pady=10)

# Grid-align "Glow" section buttons.
# citeButton_glow.grid(row=5, column=1, padx=10, pady=10)
# orgButton_glow.grid(row=5, column=2)

# Grid-align "Grow" section label
# growLabel = Label(frame, text="Grows")
# growLabel.grid(row=6, column=3, pady=10)

# Grid-align "Grow" section buttons.
# orgButton_grow.grid(row=7, column=2)
# citeButton_grow.grid(row=7, column=1)

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
