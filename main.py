import os
import time 
import pyttsx3
import pyautogui as pag
import wikipedia as wiki
import googlesearch as g
import webbrowser
import openai as ai
from gtts import gTTS as g
import pygame

import speech_recognition as sr

def DTnow():
    c=time.ctime()
    c=str(c)
    c=c.split()
    t=c[3]
    h=t[:2]
    min=t[3:5]
    s='AM'
    hr=int(h)
    if hr>=12:
        s='PM'
    if hr>12:   
        hr-=12
    print(f'{hr}:{min} {s} | {c[0]}, {c[1]} {c[2]},{c[4]}')

def speak_old(ans):
    engine = pyttsx3.init() # object creation

    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    # print (rate)                        #printing current voice rate
    engine.setProperty('rate', 145)     # setting up new voice rate


    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    # print (volume)                          #printing current volume level
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. 0 for male
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

    engine.say(ans)
    engine.runAndWait()
    engine.stop()

def speak(text):
    t=g(text)
    t.save('friday.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('friday.mp3')
    pygame.mixer.music.play()
    while  pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove('friday.mp3')
    
def greet():
    a=time.ctime()
    b=int(((a).split())[3][:2])
    if b<12:
        print("Good Morning Chief!")
        speak("Good Morning Chief!")
    elif b>=12 and b<=17:
        print("Good Afternoon Chief!")
        speak("Good Afternoon Chief!")
    else: 
        print("Good Evening Chief!")
        speak("Good Evening Chief!")

def Type(x):
    for i in x:
        pag.typewrite(i)
        time.sleep(0.1)
   
def modeC():
    pag.hotkey("Win",'4')
    pag.press('Win')
    time.sleep(1)
    Type('vsc')
    time.sleep(1)
    pag.press('enter')

def ms_rewards():
    l=['We','live','in','the','age','of','the','internet.','Also,','it','has','become','an','necessity.']
    import random as r
    a=r.randint(0,len(l))
    pag.hotkey('win','6')
    time.sleep(3)
    for i in range(len(l)):
        pag.hotkey('ctrl','t')
        time.sleep(1)
        pag.typewrite(l[i])
        time.sleep(1)
        pag.press('enter')
        time.sleep(4)

def search(query):
    print(wiki.summary(query,sentences=1))
    speak(wiki.summary(query,sentences=1))
    
def processC(c):
    c=c.lower()
    if 'open google' in c:
        print(c)
        webbrowser.open('www.google.com')
    elif 'open youtube' in c:
        print(c)
        webbrowser.open('www.youtube.com')
    elif 'open typer' in c:
        print(c)
        webbrowser.open('https://monkeytype.com/')
    elif 'open github' in c:
        print(c)
        webbrowser.open('https://github.com/Adit-Kumar-7707')
    elif 'spotify' in c:
        print(c)
        os.startfile(r'C:\Users\DELL\OneDrive\Documents\Creative\Code\Python\Jarvis\shortcuts\Spotify - Shortcut.lnk')
    elif 'vs code' in c:
        print(c)
        os.startfile(r'C:\Users\DELL\OneDrive\Documents\Creative\Code\Python\Jarvis\shortcuts\Visual Studio Code - Shortcut.lnk')
    elif 'github desktop' in c:
        print(c)
        os.startfile(r'C:\Users\DELL\OneDrive\Documents\Creative\Code\Python\Jarvis\shortcuts\GitHub Desktop.lnk')
    elif 'ms rewards' in c:
        print(c)
        ms_rewards() # does random searches to increase points in you ms rewards wallet
    elif 'i love you' or 'i like you' in c:
        print(c)
        speak('abe nikal yaha se baad surat kahe ka')
    elif 'how' or 'why' or 'who' or 'what' in c:
        print(c)
        search(c)
    elif 'code mode' in c:
        modeC()
    else:
        speak('dhaang se bool na be mujhe samaj nahi aye tare bhasha') 


if __name__=="__main__": 
    DTnow()
    greet()
    speak('Initializing friday...')
    while True:
            r = sr.Recognizer() # obtain audio from the microphone
                
            print('Recognizing...')
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source,timeout=3,phrase_time_limit=1)
                    # recognize speech using Google Speech Recognition

                prompt = r.recognize_google(audio)
                # print(prompt)
                if prompt.lower()=='friday':
                    speak("At your service Chief!")
                    print("A.I. Active!")
                    with sr.Microphone() as source:
                        print("Listening...")
                        audio = r.listen(source,timeout=2)
                        prompt = r.recognize_google(audio)
                        processC(prompt)

            except Exception as e:
                print("Error; {0}".format(e))

input()
