from tkinter import *
import pyperclip
import random

root = Tk()
root.geometry("400x400") 
passstr = StringVar()
passlen = IntVar()
passlen.set(0)

def generate():
    # storing the keys in a list which will be used to generate 
    # the password 
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']

    
    password = ""

    
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
        passstr.set(password)

# function to copy the password to the clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

# Creating a text label widget
Label(root, text="Password Generator Application", font="calibri 20 bold").pack()

# Creating a text label widget
Label(root, text="Enter password length").pack(pady=3)

# Creating a entry widget to take password length entered by the 
# user
Entry(root, textvariable=passlen).pack(pady=3)

# button to call the generate function
Button(root, text="Generate Password", command=generate).pack(pady=7)

# entry widget to show the generated password
Entry(root, textvariable=passstr).pack(pady=3)

Button(root, text="Copy to clipboard", command=copytoclipboard).pack()

root.mainloop()