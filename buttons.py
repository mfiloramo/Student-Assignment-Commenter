from tkinter import *
from main import *

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


# orgButton_grow.cget('text')

# Pack interface buttons/text boxes
inputtxt.pack()
nameButton.pack(side=TOP)

citeButton_glow.pack(side=LEFT)
citeButton_grow.pack(side=LEFT)
orgButton_grow.pack(side=RIGHT)
orgButton_glow.pack(side=RIGHT)

commentButton.pack(padx=10, side=LEFT)