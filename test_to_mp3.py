import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


from comtypes.client import CreateObject


engine = CreateObject("SAPI.SpVoice")
stream = CreateObject("SAPI.SpFileStream")
from comtypes.gen import SpeechLib

def dconv(x):
    
    outfile = desktop + "\\DTTS read.wav"
    stream.Open(outfile, SpeechLib.SSFMCreateForWrite)

    engine.AudioOutputStream = stream
    
    engine.speak(x)
    stream.Close()

    print(outfile)
    
#print(desktop)
#dconv("I am testing it")
#dconv("How is your day going")