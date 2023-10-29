"""
HackNC 2023 project
Team Members: Thomas Kung, Kevin Hayes, and Steven von Dohlen

Basic Operation:
This code can operate a medicine dispensing station that may be a fixed device or a rolling cart.
The hospital pharmacy will fill the containers with the right medicine for the right patient for the time frame being covered (day/shift/etc.)
This station will be initialized by loading data from a .csv file that will set the contents of each medicine container. (this would be generated
   by the patient management system of the hospital)
The tk.Text widget "patient_list" will display the list of patients to receive the medicine and the times that they should be dosed. (patients will be listed by dosing time)
When the current time is equal to the dosing time, the patient will be added to the list.
The opening of the specified container to dose the patient will be simulated by clicking on the indicated container (it will turn green to indicate that it has been emptied)
    (In real life this would be sensed by a switch on the container door).  Patient line in list will turn green to indicate completion.
If the patient is more than 10 minutes late for their medicine, their line of text will turn red to indicate that they are overdue.
If more than an hour late, a message will be texted to the nurses phone (simulated by a dummy function)
Once all medicines have been dispensed, the device is returned to the pharmacy for resetting/reloading for the next shift/day



"""

import tkinter as tk
from container import Container
import pandas as pd
from datetime import datetime
SIZE = 9 #Determines the number of patiants

def main():
    md = [Container() for i in range(SIZE)]

    df = pd.read_csv("HackNC_Project/Patient-Data.csv")
    #print(df.head(20))

    d = {}

    array = df.to_numpy()
    for x in range(len(array)):
        current_time = array[x][3]
        datetime_object = datetime.strptime(current_time, '%m/%d/%y %H:%M:%S')
        d[md[x]] = Container(array[x][1], datetime_object)

    #patient_list.delete("1.0", tk.END)
    #patient_list.insert(tk.END, array[0][0] + "\t")
    #patient_list.insert(tk.END, array[0][1] + "\t")
    #patient_list.insert(tk.END, str(array[0][2]) + "\t")
    #patient_list.insert(tk.END, str(array[0][3]) + "\t")
    #patient_list.insert(tk.END, str(d["md0"].med_late()))
    
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

    def button_clicked(num : int, md = md):
        if not md[num].is_open():
            md[num].open_container()
            buttons[num].configure(bg="green")
        else:
            md[num].close_container()
            buttons[num].configure(bg="#f0f0f0")
        print(md[num].open)
    '''
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
    '''
    buttons = [None] * SIZE
    def create_button(num):
        buttons[num] = tk.Button(root, text = "Patient %i"%num, command = lambda: button_clicked(num, md))
        buttons[num].pack()
    
    for i in range(SIZE):
        create_button(i)
    '''
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
    '''


    #end of code
    root.mainloop()


    

if __name__=="__main__":
    main()
