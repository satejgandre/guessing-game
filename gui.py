import random
from tkinter import *
#FUNCTIONS
def check():
    guess = int(guessbox.get())
    if guess is number: subheading.config(text="Correct!")
    elif guess > number: subheading.config(text="Less...")
    else: subheading.config(text="More...")
def reset():
    global number
    number = random.randint(0,100)
#GUI OBJECTS
reset()
root = Tk()
root.title("Guessing Game")
root.minsize(400, 150)
root.maxsize(400, 150)
root.config(bg="black")
heading = Label(root, text="Guess a number from 0 to 100", bg="black", fg="limegreen")
subheading = Label(root, text="Use the field below to enter your guess", bg="black", fg="limegreen")
guessbox = Entry(root, bd=3, width=10, bg="limegreen", fg="black")
enterbtn = Button(root,bd=3, text='Guess', bg="limegreen", fg="black", command=check)
resetbtn = Button(root,bd=3, text='Reset', bg="limegreen", fg="black", command=reset)
heading.pack(pady=5)
subheading.pack()
guessbox.pack(padx=3,pady=3)
enterbtn.pack(side='left', expand=True)
resetbtn.pack(side='right', expand=True)
root.mainloop()