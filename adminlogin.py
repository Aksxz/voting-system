import tkinter as t
from tkinter import messagebox as ms
import mysql.connector as mysql
from PIL import Image,ImageTk
from centerwindow import *

class enter:
   
    def confirm(s):
        ans=ms.askyesno(title='Exit',message='Do You Want To Exit ?')
        if ans:
            s.__w.destroy()
    
    def click2(s,event):
        if s.__e1.get()=='' or s.__e2.get()=='' :
            ms.showerror('Error','Enter UserName and password correctly ')
        else:
            con=mysql.connect(host='localhost',user='root',password='7015555218',database='Voting')
            cur=con.cursor()
            cur.execute('select * from admin where user=%s and password=%s ',(s.__e1.get(),s.__e2.get()))
            res=cur.fetchone()
            if res:
                    ms.showinfo('Success','Login Success')
                    import admin as am
                    s.__w.destroy()
                    a1=am.AdminMain()
            else:
                ms.showerror('Error','Enter username and password correctly ')


    def back(s,event):
        s.__w.destroy()
        import began as b
        asd=b.benn()
      
        
    def __init__(s):
        s.__w=t.Tk()
        
        s.__w.geometry('350x300')

        window_width=350
        window_height=300
        center_window(s.__w,window_width,window_height)

        s.__l1=t.Label(text='Login Using Your Credentials',font="bold 20",fg='orange')
        s.__l1.place(x=40,y=40)
    

        s.__adhr=t.Label(text='Username',font=('bold',16),fg='white')
        s.__password=t.Label(text='Password',font=('bold',16),fg='white')
        
        s.__adhr.place(x=40,y=100)
        s.__password.place(x=40,y=150)
        
        s.__e1=t.Entry()
        s.__e2=t.Entry(s.__w,show='*')
        s.__e1.place(x=160,y=100,width=150,height=30)
        s.__e2.place(x=160,y=150,width=150,height=30)

        s.__b1=t.Button(text='Login',font=('bold',16),bg="blue")
        s.__b1.place(x=100,y=230,width=150,height=40)
        s.__b1.bind("<Button-1>",s.click2)
        
        s.__w.protocol("WM_DELETE_WINDOW", s.confirm)

        '''
        s.__back_button = t.Button(text='⬅', fg='black', font=('Arial Bold', 14), command=s.back)
        s.__back_button.place(x=5, y=5)
        '''

        s.__path1='/Users/akshsaini/Documents/Voting/backkk.webp'
        s.__original1=Image.open(s.__path1)
        s.__resized1=s.__original1.resize((30,30))
        s.__fimage1=ImageTk.PhotoImage(s.__resized1)
        s.__label1=t.Label(s.__w,image=s.__fimage1)
        s.__label1.place(x=10,y=10)
        s.__label1.bind('<Button-1>',lambda event:s.back(event))
        
        s.__w.mainloop()

#a=enter()