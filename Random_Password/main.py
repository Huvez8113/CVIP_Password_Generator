import tkinter as tk
from random import randint
from tkinter import messagebox as mb

root = tk.Tk();
root.title("Random Password Generator")
root.geometry("500x300")



def new_rand():
    pw_entry.delete(0, "end")

    pw_length = int(my_entry.get())

    my_password = ''

    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    pw_entry.insert(0, my_password)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())


lf = tk.LabelFrame(root,text="How many characters You need for Password?")
lf.pack(pady=20)

my_entry = tk.Entry(lf,font=("Helvetica",24))
my_entry.pack(pady=20, padx=20)

pw_entry = tk.Entry(root, text='',font=("Helvetica",24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

my_frame = tk.Frame(root)
my_frame.pack(pady=20)

my_button = tk.Button(my_frame,text="Generate Strong Password",command=new_rand)
my_button.grid(row=0,column=0,padx=10)

clip_button = tk.Button(my_frame, text="Copy to ClipBoard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()