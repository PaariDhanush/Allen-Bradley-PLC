import sys
sys.path.append('..')

'''
Create a simple Tkinter window to display a
single variable.
Tkinter doesn't come preinstalled on all
Linux distributions, so you may need to install it.
Linux distributions, so you may need to install it.
For Ubuntu: sudo apt-get install python-tk
'''
from pylogix import PLC

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

tagName1 = 'INPUT_1'
tagName2 = 'INPUT_2'
tagName3 = 'INPUT_3'
ipAddress = '192.168.1.13'

def main():
    '''
    Create our window and comm driver
    '''
    global root
    global comm
    global ProductionCount
    global ProductionCount1
    global ProductionCount2
    
    # create a comm driver
    comm = PLC()
    comm.IPAddress = ipAddress

    # create a tkinter window
    root = Tk()
    root.config(background='blue')
    root.title = 'Production Count'
    root.geometry('1900x1900')
    
    # bind the "q" key to quit
    root.bind('q', lambda event:root.destroy())
    
    # create a labe to display our variable
    ProductionCount = Label(root, text='n', fg='white', bg='black', font='Helvetica 120 bold')
    ProductionCount.place(anchor=CENTER, relx=0.5, rely=0.3)
    
    ProductionCount1 = Label(root, text='n', fg='white', bg='red', font='Helvetica 140 bold')
    ProductionCount1.place(anchor=CENTER, relx=0.5, rely=0.6)
    
    ProductionCount2 = Label(root, text='n', fg='white', bg='red', font='Helvetica 140 bold')
    ProductionCount2.place(anchor=CENTER, relx=0.5, rely=0.9)
    
    # call our updater and show our window
    root.after(1000, UpdateValue)
    root.mainloop()
    comm.Close()

def UpdateValue():
    '''
    Call ourself to update the screen
    '''
    ProductionCount['text'] = comm.Read(tagName1).Value
    ProductionCount1['text'] = comm.Read(tagName2).Value
    ProductionCount2['text'] = comm.Read(tagName3).Value
    root.after(500, UpdateValue)

if __name__=='__main__':
    main()
