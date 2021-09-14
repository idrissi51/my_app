# My App

# import Modules
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import datetime
import os
# Personal information
# Nots Dossie : c:/Users/MyHP/Notes

my_name = "Mohamed"

# datetime
Time = datetime.datetime.now().strftime("Time: %H:%M:%S /")
Date = datetime.datetime.now().strftime("Date: %d-%m-%y")

# Note Function


def note_function():
    # Buttons Creat note Function
    Button(root, text="Creat Note", command=creat_note).place(x=0, y=95)
    Button(root, text="Show and edit Note",
           command=show_edit).place(x=70, y=95)

# Creat Note Function


def creat_note():
    text1 = Text(root, width=40,
                 height=10, font="arial 10")

    # Clear Function
    def delete_text():
        text1.delete("1.0", "end")

    text1.place(x=0, y=120)

    # save note function
    def choose_note_name():
        global note_name
        global entry_name
        Label(root, text="       Choose a name        ",
              font="arial 10").place(x=0, y=310)
        note_name = StringVar()
        entry_name = Entry(root, textvariable=note_name,
                           width=15)
        entry_name.place(x=160, y=312)

        # Save Funvtion (OK)
        def save():
            adress = "c:/Users/MyHP/Notes/" + note_name.get() + ".txt"
            nots_arr = os.listdir("c:/Users/MyHP/Notes")
            if len(note_name.get()) == 0:
                win1 = Toplevel(root)
                win1.geometry("300x50")
                win1.title("error")
                Label(win1, text="invalid name !",
                      font="arial 10 bold").pack()
                Button(win1, text="Close", command=lambda: win1.destroy()).pack()
            elif (note_name.get() + ".txt") in nots_arr:
                win1 = Toplevel(root)
                win1.geometry("300x50")
                win1.title("error")
                Label(win1, text="This name already exists",
                      font="arial 10 bold").pack()
                Button(win1, text="Close", command=lambda: win1.destroy()).pack()

            else:
                text = open(adress, "x")
                text.write(text1.get("1.0", "end"))
                entry_name.delete("0", "end")
        Button(root, text="OK", command=save).place(x=256, y=310)
    Button(root, text="Creat Note", command=creat_note).place(x=0, y=95)
    # Buttons
    # Save Button
    Button(root, text="Save", command=choose_note_name).place(x=105, y=284)
    # Clear Button
    Button(root, text="Clear", command=delete_text).place(x=137, y=284)


# SHOW Function

def show_edit():

    # list notes
    nots_arr = os.listdir("c:/Users/MyHP/Notes")
    j = "Notes List"
# window to see and edit Notes
    win = Toplevel(root)
    win.title("PythonGuides")
    win.geometry("400x450")
    win['bg'] = '#fb0'
# Note Text
    txtarea = Text(win, width=40, height=20)
    txtarea.pack(pady=20)
# pathh to insert note direction
    pathh = Entry(win)
    pathh.pack(side=LEFT, expand=True, fill=X, padx=20)
# Function to open old note

    def openNote():
        global adrs
        tf = filedialog.askopenfilename(
            initialdir="C:/Users/MainFrame/Desktop/", title="Open Text file", filetypes=(("Text Files", "*.txt"),))
        adrs = tf
        pathh.insert(END, tf)
        tf = open(tf, "r")
        data = tf.read()
        txtarea.insert(END, data)

        tf.close()
# Function To save any changing in any note

    def savechanging():
        fil = open(adrs, "w")
        fil.write(txtarea.get("1.0", "end"))
    Button(win, text="Open File", command=openNote).pack(
        side=RIGHT, expand=True, fill=X, padx=20)
    Button(win, text="save changing", command=savechanging).place(x=300, y=350)


# Window
root = Tk()
root.geometry("1280x720")
root.title("Home App By idrissi.51")
root.iconbitmap('C:/Users/MyHP/icon/ab.png')
root['background'] = '#353535'
# Label
Label(root, text=Date, font="arial 10").place(x=1190, y=0)
Label(root, text=Time, font="arial 10").place(x=1090, y=0)

# Buttons
Button(root, text="Note", command=note_function).place(x=125, y=70)


# run
root.mainloop()
