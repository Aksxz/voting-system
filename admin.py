import tkinter as tk
import mysql.connector as mysql
from centerwindow import *

class AdminMain:
    def __init__(self):
        self.__w = tk.Tk()
        self.__w.title("Party-wise Voter Count")

        window_width=270
        window_height=280
        center_window(self.__w,window_width,window_height)
        
        try:
            con = mysql.connect(host='localhost', user='root', password='7015555218', database='Voting')
            cur = con.cursor()
            cur.execute('SELECT party, COUNT(*) AS total FROM voters WHERE party IS NOT NULL GROUP BY party ORDER BY total DESC')
            res = cur.fetchall()
            print(res)  # For testing purposes; will print the result in the console
            
            # Display the result in Tkinter Labels using grid
            tk.Label(self.__w, text="Party").grid(row=0, column=0, padx=10, pady=5)
            tk.Label(self.__w, text="Total").grid(row=0, column=1, padx=10, pady=5)
            
            for idx, row in enumerate(res, start=1):
                party_label = tk.Label(self.__w, text=row[0])
                total_label = tk.Label(self.__w, text=row[1])
                
                party_label.grid(row=idx, column=0, padx=10, pady=5)
                total_label.grid(row=idx, column=1, padx=10, pady=5)
            
        except mysql.Error as e:
            print(f"Error: {e}")
        
        finally:
            if con.is_connected():
                cur.close()
                con.close()