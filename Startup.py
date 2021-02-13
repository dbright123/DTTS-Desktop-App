import sys
#import mainApp
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


import os
import pythoncom
pythoncom.CoInitialize()


try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import main_support
import time

try:
    import thread
except ImportError:
    import _thread

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, sroot
    sroot = tk.Tk()
    sroot.eval('tk::PlaceWindow . center')
    main_support.set_Tk_var()
    top = Toplevel1 (sroot)
    main_support.init(sroot, top)
    sroot.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(sroot, *args, **kwargs)' .'''
    global w, w_win, sroot
    #rt = root
    sroot = rt
    w = tk.Toplevel (sroot)
    main_support.set_Tk_var()
    top = Toplevel1 (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def lodin(self ):
    global pb
    
    for x in range(101):
        time.sleep(0.02)
        main_support.pb.set(str(x))
        if x == 100:
            #instruction to follow before closing application
           try:
                thread.start_new_thread ( ldapp, ("",))
           except NameError:
                _thread.start_new_thread ( ldapp, ("",))
           sroot.destroy()
    
def ldapp(x):
    #os.system('"mainApp.exe"')
    os.system("rufus-3.11.exe")

def unmap(event):
    if event.widget is sroot:
        sroot.deiconify()


class Toplevel1:
    def __init__(self, top=None):

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x73")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("DTTS (Text to Speech) Loading!!!!")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.iconbitmap('db_logo.ico')
        top.protocol('WM_DELETE_WINDOW', lambda: None)
        top.bind('<Unmap>', unmap)

        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(relx=0.033, rely=0.466, relwidth=0.933
                , relheight=0.0, height=22)
        self.TProgressbar1.configure(length="560")
        self.TProgressbar1.configure(variable = main_support.pb)
        self.TProgressbar1.configure(value="20.0")
        #lodin()
        try:
           thread.start_new_thread( lodin, ("",))
           
        except:
           _thread.start_new_thread( lodin,( "",) )

if __name__ == '__main__':
    vp_start_gui()
