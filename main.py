
#from distutils.cmd import Command
#from multiprocessing.connection import Listener
#from distutils.cmd import Command
from cmath import inf
from time import time
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
     engine.say(text)
     engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
           print('listening...')
           voice = listener.listen(source)
           Command = listener.recognize_google(voice)
           Command = Command.lower()
           if 'alexa' in Command: 
            Command = Command.replace('alexa','')
            print(Command)

    except:
        pass
    return Command

def run_alexa():
    Command = take_command()
    print(Command)
    if 'play' in Command:
        song = Command.replace('play','')
        talk('Playing'+ song)
        pywhatkit.playonyt(song)

    elif 'time' in Command:
       time = datetime.datetime.now().strftime('%I:%M %p')
       talk('Current time is' + time)

    elif 'Who the heck is' in Command:
        person = Command.replace('Who the heck is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)

    elif 'date' in Command:
        talk('Sorry, I have a Headache')
    
    elif ' Are You Single' in Command:
        talk('I am in a relationship with wifi')
 
    elif 'joke' in Command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again.')

while True:
    run_alexa()

