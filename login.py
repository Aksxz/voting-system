
import tkinter as t
from tkinter import messagebox as ms
import mysql.connector as mysql
from PIL import Image,ImageTk
from centerwindow import *

class login:

    def daks(s,event):
        ms.showinfo("SUCCESS","PLEASE WAIT")
        import regist as g
        s.__win.destroy()
        qw=g.regg()

    def aks(s,event):
        aid=s.__che.get()
        if s.__che.get()=="" or s.__g.get()=="" :
            ms.showerror("ERROR","Please try again")

        else:
            con=mysql.connect(host='localhost',user='root',password='7015555218',database='Voting')
            cur=con.cursor()
            cur.execute('select * from voters where adhar_no=%s and password=%s',(s.__che.get(),s.__g.get()))
            p=cur.fetchone()
            if p is not None:
                if p[5]==0 :
                    ms.showinfo('Success','Login Success')
                    import votingsys as v
                    s.__win.destroy()
                    ab=v.VotingSystem(aid)
                else:
                    ms.showerror("ERROR","This user has alredy voted")
            else:
                ms.showerror("ERROR","Invalid credentials")


    def back(s,event):
        s.__win.destroy()
        import began as b
        asd=b.benn()
        

    def __init__(s):

        s.__win=t.Tk()
        s.__win.geometry("500x300")

        s.__win.title("VOTING")

        window_width=500
        window_height=300
        center_window(s.__win,window_width,window_height)


        s.__mans=t.Label(text='LOGING IN',fg='orange',font=('Arial Bold',20))
        s.__mans.place(x=180,y=30)


        s.__daks=t.Label(text='Adhaar ID',fg='white',font=("yu gothic ui",16,"bold"))
        s.__daks.place(x=70,y=110)

        s.__che=t.Entry(bg='white',fg='black')
        s.__che.place(x=240,y=110)

        s.__bans=t.Label(text='Password',fg='white',font=("yu gothic ui",16,"bold"))
        s.__bans.place(x=70,y=150)

        s.__g=t.Entry(s.__win,bg='white',fg='black',show="*")
        s.__g.place(x=240,y=150)

        s.__but=t.Button(text='Login',fg='blue',font=('Arial Bold',18))
        s.__but.place(x=200,y=220)
        s.__but.bind("<Button-1>",s.aks)
        
        s.__p=t.Label(text="Don't have account ?",font=(12))
        s.__p.place(x=140,y=250)

        s.__butt=t.Button(text='Sign up',fg='blue',font=('Arial Bold',14))
        s.__butt.place(x=270,y=250,height=20,width=60)
        s.__butt.bind("<Button-1>",s.daks)

        '''
        s.__back_button = t.Button(text='⬅', fg='black', font=('Arial Bold', 14), command=s.back)
        s.__back_button.place(x=10, y=10)
        '''
        
        s.__path1='/Users/akshsaini/Documents/Voting/backkk.webp'
        s.__original1=Image.open(s.__path1)
        s.__resized1=s.__original1.resize((30,30))
        s.__fimage1=ImageTk.PhotoImage(s.__resized1)
        s.__label1=t.Label(s.__win,image=s.__fimage1)
        s.__label1.place(x=10,y=10)
        s.__label1.bind('<Button-1>',lambda event:s.back(event))

        s.__win.mainloop()


#abc=login()



