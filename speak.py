import main_support
#x = main_support.dText
import pyttsx3


import pythoncom
pythoncom.CoInitialize()
#import cherrypy

def onThreadStart(threadIndex):
  #pythoncom.CoInitialize()
  pass
#cherrypy.engine.subscribe('start_thread', onThreadStart)

def say(x):
    pythoncom.CoInitialize()
    engine = pyttsx3.init()
    if(engine.isBusy()):
        engine.stop()
    
    engine.setProperty('rate', 130)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')       
    #engine.setProperty('voice', voices[0].id)  
    engine.setProperty('voice', voices[1].id)  
    engine.say(x)
    #engine.save_to_file(x, 'test.mp3')
    #dseconds()
    #engine.say("You can queue up multiple items")
    engine.runAndWait()
    
    
        
        

def dseconds():
    engine = pyttsx3.init()
    # future application will be edited for timing 
    pass

#say("Hello how are you")