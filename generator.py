"""
author:cpython420
"""
from tkinter import *
import string
import random
import csv

window = Tk()
window.title("Password generation")
window.resizable(False, False)

"""
try-except error handling added
"""

def generatePassword(len):
    try:
        len = int(len)
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for i in range(len))
        pwBox.delete(0, END)                   #vymaze obsah pwBox
        pwBox.insert(0, password)              #vlozi vygenerovane heslo
        with open("list.txt", "a") as outfile: #zapise heslo do .txt subora, append, aby sa nezmazali predchadzajuce
            outfile.write(password + "\n")     #kazde heslo do noveho radku
        print("Success: "+password)
        
    except ValueError:
        print("Please, type in an integer.")
            
    
"""
tkinter widgets
"""  

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
    command=lambda: generatePassword((pwLen.get())))

"""
render widgetov
"""

pwBox.grid(row=0, column=0,sticky="nsew") #tu sa zobrazi vygenerovane heslo
pwLen.grid(row=0, column=1, sticky="nsew") #pocet znakov hesla
pwButton.grid(row=1, column=0, columnspan=3, sticky="nsew") #vygeneruje heslo o danom pocte znakov po kliknuti

window.mainloop() 
