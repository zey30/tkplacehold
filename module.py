from tkinter import *


def placehold(v):


    v.insert(0, v.text)
    v.configure(state=DISABLED)

    def on_click(event):
        v.configure(state=NORMAL)
        v.delete(0, END)

        # make the callback only work once
        v.unbind('<Button-1>', on_click_id)

    on_click_id = v.bind('<Button-1>', on_click)

