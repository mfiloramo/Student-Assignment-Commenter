from random import *
from tkinter import *
from corpus import *
from pyperclip import *
from itertools import *
from PIL import Image, ImageTk


def define_name():
    global name
    name = inputtxt.get(1.0, "end-1c")


def create_glow(text):
    global glow
    glow = choice(skills_dict[text])
    return glow


def create_grow(text):
    global grow
    grow = choice(skills_dict[text])
    return grow


def generate_comment():
    global final_com
    final_com = f'{name}, {choice(glows_pre)} {glow}. {choice(grows_pre)}, {choice(grows_effort)} {grow}.'
    copy(final_com)


# Top level parent window
frame = Tk()
frame.title("Assignment Commenter")
frame.geometry('600x400')

# Add a background image to the parent Widget.
image1 = Image.open('image.jpg')
image = ImageTk.PhotoImage(image1)
label1 = Label(image=image)
label1.image = image
label1.place(x=0, y=0)

# Define interface buttons/text boxes
inputtxt = Text(frame, height=1, width=15)
nameButton = Button(frame, text="Input Name", command=define_name)
commentButton = Button(frame, background='#296dff', text="Generate Comment", command=generate_comment)

glow_dict = {}
grow_dict = {}

for i in skills_dict.keys():
    glow_dict[i] = Button(frame, background='#46ff29', text=i, command=lambda i=i: create_glow(i))
    grow_dict[i] = Button(frame, background='red', text=i, command=lambda i=i: create_grow(i))

# Iteratively position the buttons within the GUI.
grid_coors = product('1234', repeat=2)

for w, x, y in zip(glow_dict.values(), grow_dict.values(), grid_coors):
    w.grid(row=int(y[0])+1, column=y[1])
    x.grid(row=int(y[0])+8, column=y[1])

# Grid-align text input and define_name button.
inputtxt.grid(row=0, column=2)
nameButton.grid(row=0, column=3)

# Grid-align Glow Section label.
glowLabel = Label(frame, text="Glows")
glowLabel.grid(row=1, column=3, pady=10)

# Grid-align "Grow" section label
growLabel = Label(frame, text="Grows")
growLabel.grid(row=6, column=3, pady=10)

# Grid-align generate_comment button.
commentButton.grid(row=14, column=3, pady=35)

# Run the application.
frame.mainloop()


# TODO: Reorganize file structure (consider making the application a class, where each instance is based on ass. type.

# TODO: Incorporate functionality with the Google Classroom API.
