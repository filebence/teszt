from tkinter import *
from PIL import ImageTk, Image

first_names = ["Baker", "Brice", "Dustin", "Cage", "Orson"]
last_names = ["Barney", "Whaley", "Cooper", "Billton", "Perez "]

def name_gen():
    import random
    full_name.set(random.choice(first_names) + " " + random.choice(last_names))

def exit_program():
    import sys
    sys.exit()

root = Tk()
root.title("Random name generator")
root.geometry("622x350")
root.resizable(False, False)

background_photo = ImageTk.PhotoImage(Image.open("python.png"))
label_photo = ImageTk.PhotoImage(Image.open("label.gif"))
button_photo = ImageTk.PhotoImage(Image.open("button.gif"))
button1_photo = ImageTk.PhotoImage(Image.open("button1.gif"))

background = Label(root, image = background_photo).pack()

full_name = StringVar()

label = Label(root, image = label_photo, textvariable = full_name, bg = "black", compound = CENTER, bd = 0, font = ("Arial", 20), highlightthickness = 0, padx = 0, pady = 0)
label.place(x = 211, y = 50)

button = Button(root, image = button_photo, compound = CENTER, bg = "black", text = "Generate", font = ("Arial", 25), bd = 1, highlightthickness = 0, command = name_gen, padx = 0, pady = 0)
button.place(x = 231, y = 220)

button1 = Button(root, image = button1_photo, compound = CENTER, bg = "black", text = "Exit", font = ("Arial", 20), bd = 1, highlightthickness = 0, padx = 0, pady = 0, command = exit_program)
button1.place(x = 244, y = 284)

root.mainloop()