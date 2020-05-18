import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wolframalpha
import os
import sys
import time as t
from playsound import playsound

converter = pyttsx3.init() #'dummy') 
converter.setProperty('rate', 150) 
converter.setProperty('volume', 1) 
converter.say("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15") 
converter.runAndWait()

voices = converter.getProperty('voices')
for voice in voices:
    print("^^Voice:")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    converter.say("Hello")
    converter.runAndWait()

voice_id = "C:\\Program Files (x86)\\Common Files\\Microsoft Shared\\Speech\\Tokens\\TTS_MS_en-IN_Heera_11.0\\HeeraT"
#voices = converter.getProperty('voices')
#converter.setProperty('voice',voices[0].id)
converter.setProperty(voice,voice_id)
print("^^Voice:")
print("ID: %s" %voice.id)
print("Name: %s" %voice.name)
converter.say("out of the loop")
converter.runAndWait()
