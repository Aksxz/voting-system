
import tkinter as a
from tkinter import ttk
from tkinter import messagebox as ms
import mysql.connector as mc
from PIL import Image,ImageTk
from centerwindow import *

class regg:
    def regis(s,event):
        if s.__che.get()=="" or s.__vas.get()=="" or s.__g.get()=="" or s.__h.get()=="" or s.__ac.get()=="" or s.__ca.get()=="" : 
            ms.showerror("ERROR","Please try again")

        elif len(s.__g.get())<6:
            ms.showerror('Error','Password is weak')
            s.__g.delete(0,a.END)
            s.__g.delete(0,a.END)

        elif s.__g.get()!=s.__h.get():
            s.__g.delete(0,a.END)
            s.__h.delete(0,a.END)
            ms.showerror('Error','Password does not match')

        elif len(s.__ca.get())<=9 or len(s.__ca.get())>=11:
            ms.showerror('Error','Check Your Number' )

        elif len(s.__ca.get())==12:
            ms.showerror('Error','Check Your Adhar No.' )

        else :
            con=mc.connect(host="localhost",user="root",password="7015555218",database="voting") 
            cur=con.cursor() 
            cur.execute("insert into voters (First_name,last_name,password,adhar_no,phone_no)values(%s,%s,%s,%s,%s)",(s.__che.get(),s.__vas.get(),s.__g.get(),s.__ac.get(),s.__ca.get()))
            con.commit()
            ms.showinfo("SUCCESS","Sign up succesfully")
            s.__b.destroy()
            import login as l
            m=l.login()

    def back(s,event):
        s.__b.destroy()
        import login as b
        asd=b.login()


    def __init__(s):
        s.__b=a.Tk()

        s.__b.geometry('500x500')

        s.__b.title("VOTING")

        window_width=500
        window_height=500
        center_window(s.__b,window_width,window_height)


        s.__mans=a.Label(text='CREATE AN ACCOUNT',fg='orange',font=('Arial Bold',20))
        s.__daks=a.Label(text='First name',fg='white',font=("yu gothic ui",13,"bold"))
        s.__aks=a.Label(text='Last name',fg='white')
        s.__bans=a.Label(text='Password',fg='white')
        s.__tans=a.Label(text='Confirm password',fg='white')
        s.__hans=a.Label(text='Gender',fg='white')
        s.__vans=a.Label(text='City',fg='white')
        s.__chans=a.Label(text="Adhar number",fg="white")
        s.__ans=a.Label(text="Phone number (+91)",fg="white")


        s.__mans.place(x=130,y=10)
        s.__daks.place(x=60,y=90)
        s.__aks.place(x=60,y=130)
        s.__bans.place(x=60,y=170)
        s.__tans.place(x=60,y=210)
        s.__hans.place(x=60,y=250)
        s.__vans.place(x=60,y=290)
        s.__chans.place(x=60,y=330)
        s.__ans.place(x=60,y=370)


        s.__che=a.Entry(bg='white',fg='black')
        s.__vas=a.Entry(bg='white',fg='black')
        s.__g=a.Entry(s.__b,bg='white',fg='black',show="*") 
        s.__h=a.Entry(s.__b,bg='white',fg='black',show="*")
        s.__ac=a.Entry(bg='white',fg='black')
        s.__ca=a.Entry(bg='white',fg='black')


        s.__che.place(x=240,y=90)
        s.__vas.place(x=240,y=130)
        s.__g.place(x=240,y=170)
        s.__h.place(x=240,y=210)
        s.__ac.place(x=240,y=330)
        s.__ca.place(x=240,y=370)



        s.__z=a.Radiobutton(text='Male')
        s.__y=a.Radiobutton(text='Female')
        s.__z.place(x=250,y=250)
        s.__y.place(x=340,y=250)


        s.__but=a.Button(text='Sign up',fg='blue',font=('Arial Bold',16))
        s.__but.bind("<Button-1>",s.regis)
        s.__but.place(x=180,y=450,width=150,height=40)


        s.__selected_options=a.StringVar(s.__b)
        s.__choices=['Select an option','panipat','guragoan','karnal','chatisgarh','sonipat','faridabad','ghaziabad','ambala','kurukshetra']
        s.__t=ttk.OptionMenu(s.__b,s.__selected_options,*s.__choices)
        s.__t.place(x=240,y=290,width=190)

        '''
        s.__back_button = a.Button(text='⬅', fg='black', font=('Arial Bold', 14), command=s.back)
        s.__back_button.place(x=10, y=10)
        '''

        s.__path1='/Users/akshsaini/Documents/Voting/backkk.webp'
        s.__original1=Image.open(s.__path1)
        s.__resized1=s.__original1.resize((30,30))
        s.__fimage1=ImageTk.PhotoImage(s.__resized1)
        s.__label1=a.Label(s.__b,image=s.__fimage1)
        s.__label1.place(x=10,y=10)
        s.__label1.bind('<Button-1>',lambda event:s.back(event))

        s.__b.mainloop()

#qw=regg()










