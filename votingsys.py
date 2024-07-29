# Python program to create a voting system using Tkinter

import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image,ImageTk
import mysql.connector as mysql
from centerwindow import *

class VotingSystem:

    def confirm(s):
        response = ms.askyesno("Confirm Close", "Are you sure you want to close the window?")
        if response:
            s.__b.destroy()

    def akss(s,event,party):
        con=mysql.connect(host="localhost",user="root",password="7015555218",database="voting")
        cur=con.cursor()
        cur.execute("Update voters set status=1,party=%s where adhar_no=%s",(party,s.__aid))
        con.commit()
        con.close
        ms.showinfo("SUCCESS","YOUR VOTE HAS BEEN SUCCESSFULLY CAST")
        s.__b.destroy()
        import startingpg as s
        s1=s.benn()

    def __init__(s,aid):
        
        s.__b=tk.Tk()

        s.__b.geometry('500x550')

        s.__b.title("VOTING")

        window_width=500
        window_height=500
        center_window(s.__b,window_width,window_height)

        s.__aid=aid

        s.__w=tk.Label(text="VOTE FOR INDIA",fg="orange",font=('Arial Bold',20))
        s.__w.place(x=170,y=50)

        s.__but1=tk.Button(fg="white")
        s.__but1.place(x=300,y=120)

        s.__but2=tk.Button(fg="white")
        s.__but2.place(x=300,y=190)

        s.__but3=tk.Button(fg="white")
        s.__but3.place(x=300,y=260)

        s.__but4=tk.Button(fg="white")
        s.__but4.place(x=300,y=330)

        s.__but5=tk.Button(fg="white")
        s.__but5.place(x=300,y=400)

        s.__but=tk.Button(text="SUBMIT",bg="blue")
        s.__but.bind("<Button-1>",s.akss)
        s.__but.place(x=200,y=500,height=30,width=100)

        s.__b.protocol("WM_DELETE_WINDOW", s.confirm)



        image_path1="/Users/akshsaini/Documents/Voting/bjp.jpg"
        original1=Image.open(image_path1)
        resized1=original1.resize((50,45))  
        final_image1=ImageTk.PhotoImage(resized1)
        s.__label = tk.Label(s.__b,image=final_image1)
        s.__label.place(x=200,y=120)


        image_path2="/Users/akshsaini/Documents/Voting/AAP.jpeg"
        original2=Image.open(image_path2)
        resized2=original2.resize((50,45))  
        final_image2=ImageTk.PhotoImage(resized2)
        s.__label = tk.Label(s.__b,image=final_image2)
        s.__label.place(x=200,y=190)

        
        image_path3="/Users/akshsaini/Documents/Voting/congress.png"
        original3=Image.open(image_path3)
        resized3=original3.resize((50,45))  
        final_image3=ImageTk.PhotoImage(resized3)
        s.__label = tk.Label(s.__b,image=final_image3)
        s.__label.place(x=200,y=260)


        image_path4="/Users/akshsaini/Documents/Voting/elep.jpg"
        original4=Image.open(image_path4)
        resized4=original4.resize((50,45))  
        final_image4=ImageTk.PhotoImage(resized4)
        s.__label = tk.Label(s.__b,image=final_image4)
        s.__label.place(x=200,y=330)


        image_path5="/Users/akshsaini/Documents/Voting/samajwadi.png"
        original5=Image.open(image_path5)
        resized5=original5.resize((50,45))  
        final_image5=ImageTk.PhotoImage(resized5)
        s.__label = tk.Label(s.__b,image=final_image5)
        s.__label.place(x=200,y=400)


        s.__but1.bind('<Button-1>',lambda event,party='bjp':s.akss (event,party))
        s.__but2.bind('<Button-1>',lambda event,party='AAP':s.akss (event,party))
        s.__but3.bind('<Button-1>',lambda event,party='congress':s.akss (event,party))
        s.__but4.bind('<Button-1>',lambda event,party='elep':s.akss (event,party))
        s.__but5.bind('<Button-1>',lambda event,party='samajvadi':s.akss (event,party))


        s.__b.mainloop()

#abc=VotingSystem()