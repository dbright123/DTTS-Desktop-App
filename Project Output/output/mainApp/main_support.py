
import sys
import os
#import text as dt

from speak import say
from test_to_mp3 import dconv
from pathlib import Path

global sText

import pythoncom
pythoncom.CoInitialize()


stop_process = True

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import thread
except ImportError:
    import _thread

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global pb
    pb = tk.StringVar()
    global dcounter
    dcounter = tk.StringVar()

    dcounter.set('1 word')
    global sText
   

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def dconvert():
    print('main_support.dconvert')
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
   
    print(sText)
    dText = str(sText)
    dconv(dText)
    dcounter.set("Done saving")
    
    sys.stdout.flush()


def Dproc(x):
    print("Loading !!!!")
    dcounter.set("Processing the image")
    #while(stop_process):
     ##  dcounter.set("Processing the image")
    #    if(stop_process == False):
     #       break;


def extractImg(dText):
    dText = dText.replace("\n"," ")
    dcount = dText.split(" ")

    print(dcount)
    stop_process = False
    c = 0
    for ct in dcount:
        if ct == " " or ct == "":
            pass
        else:
            c = c + 1
    print(c)

    if c == 1:
        dcounter.set("1 word")
    elif c > 1 :
        dcounter.set(str(c) + " words done extracting")
        #print("Itz working")
    else:
        dcounter.set("0 word done extracting")
    #dcounter.set(" Done extracting ")

def dread():
    print('main_support.dread')
    print(sText)
    dText = str(sText)
   
    
    dText = dText.replace("\n"," ")
    dcount = dText.split(" ")

    print(dcount)
    
    c = 0
    for ct in dcount:
        if ct == " " or ct == "":
            pass
        else:
            c = c + 1
    print(c)
    if c == 1:
        dcounter.set("1 word")
    elif c > 1 :
        dcounter.set(str(c) + " words")
        print("Itz working")
    else:
        dcounter.set("0 word")

    
    try:
        thread.start_new_thread ( say, (dText,))
    except NameError:
        _thread.start_new_thread ( say, (dText,))
        
    #say(dText)
    

    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import mainApp
    mainApp.vp_start_gui()




