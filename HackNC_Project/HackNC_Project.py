"""
HackNC 2023 project
Team Members: Thomas Kung, Kevin Hayes, and Steven von Dohlen



"""

import tkinter as tk
from container import Container
import pandas as pd


def main():
    md1 = Container()
    md2 = Container()
    md3 = Container()
    md4 = Container()
    md5 = Container()
    md6 = Container()
    md7 = Container()
    md8 = Container()
    md9 = Container()

    df = pd.read_csv("HackNC_Project/Patient-Data.csv")
    print(df.head(20))
    # define the window
    root = tk.Tk()
 
    #optional
    root.configure(background='grey')
    root.geometry('600x600')
    #place any of your code lines here
    message = tk.Label(root, text="Medicine Manager")
    message.pack()

    patient_list = tk.Text(root, height=20, width=70)
    patient_list.pack()
    patient_list.insert(tk.END, df.head(20))

    def button1_clicked():
        md1.open_container()
        button1.configure(bg="green")
        print(md1.open)

    def button2_clicked():
        md2.open_container()
        button2.configure(bg="green")
        print(md2.open)

    def button3_clicked():
        md3.open_container()
        button3.configure(bg="green")
        print(md3.open)

    def button4_clicked():
        md4.open_container()
        button4.configure(bg="green")
        print(md4.open)

    def button5_clicked():
        md5.open_container()
        button5.configure(bg="green")
        print(md5.open)

    def button6_clicked():
        md6.open_container()
        button6.configure(bg="green")
        print(md6.open)

    def button7_clicked():
        md7.open_container()
        button7.configure(bg="green")
        print(md7.open)

    def button8_clicked():
        md8.open_container()
        button8.configure(bg="green")
        print(md8.open)

    def button9_clicked():
        md9.open_container()
        button9.configure(bg="green")
        print(md9.open)

    button1 = tk.Button(root, text='Patient 1', command=button1_clicked)
    button1.pack()
    button2 = tk.Button(root, text='Patient 2', command=button2_clicked)
    button2.pack()
    button3 = tk.Button(root, text='Patient 3', command=button3_clicked)
    button3.pack()
    button4 = tk.Button(root, text='Patient 4', command=button4_clicked)
    button4.pack()
    button5 = tk.Button(root, text='Patient 5', command=button5_clicked)
    button5.pack()
    button6 = tk.Button(root, text='Patient 6', command=button6_clicked)
    button6.pack()
    button7 = tk.Button(root, text='Patient 7', command=button7_clicked)
    button7.pack()
    button8 = tk.Button(root, text='Patient 8', command=button8_clicked)
    button8.pack()
    button9 = tk.Button(root, text='Patient 9', command=button9_clicked)
    button9.pack()



    #end of code
    root.mainloop()


    

if __name__=="__main__":
    main()
