"""
HackNC 2023 project
Team Members: Thomas Kung, Kevin Hayes, and Steven von Dohlen



"""

from tkinter import *
from container import Container
import pandas


def main():
    # define the window
    
 
    root = Tk()
 
    #optional
    root.configure(background='yellow')
    root.geometry('600x800')
 
    #place any of your code lines here
 
    #end of code
    root.mainloop()

    md1 = Container()
    print(md1.open)
    

if __name__=="__main__":
    main()
