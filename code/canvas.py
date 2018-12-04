from tkinter import * 
root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()
img = PhotoImage(file='Ted.png')
canvas.create_image(250, 250, image=img)
root.mainloop()