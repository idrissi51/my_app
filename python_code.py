# My App

# import Modules
from tkinter import *
from tkinter import ttk
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
    win = Toplevel(root)
    win.geometry("400x100")
    win.title('Notes Lsit')

    # Creat A Main Frame
    main_frame = Frame(win)
    main_frame.pack(fill=BOTH, expand=1)
    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    # Add A Scrollbar To the Canvas
    my_scrollbar = ttk.Scrollbar(
        main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    # Configure Thes Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox("all")))
    # Create ANOTER Frame INSIDE the canvas
    second_frame = Frame(my_canvas)
    # Add tha new frame to a window in the canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    x = 0
    for i in nots_arr:
        Button(second_frame, text=i, font="arial 10 bold").grid(
            row=x, column=0, pady=2, padx=2)
        x += 1


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
