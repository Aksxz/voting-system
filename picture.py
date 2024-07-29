
import tkinter as tk 
from PIL import Image,ImageTk
from centerwindow import *

class pic():

    def page(self):

        import began as b
        self.__root.destroy()
        q=b.benn()
    
    def __init__(self):
        self.__root =tk.Tk()
        self.__root.geometry("800x800")
        self.__root.resizable(width=False,height=False)

        window_width=800
        window_height=800
        center_window(self.__root,window_width,window_height)

        self.__main_frame = tk.Frame(self.__root,bg="white")
        self.__main_frame.pack(fill=tk.BOTH,expand=True)
        self.__main_frame.columnconfigure(0,weight=1)
        self.__main_frame.rowconfigure(0,weight=1)

        self.__image_obj=ImageTk.PhotoImage(Image.open("/Users/akshsaini/Documents/Voting/vote2.jpg"))
        self.__label_img=tk.Label(self.__main_frame,image=self.__image_obj,bg="white")
        self.__label_img.grid(column=0,row=0)


        self.__root.after(4000,self.page)
        self.__root.mainloop()
 

ab=pic()





















