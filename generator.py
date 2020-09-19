"""
author:cpython420
"""
from tkinter import *
import string
import random
import csv

window = Tk()
window.title("Password generation")


def generatePassword(len):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(len))
    pwBox.delete(0, END)
    pwBox.insert(0, password)
    with open("list.txt", "a") as outfile: #zapise heslo do .txt subora, append, aby sa nezmazali predchadzajuce
        outfile.write(password + "\n")     #kazde heslo do noveho radku
    print(password)
    
    
pwBox = Entry(
    window, 
    width=30, 
    borderwidth=3,
    fg="red")

pwLen = Entry(
    window,
    width=5,
    borderwidth=3,
    fg="blue")

pwButton = Button(
    window, 
    text="Generate password", 
    width=30,
    command=lambda: generatePassword(int(pwLen.get())))





pwBox.grid(row=0, column=0) #tu sa zobrazi vygenerovane heslo
pwLen.grid(row=0, column=1) #pocet znakov hesla
pwButton.grid(row=1, column=0, columnspan=2) #vygeneruje heslo o danom pocte znakov po kliknuti
window.mainloop()
