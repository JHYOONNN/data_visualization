from tkinter import *
from PIL import Image, ImageTk
import time
import capture_img as cap_img
import emotion_get as emo

root = Tk()

ted = Image.open("Ted_fixed.png")
photoimg = ImageTk.PhotoImage(ted)
canvas = Canvas(root, width=1000, height=500)
canvas.pack()
my_color = '#%02x%02x%02x' % (30, 30, 30)
ted_cr_image = canvas.create_image(850, 250, image = photoimg)

mouse = canvas.create_arc(830, 180 -5,880,180 +5, start = 0, extent = 180, style = 'arc', width = 3, outline = my_color)

root.mainloop()