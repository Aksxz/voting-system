import tkinter as tk
from tkinter import messagebox as ms
from centerwindow import *

class benn():

    def confirm(s):
        response = ms.askyesno("Confirm Close", "Are you sure you want to close the window?")
        if response:
            s.__win.destroy()

    def che(s,event):

        ms.showinfo("THNAK YOU","Directing to next page")
        import login as l
        s.__win.destroy()
        abcd=l.login()

    def vas(s,event):
        ms.showinfo("SUCCESS","PLEASE WAIT")
        import adminlogin as al
        s.__win.destroy()
        abcd=al.enter()


    def __init__(s):

        s.__win=tk.Tk()

        s.__win.title("VOTING")

        s.__win.geometry("300x300")

        window_width=300
        window_height=300
        center_window(s.__win,window_width,window_height)

        s.__a=tk.Label(text="SELECT YOUR CATEGORY")

        s.__but1=tk.Button(text="VOTER",fg="blue")
        s.__but1.bind("<Button-1>",s.che)
        s.__but1.place(x=110,y=70,height=40,width=80)

        s.__but2=tk.Button(text="ADMIN",fg="blue")
        s.__but2.bind("<Button-1>",s.vas)
        s.__but2.place(x=110,y=170,height=40,width=80)

        s.__win.protocol("WM_DELETE_WINDOW", s.confirm)

        s.__win.mainloop()

#abc=benn()