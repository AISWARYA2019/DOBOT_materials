import PySimpleGUI as sg
import pyttsx3
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
from datetime import date
import wolframalpha
import os
import sys
import time as t
from playsound import playsound
import threading
import cv2
import numpy as np
import imutils
import DobotDllType as dType

# initialize the voice
engine = pyttsx3.init()#'dummy')#'sapi5')
client = wolframalpha.Client('89K64G-LQ9AGWR8GU')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)#len(voices)-1].id)
engine.setProperty('rate',135)

# window layout
sg.theme('Dark Blue')
cus_size = (1800,800)
atext = "I am a Robot"
utext = "I am a human"
lay1 = [[sg.Text(' ROHiNi ',font='Space\ Ranger\ Semi\-Italic 35',size=(6,1),text_color='white',background_color='darkblue'), sg.Text(atext,font='Arial 20',size=(30,2),text_color='black',background_color='white',key='adisp')],
        [sg.Text(' USER  ',font='Space\ Ranger\ Semi\-Italic 35',size=(6,1),text_color='black',background_color='lightblue'), sg.Text(utext,font='Arial 20',size=(30,2),text_color='black',background_color='white',key='udisp')],
        [sg.Text('Please type here',),sg.InputText(), sg.Button(' ENTER ',button_color=('white','black'),size=(5,1))],
        [sg.Text(' ',size = (2,1))],
        [sg.Text('I can tell you the time',font='Nasalization\ Rg 20',size=(10,2),text_color='white',background_color='black'), sg.Text('I can print you a text',font='Nasalization\ Rg 20',size=(10,2),text_color='white',background_color='black'), sg.Text('I can give you a candy',font='Nasalization\ Rg 20',size=(10,2),text_color='white',background_color='black'), sg.Text('I can dance',font='Nasalization\ Rg 20',size=(7,2),text_color='white',background_color='black')]]

win = sg.Window('ROHINI HMI (Trial #5)',size=cus_size).Layout(lay1)
win.finalize()

# speak
def speak(audio):
    win['adisp'].update(audio)
    t.sleep(2)
    print('Robot ROHINI: ' + audio)
    engine.say(audio)
    engine.runAndWait()

# greet
def greetMe():
    t.sleep(4)
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        atext = 'Good Morning!'
    elif currentH >= 12 and currentH < 18:
        atext = 'Good Afternoon!'
    else:
        atext = 'Good Evening!'
    speak(atext)

# get user's command    
def myCommand():
    tic=t.time()
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        win['adisp'].update('Listening...')
        t.sleep(0.5)
        r.pause_threshold =  1
        audio = r.listen(source)
    toc=t.time()
    s_elapse = toc - tic
    try:
        query = r.recognize_google(audio, language='en-in')
        print('Human:  ' + query + '\n')
        win['udisp'].update(query)
    except sr.UnknownValueError or s_elapse>10:
        win['adisp'].update('Sorry! I didn\'t get that! Try typing the command!')
        t.sleep(0.5)
        speak('Sorry! I didn\'t get that! Try typing the command!')
        event, values = win.read()
        query = values[0]
        #query = str(input('Command: '))
        win['udisp'].update(query)
    return query










###############################  BLUE
def blue(): ## Time
	
	cap = cv2.VideoCapture(0)

	#Setting resolution
	cap.set(3,640)
	cap.set(4,480)
	win['adisp'].update('(Entered blue function)')


	print('Entered blue function')
	while True:

		_,frame = cap.read()
		hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)

		ret, frame = cap.read()  # capture the image

		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert BGR to HSV

		lower_blue = np.array([90, 60, 120])
		upper_blue = np.array([121, 255, 255])

		mask1 = cv2.inRange(hsv_frame, lower_blue, upper_blue)  # mask for blue

		cnts1 = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		cnts1 = imutils.grab_contours(cnts1)

		for c in cnts1:
			area1 = cv2.contourArea(c)
			if area1 > 2000:
				cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
				M = cv2.moments(c)
				cx_1 = int(M["m10"] / M["m00"])
				cy_1 = int(M["m01"] / M["m00"])
				cv2.circle(frame,(cx_1,cy_1),7,(255,0,0),-1)
				cv2.putText(frame,"Orbit Blue", (cx_1-20, cy_1-20), cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),2)
					
				cam_cord = [cx_1, cy_1]

						#print(coordinates)
				dobot_cord_x = 0.5426*cam_cord[0]+146.98 
				dobot_cord_y = -0.6249*cam_cord[1]+208.54
				dobot_cord = (dobot_cord_x, dobot_cord_y)
						# print(cam_cord[2])
				with open('coordinates_voice.txt', 'w') as file:
					for listitem in dobot_cord:
						file.write('%d\n' % listitem)
				win['adisp'].update('Located blue orbit coordinates')
				print('Located blue orbit coordinates')
				win['adisp'].update('Orbit Blue is my favorite candy too, so save some for me!')
				t.sleep(0.5)
				speak('Orbit Blue is my favorite candy too, so save some for me!')
				os.system (r"python C:\Users\user7\Downloads\DobotDemoV2.0\DobotDemoV2.0\DobotDemoForPython\cam_dobot_exec_voice.py")
				break
		break
		cv2.imshow("frame", frame)

##################################  YELLOW
def yellow(): 
	
	cap = cv2.VideoCapture(0)

	#Setting resolution
	cap.set(3,640)
	cap.set(4,480)
	win['adisp'].update('Entered yellow function')
	print('Entered yellow function')
	while True:

		_,frame = cap.read()
		hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)

		ret, frame = cap.read()  # capture the image

		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert BGR to HSV

		lower_yellow = np.array([25, 45, 120])
		upper_yellow = np.array([40, 255, 255])

		mask2 =cv2.inRange(hsv_frame, lower_yellow, upper_yellow) #mask for yellow

		cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		cnts2 = imutils.grab_contours(cnts2)


		for c in cnts2:
			area2 = cv2.contourArea(c)
			if area2 > 2000:
				cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
				M = cv2.moments(c)
				cx_2 = int(M["m10"] / M["m00"])
				cy_2 = int(M["m01"] / M["m00"])
				cv2.circle(frame,(cx_2,cy_2),7,(255,0,0),-1)
				cv2.putText(frame,"Orbit yellow", (cx_2-20, cy_2-20), cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),2)
					
				cam_cord = [cx_2, cy_2]

						#print(coordinates)
				dobot_cord_x = 0.5426*cam_cord[0]+146.98 
				dobot_cord_y = -0.6249*cam_cord[1]+208.54
				dobot_cord = (dobot_cord_x, dobot_cord_y)
						# print(cam_cord[2])
				with open('coordinates_voice.txt', 'w') as file:
					for listitem in dobot_cord:
						file.write('%d\n' % listitem)
				win['adisp'].update('Located yellow orbit coordinates')
				print('Located yellow orbit coordinates')
				win['adisp'].update('I dont like the Orbit yellow very much, so you can have it all')
				t.sleep(0.5)
				speak('I dont like the Orbit yellow very much, so you can have it all')
				os.system (r"python C:\Users\user7\Downloads\DobotDemoV2.0\DobotDemoV2.0\DobotDemoForPython\cam_dobot_exec_voice.py")
				break
		break
		cv2.imshow("frame", frame)


##############################################################RED
def red(): 
	
	cap = cv2.VideoCapture(0)

	#Setting resolution
	cap.set(3,640)
	cap.set(4,480)
	win['adisp'].update('Entered red function')
	print('Entered red function')
	while True:

		_,frame = cap.read()
		hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)

		ret, frame = cap.read()  # capture the image

		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert BGR to HSV

		lower_red = np.array([0, 50, 120])
		upper_red = np.array([10, 255, 255])

	
	
		mask3 = cv2.inRange(hsv_frame, lower_red, upper_red)

		cnts3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		cnts3 = imutils.grab_contours(cnts3)


		for c in cnts3:
			area2 = cv2.contourArea(c)
			if area2 > 2000:
				cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
				M = cv2.moments(c)
				cx_2 = int(M["m10"] / M["m00"])
				cy_2 = int(M["m01"] / M["m00"])
				cv2.circle(frame,(cx_2,cy_2),7,(255,0,0),-1)
				cv2.putText(frame,"Red candy", (cx_2-20, cy_2-20), cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),2)
					
				cam_cord = [cx_2, cy_2]

						#print(coordinates)
				dobot_cord_x = 0.5426*cam_cord[0]+146.98 
				dobot_cord_y = -0.6249*cam_cord[1]+208.54
				dobot_cord = (dobot_cord_x, dobot_cord_y)
						# print(cam_cord[2])
				with open('coordinates_voice.txt', 'w') as file:
					for listitem in dobot_cord:
						file.write('%d\n' % listitem)
				win['adisp'].update('Located coordinates')
				print('Located coordinates')
				win['adisp'].update('Interesting choice, here you go!')
				t.sleep(0.5)
				speak('Interesting choice, here you go!')
				os.system (r"python C:\Users\user7\Downloads\DobotDemoV2.0\DobotDemoV2.0\DobotDemoForPython\cam_dobot_exec_voice.py")
				break
		break
		cv2.imshow("frame", frame)

####################################BROWN
def brown(): 
	
	cap = cv2.VideoCapture(0)

	#Setting resolution
	cap.set(3,640)
	cap.set(4,480)
	win['adisp'].update('Entered brown function')
	print('Entered brown function')
	while True:

		_,frame = cap.read()
		hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)

		ret, frame = cap.read()  # capture the image

		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert BGR to HSV

		lower_dark_brown = np.array([0,0,0])
		upper_dark_brown = np.array([53, 181,89])

	
	
		mask4 = cv2.inRange(hsv_frame, lower_dark_brown, upper_dark_brown)

		cnts4 = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		cnts4 = imutils.grab_contours(cnts4)


		for c in cnts4:
			area4 = cv2.contourArea(c)
			if area4> 2000:
				cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
				M = cv2.moments(c)
				cx_4 = int(M["m10"] / M["m00"])
				cy_4 = int(M["m01"] / M["m00"])
				cv2.circle(frame,(cx_4,cy_4),7,(255,0,0),-1)
				cv2.putText(frame,"Dark Fantasy", (cx_4-20, cy_4-20), cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),2)
					
				cam_cord = [cx_4, cy_4]

						#print(coordinates)
				dobot_cord_x = 0.5426*cam_cord[0]+146.98 
				dobot_cord_y = -0.6249*cam_cord[1]+208.54
				dobot_cord = (dobot_cord_x, dobot_cord_y)
						# print(cam_cord[2])
				with open('coordinates_voice.txt', 'w') as file:
					for listitem in dobot_cord:
						file.write('%d\n' % listitem)
				win['adisp'].update('Located Dark Fantasy coordinates')
				print('Located Dark Fantasy coordinates')
				win['adisp'].update('Yummy, great choice! I love chocolate filled biscuits, enjoy!')
				t.sleep(0.5)
				speak('Yummy, great choice! I love chocolate filled biscuits, enjoy!')
				os.system (r"python C:\Users\user7\Downloads\DobotDemoV2.0\DobotDemoV2.0\DobotDemoForPython\cam_dobot_exec_voice.py")
				break
		break
		cv2.imshow("frame", frame)

########################################PURPLE
def purple(): 
	
	cap = cv2.VideoCapture(0)

	#Setting resolution
	cap.set(3,640)
	cap.set(4,480)
	win['adisp'].update('Entered purple function')
	print('Entered purple function')
	while True:

		_,frame = cap.read()
		hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)

		ret, frame = cap.read()  # capture the image

		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert BGR to HSV

		lower_purple = np.array([159, 113, 193])
		upper_purple = np.array([180, 255, 255])
	
	
		mask5 = cv2.inRange(hsv_frame, lower_purple, upper_purple)

		cnts5 = cv2.findContours(mask5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		cnts5 = imutils.grab_contours(cnts5)


		for c in cnts5:
			area5 = cv2.contourArea(c)
			if area5> 1500:
				cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
				M = cv2.moments(c)
				cx_5 = int(M["m10"] / M["m00"])
				cy_5 = int(M["m01"] / M["m00"])
				cv2.circle(frame,(cx_5,cy_5),7,(255,0,0),-1)
				cv2.putText(frame,"Boomer", (cx_5-20, cy_5-20), cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),2)
					
				cam_cord = [cx_5, cy_5]

						#print(coordinates)
				dobot_cord_x = 0.5426*cam_cord[0]+146.98 
				dobot_cord_y = -0.6249*cam_cord[1]+208.54
				dobot_cord = (dobot_cord_x, dobot_cord_y)
						# print(cam_cord[2])
				with open('coordinates_voice.txt', 'w') as file:
					for listitem in dobot_cord:
						file.write('%d\n' % listitem)
				win['adisp'].update('Located Boomer coordinates')
				print('Located Boomer coordinates')
				win['adisp'].update('Enjoy your Boomer')
				t.sleep(0.5)
                                #t.sleep(0.5)
				speak('Enjoy your Boomer')
				os.system (r"python C:\Users\user7\Downloads\DobotDemoV2.0\DobotDemoV2.0\DobotDemoForPython\cam_dobot_exec_voice.py")
				break
		break
		cv2.imshow("frame", frame)

################################PICK UP A CANDY
def pickupacandy():
    win['adisp'].update('What is the colour of your favorite candy?')
    t.sleep(0.5)
    speak('What is the colour of your favorite candy?')

    with sr.Microphone() as source:                                                                       
        print("Listening...")
        win['adisp'].update('Listening...')
        t.sleep(0.5)
        r.pause_threshold =  1
        audio = r.listen(source)
    toc=t.time()
    s_elapse = toc - tic
    try:
        query = r.recognize_google(audio, language='en-in')
        print('Human:  ' + query + '\n')
        win['udisp'].update(query)
    except sr.UnknownValueError or s_elapse>10:
        win['adisp'].update('Sorry! I didn\'t get that! Try typing the command!')
        t.sleep(0.5)
        speak('Sorry! I didn\'t get that! Try typing the command!')
        event, values = win.read()
        query = values[0]
        print('>>>>>The user wrote',values[0])
        win['udisp'].update(query)
    query = query.lower()

    if 'pick up blue chocolate' in query or 'blue chocolate' in query or 'blue' in query or 'blue orbit' in query:
            win['adisp'].update('(Identified Blue Orbit)')
            t.sleep(0.5)
            print('Identified Blue Orbit')
            blue()
    elif 'pick up red chocolate' in query or 'red chocolate' in query or 'red' in query or 'kit kat' in query:
            win['adisp'].update('(Identified Red candy)')
            t.sleep(0.5)
            print('Identified Red candy')
            red()
            
    elif 'yellow chocolate' in query or 'yellow' in query or 'yellow orbit' in query:
            win['adisp'].update('(Identified Yellow Orbit)')
            t.sleep(0.5)
            print('Identified Yellow Orbit')
            yellow()

    elif 'pick up boomer' in query or 'boomer' in query or 'purple'in query or 'pink' in query or 'gum' in query or 'bubble gum' in query:
            win['adisp'].update('(Identified Boomer)')
            t.sleep(0.5)
            print('Identified Boomer')
            purple()

    elif 'dark fantasy' in query or 'biscuit' in query or 'Brown' in query or 'black' in query or 'dark brown' in query:
            win['adisp'].update('(Identified Dark Fantasy)')
            t.sleep(0.5)
            print('Identified Dark Fantasy')
            brown()



#############################################################short name
def SHORTusername():
    speak('What is your nickname?')
    tic=t.time()
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        win['adisp'].update('Listening...')
        t.sleep(0.5)
        r.pause_threshold =  1
        audio = r.listen(source)
    toc=t.time()
    s_elapse = toc - tic
    try:
        query = r.recognize_google(audio, language='en-in')
        print('Human:  ' + query + '\n')
        win['udisp'].update(query)
    except sr.UnknownValueError or s_elapse>10:
        speak('Sorry! I didn\'t get that! Try typing the command!')
        event, values = win.read()
        query = values[0]
        print('>>>>>The user wrote',values[0])
        #query = str(input('Command: '))
        win['udisp'].update(query)
    query = query.lower()
    win['adisp'].update('Your name is '+ query)
    speak('Your name is '+ query)
    speak('Am I correct? (YES or NO) ?')
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        win['adisp'].update('Listening...')
        t.sleep(0.5)
        r.pause_threshold =  1
        audio = r.listen(source)
    toc=t.time()
    s_elapse = toc - tic
    try:
        query = r.recognize_google(audio, language='en-in')
        print('Human:  ' + query + '\n')
        win['udisp'].update(query)
    except sr.UnknownValueError or s_elapse>10:
        speak('Sorry! I didn\'t get that! Try typing the command!')
        event, values = win.read()
        query = values[0]
        print('>>>>>The user wrote',values[0])
        #query = str(input('Command: '))
        win['udisp'].update(query)
    query = query.lower()
    if 'yes' in query or 's' in query or 'yeah' in query or 'correct' in query:
        S_username = query
        return S_username
        #break
    else:
        win['adisp'].update('Please type your nick name')
        t.sleep(0.5)
        speak("Please type your nick name")
        events, values = win.read()
        query = values[0]
        S_username = query
        return S_username
        #break

###############################################################################################################
def dobotprint(tx1):
    CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

    api = dType.load() #Load Dll
    state = dType.ConnectDobot(api, "", 115200)[0] #Connect Dobot
    print("Connect status:",CON_STR[state])

    rx=250
    ry=150
    zd = -73 #/////////////////////////////////PLEASE CHANGE THE VERTICAL HEIGHT ACCORDING TO THE ENVIRONMENT

    if (state == dType.DobotConnect.DobotConnect_NoError):
        dType.SetQueuedCmdClear(api)  #Clear Command Queued
        dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 0)
        dType.SetPTPJointParams(api, 100, 100, 100, 100, 100, 100, 100, 100, isQueued = 1)
        dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)
        dType.SetARCParams(api,10,10,10,10, isQueued = 0)
        k=0
        hi = "HI"
        txU1 = tx1.upper()
        abc = hi + txU1
        hilen  = len(hi)
        texlen = len(txU1)
        lenabc = len(abc)
        while k<lenabc:
            if k<hilen:
                ry = 150-(k*20)
            else:
                rx = 220
                ry = 150 - ((k-hilen)*20)
            if abc[k]=='A':
                #~~~~~~~~~~~~~~~~~~~~~~~A~~~~~~~~~~~~~~~~~~~~~~~~~~
                pa0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                #pa1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #start
                pa2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,zd,0,isQueued=0) #down
                pa3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-10,zd,0,isQueued=0) #/
                pa4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,zd,0,isQueued=0) #\
                pa5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) # lift
                pa6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-5,0,0,isQueued=0) #---
                pa7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-5,zd,0,isQueued=0) #down
                pa8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-15,zd,0,isQueued=0) #-
                pa8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-15,0,0,isQueued=0) #lift
                pa9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->A")
            elif abc[k]=='B':
                #~~~~~~~~~~~~~~~~~~~~~~~B~~~~~~~~~~~~~~~~~~~~~~~~~~
                pb0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0, start
                pb1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,zd,0,isQueued=0) #down
                pb2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-0,zd,0,isQueued=0) #|^
                pb3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-10,zd,0,isQueued=0) #->
                pb4 = dType.SetARCCmd(api,[rx+15,ry-15,zd,0],[rx+10,ry-10,zd,0],isQueued=0) #)v
                pb5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-0,zd,0,isQueued=0) #<-
                pb6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,zd,0,isQueued=0) #->
                pb7 = dType.SetARCCmd(api,[rx+5,ry-15,zd,0],[rx+0,ry-10,zd,0],isQueued=0) #)v
                pb8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,zd,0,isQueued=0) #<-
                pb8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #lift
                pb9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->B")
            elif abc[k]=='C':
                #~~~~~~~~~~~~~~~~~~~~~~~C~~~~~~~~~~~~~~~~~~~~~~~~~~
                pc0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pc1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+17,ry-17,0,0,isQueued=0) #start
                pc2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+17,ry-17,zd,0,isQueued=0) #down
                pc3 = dType.SetARCCmd(api,[rx+20,ry-10,zd,0],[rx+17,ry-2,zd,0],isQueued=0) #//\\
                pc4 = dType.SetARCCmd(api,[rx+10,ry-0,zd,0],[rx+2,ry-2,zd,0],isQueued=0) #(
                pc5 = dType.SetARCCmd(api,[rx+0,ry-10,zd,0],[rx+2,ry-17,zd,0],isQueued=0) #\\//
                pc6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+2,ry-17,0,0,isQueued=0) #lift
                pc7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->C")
            elif abc[k]=='D':
                #~~~~~~~~~~~~~~~~~~~~~~~D~~~~~~~~~~~~~~~~~~~~~~~~~~
                pd0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pd1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,zd,0,isQueued=0) #down
                pd2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-0,zd,0,isQueued=0) #|^
                pd3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-10,zd,0,isQueued=0) #->
                pd4 = dType.SetARCCmd(api,[rx+10,ry-15,zd,0],[rx+0,ry-10,zd,0],isQueued=0) #)
                pd5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,zd,0,isQueued=0) #<-
                pd6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #lift
                pd7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->D")
            elif abc[k]=='E':
                #~~~~~~~~~~~~~~~~~~~~~~~E~~~~~~~~~~~~~~~~~~~~~~~~~~
                pe0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pe1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,0,0,isQueued=0) #start
                pe2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,zd,0,isQueued=0) #down
                pe3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-0,zd,0,isQueued=0) #<-
                pe4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,zd,0,isQueued=0) #|v
                pe5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,zd,0,isQueued=0) #->
                pe6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,0,0,isQueued=0) #lift
                pe7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-0,0,0,isQueued=0) #--
                pe8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-0,zd,0,isQueued=0) #down
                pe9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,zd,0,isQueued=0) #->
                pe10 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,0,0,isQueued=0) #lift
                pe11 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->E")
            elif abc[k]=='F':
                #~~~~~~~~~~~~~~~~~~~~~~~F~~~~~~~~~~~~~~~~~~~~~~~~~~
                pf0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pf1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,0,0,isQueued=0) #start
                pf2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,zd,0,isQueued=0) #down
                pf3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-0,zd,0,isQueued=0) #<-
                pf4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,zd,0,isQueued=0) #|v
                pf5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #lift
                pf6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-0,0,0,isQueued=0) #--
                pf7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-0,zd,0,isQueued=0) #down
                pf8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,zd,0,isQueued=0) #->
                pf9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,0,0,isQueued=0) #lift
                pf10 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->F")
            elif abc[k]=='G':
                #~~~~~~~~~~~~~~~~~~~~~~~G~~~~~~~~~~~~~~~~~~~~~~~~~~
                pg0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pg1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+17,ry-17,0,0,isQueued=0) #start
                pg2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+17,ry-17,zd,0,isQueued=0) #down
                pg3 = dType.SetARCCmd(api,[rx+20,ry-10,zd,0],[rx+17,ry-2,zd,0],isQueued=0) #/\
                pg4 = dType.SetARCCmd(api,[rx+10,ry-0,zd,0],[rx+2,ry-2,zd,0],isQueued=0) #(
                pg5 = dType.SetARCCmd(api,[rx+0,ry-10,zd,0],[rx+2,ry-17,zd,0],isQueued=0) #\/
                pg6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-17,zd,0,isQueued=0) #|^
                pg7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,zd,0,isQueued=0) #<-
                pg8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,0,0,isQueued=0) #lift
                pg9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->G")
            elif abc[k]=='H':
                #~~~~~~~~~~~~~~~~~~~~~~~H~~~~~~~~~~~~~~~~~~~~~~~~~~
                ph0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                ph1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-0,0,0,isQueued=0) #start
                ph2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-0,zd,0,isQueued=0) #down
                ph3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,zd,0,isQueued=0) #|v
                ph4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #lift
                ph5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,0,0,isQueued=0) #--
                ph6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,zd,0,isQueued=0) #down
                ph7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,zd,0,isQueued=0) #|v
                ph8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,0,0,isQueued=0) #lift
                ph9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-0,0,0,isQueued=0) #--
                ph10 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-0,zd,0,isQueued=0) #down
                ph11 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-17,zd,0,isQueued=0) #->
                ph12 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-17,0,0,isQueued=0) #lift
                ph13 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->H")
            elif abc[k]=='I':
                #~~~~~~~~~~~~~~~~~~~~~~~I~~~~~~~~~~~~~~~~~~~~~~~~~~
                pi0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pi1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,0,0,isQueued=0) #start
                pi2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,zd,0,isQueued=0) #down
                pi3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,zd,0,isQueued=0) #->
                pi4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,0,0,isQueued=0) #lift
                pi5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-2,0,0,isQueued=0) #--
                pi6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-2,zd,0,isQueued=0) #down
                pi7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,zd,0,isQueued=0) #->
                pi8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,0,0,isQueued=0) #lift
                pi9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-10,0,0,isQueued=0) #--
                pi10 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-10,zd,0,isQueued=0) #down
                pi11 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-10,zd,0,isQueued=0) #|v
                pi12 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-10,0,0,isQueued=0) #lift
                pi13 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->I")
            elif abc[k]=='J':
                #~~~~~~~~~~~~~~~~~~~~~~~J~~~~~~~~~~~~~~~~~~~~~~~~~~
                pj0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pj1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,0,0,isQueued=0) #start
                pj2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,zd,0,isQueued=0) #down
                pj3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,zd,0,isQueued=0) #->
                pj4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,0,0,isQueued=0) #lift
                pj5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-10,0,0,isQueued=0) #--
                pj6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-10,zd,0,isQueued=0) #down
                pj7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,zd,0,isQueued=0) #|v
                pj8 = dType.SetARCCmd(api,[rx+0,ry-5,zd,0],[rx+10,ry-0,zd,0],isQueued=0) #\\//
                pj9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-0,0,0,isQueued=0) #lift
                pj10 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->J")
            elif abc[k]=='K':
                #~~~~~~~~~~~~~~~~~~~~~~~K~~~~~~~~~~~~~~~~~~~~~~~~~~
                pk0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0,start
                pk1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,zd,0,isQueued=0) #down
                pk2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-0,zd,0,isQueued=0) #|^
                pk3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-0,0,0,isQueued=0) #lift
                pk4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-15,0,0,isQueued=0) #--
                pk5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-15,zd,0,isQueued=0) #down
                pk6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-0,zd,0,isQueued=0) #/
                pk7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-0,0,0,isQueued=0) #lift
                pk8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+12,ry-5,0,0,isQueued=0) #--
                pk9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+12,ry-5,zd,0,isQueued=0) #down
                pk10 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-15,zd,0,isQueued=0) #\
                pk11 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-15,0,0,isQueued=0) #lift
                pk12 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->K")
            elif abc[k]=='L':
                #~~~~~~~~~~~~~~~~~~~~~~~L~~~~~~~~~~~~~~~~~~~~~~~~~~
                pl0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pl1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-0,0,0,isQueued=0) #start
                pl2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-0,zd,0,isQueued=0) #down
                pl3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,zd,0,isQueued=0) #|v
                pl4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,zd,0,isQueued=0) #->
                pl5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,0,0,isQueued=0) #lift
                pl6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->L")
            elif abc[k]=='M':
                #~~~~~~~~~~~~~~~~~~~~~~~M~~~~~~~~~~~~~~~~~~~~~~~~~~
                pm0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pm1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-2,0,0,isQueued=0) #start
                pm2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-2,zd,0,isQueued=0) #down
                pm3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,zd,0,isQueued=0) #|^
                pm4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,zd,0,isQueued=0) #\
                pm5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,zd,0,isQueued=0) #/
                pm6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,zd,0,isQueued=0) #|v
                pm7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,0,0,isQueued=0) #lift
                pm8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->M")
            elif abc[k]=='N':
                #~~~~~~~~~~~~~~~~~~~~~~~N~~~~~~~~~~~~~~~~~~~~~~~~~~
                pn0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pn1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-2,0,0,isQueued=0) #start
                pn2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-2,zd,0,isQueued=0) #down
                pn3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,zd,0,isQueued=0) #|^
                pn4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,zd,0,isQueued=0) #\
                pn5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,zd,0,isQueued=0) #|^
                pn6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,0,0,isQueued=0) #lift
                pn7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->N")
            elif abc[k]=='O':
                #~~~~~~~~~~~~~~~~~~~~~~~O~~~~~~~~~~~~~~~~~~~~~~~~~~
                po0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                po1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+17,ry-17,0,0,isQueued=0) #start
                po2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+17,ry-17,zd,0,isQueued=0) #down
                po3 = dType.SetARCCmd(api,[rx+20,ry-10,zd,0],[rx+17,ry-2,zd,0],isQueued=0) #/\
                po4 = dType.SetARCCmd(api,[rx+10,ry-0,zd,0],[rx+2,ry-2,zd,0],isQueued=0) #(
                po5 = dType.SetARCCmd(api,[rx+0,ry-10,zd,0],[rx+2,ry-17,zd,0],isQueued=0) #\/
                po6 = dType.SetARCCmd(api,[rx+10,ry-20,zd,0],[rx+17,ry-17,zd,0],isQueued=0) #)
                po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+17,ry-17,0,0,isQueued=0) #lift
                po8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->O")
            elif abc[k]=='P':
                #~~~~~~~~~~~~~~~~~~~~~~~P~~~~~~~~~~~~~~~~~~~~~~~~~~
                pp0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0, start
                pp1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,zd,0,isQueued=0) #down
                pp2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-0,zd,0,isQueued=0) #|^
                pp3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-10,zd,0,isQueued=0) #->
                pp4 = dType.SetARCCmd(api,[rx+15,ry-17,zd,0],[rx+10,ry-10,zd,0],isQueued=0) #)
                pp5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-0,zd,0,isQueued=0) #<-
                pp6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-0,0,0,isQueued=0) #lift
                pp7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->P")
            elif abc[k]=='Q':
                #~~~~~~~~~~~~~~~~~~~~~~~Q~~~~~~~~~~~~~~~~~~~~~~~~~~
                pq0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pq1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+17,ry-17,0,0,isQueued=0) #start
                pq2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+17,ry-17,zd,0,isQueued=0) #down
                pq3 = dType.SetARCCmd(api,[rx+20,ry-10,zd,0],[rx+17,ry-2,zd,0],isQueued=0) #/\
                pq4 = dType.SetARCCmd(api,[rx+10,ry-0,zd,0],[rx+2,ry-2,zd,0],isQueued=0) #(
                pq5 = dType.SetARCCmd(api,[rx+0,ry-10,zd,0],[rx+2,ry-17,zd,0],isQueued=0) #\/
                pq6 = dType.SetARCCmd(api,[rx+10,ry-20,zd,0],[rx+17,ry-17,zd,0],isQueued=0) #)           
                pq7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+17,ry-17,0,0,isQueued=0) #lift
                pq8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+7,ry-12,0,0,isQueued=0) #--
                pq9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+7,ry-12,zd,0,isQueued=0) #down
                pq10 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,zd,0,isQueued=0) #\
                pq11 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end, lift
                print(k,"-->Q")
            elif abc[k]=='R':
                #~~~~~~~~~~~~~~~~~~~~~~~R~~~~~~~~~~~~~~~~~~~~~~~~~~
                pr0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0, start
                pr1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,zd,0,isQueued=0) #down
                pr2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-0,zd,0,isQueued=0) #|^
                pr3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-10,zd,0,isQueued=0) #->
                pr4 = dType.SetARCCmd(api,[rx+15,ry-17,zd,0],[rx+10,ry-10,zd,0],isQueued=0) #)
                pr5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-0,zd,0,isQueued=0) #<-
                pr6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,zd,0,isQueued=0) #->
                pr7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-15,zd,0,isQueued=0) #\
                pr8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-15,0,0,isQueued=0) #lift
                pr9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->R")
            elif abc[k]=='S':
                #~~~~~~~~~~~~~~~~~~~~~~~S~~~~~~~~~~~~~~~~~~~~~~~~~~
                ps0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                ps1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+17,ry-17,0,0,isQueued=0) #start
                ps2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+17,ry-17,zd,0,isQueued=0) #down
                ps3 = dType.SetARCCmd(api,[rx+20,ry-10,zd,0],[rx+17,ry-2,zd,0],isQueued=0) #/\
                ps4 = dType.SetARCCmd(api,[rx+12,ry-2,zd,0],[rx+10,ry-10,zd,0],isQueued=0) #\_
                ps5 = dType.SetARCCmd(api,[rx+7,ry-17,zd,0],[rx+2,ry-17,zd,0],isQueued=0)  #-\
                ps6 = dType.SetARCCmd(api,[rx+0,ry-10,zd,0],[rx+2,ry-2,zd,0],isQueued=0)    #\/
                ps7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+2,ry-2,0,0,isQueued=0) #lift
                ps8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->S")
            elif abc[k]=='T':
                #~~~~~~~~~~~~~~~~~~~~~~~T~~~~~~~~~~~~~~~~~~~~~~~~~~
                pt0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pt1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,0,0,isQueued=0) #start
                pt2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,zd,0,isQueued=0) #down
                pt3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,zd,0,isQueued=0) #->
                pt4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,0,0,isQueued=0) #lift
                pt5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-10,0,0,isQueued=0) #--
                pt6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-10,zd,0,isQueued=0) #down
                pt7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-10,zd,0,isQueued=0) #|v
                pt8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-10,0,0,isQueued=0) #lift
                pt9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->T")
            elif abc[k]=='U':
                #~~~~~~~~~~~~~~~~~~~~~~~U~~~~~~~~~~~~~~~~~~~~~~~~~~
                pu0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pu1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,0,0,isQueued=0) #start
                pu2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,zd,0,isQueued=0) #down
                pu3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+5,ry-2,zd,0,isQueued=0) #|v
                pu4 = dType.SetARCCmd(api,[rx+0,ry-10,zd,0],[rx+5,ry-17,zd,0],isQueued=0) #\\//
                pu5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,zd,0,isQueued=0) #|^
                pu6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,0,0,isQueued=0) #lift
                pu7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->U")
            elif abc[k]=='V':
                #~~~~~~~~~~~~~~~~~~~~~~~V~~~~~~~~~~~~~~~~~~~~~~~~~~
                pv0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pv1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,0,0,isQueued=0) #start
                pv2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,zd,0,isQueued=0) #down
                pv3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-10,zd,0,isQueued=0) #\
                pv4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,zd,0,isQueued=0) #/
                pv5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,0,0,isQueued=0) #lift
                pv6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->V")
            elif abc[k]=='W':
                #~~~~~~~~~~~~~~~~~~~~~~~W~~~~~~~~~~~~~~~~~~~~~~~~~~
                pw0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pw1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,0,0,isQueued=0) #start
                pw2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,zd,0,isQueued=0) #down
                pw3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-2,zd,0,isQueued=0) #|v
                pw4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,zd,0,isQueued=0) #/
                pw5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,zd,0,isQueued=0) #\
                pw6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,zd,0,isQueued=0) #|^
                pw7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,0,0,isQueued=0) #lift
                pw8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->W")
            elif abc[k]=='X':
                #~~~~~~~~~~~~~~~~~~~~~~~X~~~~~~~~~~~~~~~~~~~~~~~~~~
                px0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                px1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,0,0,isQueued=0) #start
                px2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,zd,0,isQueued=0) #down
                px3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,zd,0,isQueued=0) #\
                px4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,0,0,isQueued=0) #lift
                px5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,0,0,isQueued=0) #--
                px6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,zd,0,isQueued=0) #down
                px7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-2,zd,0,isQueued=0) #/
                px8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-2,0,0,isQueued=0) #lift
                px9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->X")
            elif abc[k]=='Y':
                #~~~~~~~~~~~~~~~~~~~~~~~Y~~~~~~~~~~~~~~~~~~~~~~~~~~
                py0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                py1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,0,0,isQueued=0) #start
                py2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,zd,0,isQueued=0) #down
                py3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,zd,0,isQueued=0) #\
                py4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-10,zd,0,isQueued=0) #|v
                py5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,zd,0,isQueued=0) #/
                py6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,zd,0,isQueued=0) #/
                py7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,0,0,isQueued=0) #lift
                py8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->Y")
            elif abc[k]=='Z':
                #~~~~~~~~~~~~~~~~~~~~~~~Z~~~~~~~~~~~~~~~~~~~~~~~~~~
                pz0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                pz1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,0,0,isQueued=0) #start
                pz2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-2,zd,0,isQueued=0) #down
                pz3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-17,zd,0,isQueued=0) #->
                pz4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-2,zd,0,isQueued=0) #/
                pz5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,zd,0,isQueued=0) #->
                pz9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-17,0,0,isQueued=0) #lift
                pz10 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->Z")
            elif abc[k]=='0':
                #~~~~~~~~~~~~~~~~~~~~~~~0~~~~~~~~~~~~~~~~~~~~~~~~~~
                p00 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                p01 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+15,ry-15,0,0,isQueued=0) #start
                p02 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+15,ry-15,zd,0,isQueued=0) #down
                p03 = dType.SetARCCmd(api,[rx+20,ry-10,zd,0],[rx+15,ry-5,zd,0],isQueued=0) #/\
                p04 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+5,ry-5,zd,0,isQueued=0) #|v
                p05 = dType.SetARCCmd(api,[rx+0,ry-10,zd,0],[rx+5,ry-15,zd,0],isQueued=0) #\/
                p06 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+15,ry-15,zd,0,isQueued=0) #|^
                p07 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+15,ry-15,0,0,isQueued=0) #lift
                p08 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->0")
            elif abc[k]=='1':
                #~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~
                p10 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                p11 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+15,ry-5,0,0,isQueued=0) #start
                p12 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+15,ry-5,zd,0,isQueued=0) #down
                p13 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-10,zd,0,isQueued=0) #/
                p14 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-10,zd,0,isQueued=0) #|
                p15 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-5,zd,0,isQueued=0) #<-
                p16 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-15,zd,0,isQueued=0) #->
                p17 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-15,0,0,isQueued=0) #lift
                p18 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->1")
            elif abc[k]=='2':
                #~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~
                p20 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                p21 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+15,ry-5,0,0,isQueued=0) #start
                p22 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+15,ry-5,zd,0,isQueued=0) #down
                p23 = dType.SetARCCmd(api,[rx+20,ry-10,zd,0],[rx+15,ry-15,zd,0],isQueued=0) #/\
                #p24 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+5,ry-10,zd,0,isQueued=0) #//
                p25 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-5,zd,0,isQueued=0) #/
                p26 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-15,zd,0,isQueued=0) #->
                p27 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-15,0,0,isQueued=0) #lift
                p28 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->2")
            elif abc[k]=='3':
                #~~~~~~~~~~~~~~~~~~~~~~~3~~~~~~~~~~~~~~~~~~~~~~~~~~
                p30 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                p31 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-5,0,0,isQueued=0) #start
                p32 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-5,zd,0,isQueued=0) #down
                p33 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-15,zd,0,isQueued=0) #->
                p34 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-5,zd,0,isQueued=0) #/
                p35 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,zd,0,isQueued=0) #->
                p36 = dType.SetARCCmd(api,[rx+5,ry-15,zd,0],[rx+0,ry-10,zd,0],isQueued=0) #)
                p37 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+5,ry-0,zd,0,isQueued=0) #<-
                p38 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+5,ry-0,0,0,isQueued=0) #lift
                p39 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->3")
            elif abc[k]=='4':
                #~~~~~~~~~~~~~~~~~~~~~~~4~~~~~~~~~~~~~~~~~~~~~~~~~~
                p40 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                p41 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-12,0,0,isQueued=0) #start
                p42 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-12,zd,0,isQueued=0) #down
                p43 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-12,zd,0,isQueued=0) #|^
                p44 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-2,zd,0,isQueued=0) #/
                p45 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-15,zd,0,isQueued=0) #->
                p46 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-15,0,0,isQueued=0) #lift
                p47 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->4")
            elif abc[k]=='5':
                #~~~~~~~~~~~~~~~~~~~~~~~5~~~~~~~~~~~~~~~~~~~~~~~~~~
                p50 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                p51 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-15,0,0,isQueued=0) #start
                p52 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-15,zd,0,isQueued=0) #down
                p53 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-5,zd,0,isQueued=0) #<-
                p54 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-5,zd,0,isQueued=0) #|v
                p55 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-15,zd,0,isQueued=0) #->
                p56 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+5,ry-15,zd,0,isQueued=0) #|v
                p57 = dType.SetARCCmd(api,[rx+0,ry-10,zd,0],[rx+5,ry-5,zd,0],isQueued=0) #\/
                p58 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+5,ry-5,0,0,isQueued=0) #lift
                p59 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->5")
            elif abc[k]=='6':
                #~~~~~~~~~~~~~~~~~~~~~~~6~~~~~~~~~~~~~~~~~~~~~~~~~~
                p60 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                p61 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+17,ry-15,0,0,isQueued=0) #start
                p62 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+17,ry-15,zd,0,isQueued=0) #down
                p63 = dType.SetARCCmd(api,[rx+20,ry-10,zd,0],[rx+15,ry-5,zd,0],isQueued=0) #/\
                p64 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+5,ry-5,zd,0,isQueued=0) #|v
                p65 = dType.SetARCCmd(api,[rx+0,ry-10,zd,0],[rx+5,ry-15,zd,0],isQueued=0) #\/
                p66 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-15,zd,0,isQueued=0) #|^
                p67 = dType.SetARCCmd(api,[rx+12,ry-10,zd,0],[rx+10,ry-5,zd,0],isQueued=0) #/\
                p68 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-5,0,0,isQueued=0) #lift
                p69 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->6")
            elif abc[k]=='7':
                #~~~~~~~~~~~~~~~~~~~~~~~7~~~~~~~~~~~~~~~~~~~~~~~~~~
                p00 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                p01 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-5,0,0,isQueued=0) #start
                p02 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-5,zd,0,isQueued=0) #down
                p04 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-15,zd,0,isQueued=0) #->
                p06 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-5,zd,0,isQueued=0) #/
                p07 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-5,0,0,isQueued=0) #lift
                p08 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->7")
            elif abc[k]=='8':
                #~~~~~~~~~~~~~~~~~~~~~~~8~~~~~~~~~~~~~~~~~~~~~~~~~~
                p00 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                p01 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,0,0,isQueued=0) #start
                p02 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,zd,0,isQueued=0) #down
                p03 = dType.SetARCCmd(api,[rx+15,ry-15,zd,0],[rx+20,ry-10,zd,0],isQueued=0) #)
                p05 = dType.SetARCCmd(api,[rx+15,ry-5,zd,0],[rx+10,ry-10,zd,0],isQueued=0) #(
                p03 = dType.SetARCCmd(api,[rx+5,ry-5,zd,0],[rx+0,ry-10,zd,0],isQueued=0) #(
                p05 = dType.SetARCCmd(api,[rx+5,ry-15,zd,0],[rx+10,ry-10,zd,0],isQueued=0) #)
                p07 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-10,0,0,isQueued=0) #lift
                p08 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->8")
            elif abc[k]=='9':
                #~~~~~~~~~~~~~~~~~~~~~~~9~~~~~~~~~~~~~~~~~~~~~~~~~~
                p00 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                p01 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-15,0,0,isQueued=0) #start
                p02 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+10,ry-15,zd,0,isQueued=0) #down
                p03 = dType.SetARCCmd(api,[rx+7,ry-10,zd,0],[rx+10,ry-5,zd,0],isQueued=0) #\/
                p04 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+15,ry-5,zd,0,isQueued=0) #|^
                p05 = dType.SetARCCmd(api,[rx+20,ry-10,zd,0],[rx+15,ry-15,zd,0],isQueued=0) #/\
                p06 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+5,ry-15,zd,0,isQueued=0) #|v
                p03 = dType.SetARCCmd(api,[rx+0,ry-10,zd,0],[rx+2,ry-5,zd,0],isQueued=0) #\/
                p07 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+2,ry-5,0,0,isQueued=0) #lift
                p08 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->9")
            elif abc[k]==' ':
                #~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~~~~~~~~~~
                pspace0 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0)
                print(k,"--> ")
            elif abc[k]=='/':
                #~~~~~~~~~~~~~~~~~~~~~~~/~~~~~~~~~~~~~~~~~~~~~~~~~~
                p00 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                p01 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-15,0,0,isQueued=0) #start
                p02 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-15,zd,0,isQueued=0) #down
                p04 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-5,zd,0,isQueued=0) #/
                p07 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-5,0,0,isQueued=0) #lift
                p08 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"-->/")
            elif abc[k]=='&':
                #~~~~~~~~~~~~~~~~~~~~~~~& next line~~~~~~~~~~~~~~~~~~~~~~~~~~
                rx = 220
                
                p00 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-0,0,0,isQueued=0) #0
                p01 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-15,0,0,isQueued=0) #start
                p02 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+20,ry-15,zd,0,isQueued=0) #down
                p04 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-5,zd,0,isQueued=0) #/
                p07 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-5,0,0,isQueued=0) #lift
                p08 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,rx+0,ry-20,0,0,isQueued=0) #end
                print(k,"--> next line")
            else:
                print(k,"-->Invalid character")
            t.sleep(7)
            k=k+1

    #Disconnect Dobot
    dType.DisconnectDobot(api)

########################################## dance

def dance():
    CON_STR = {
        dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
        dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
        dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

    #Load Dll
    api = dType.load()

    #Connect Dobot
    state = dType.ConnectDobot(api, "", 115200)[0]
    print("Connect status:",CON_STR[state])

    xoff = 200
    zc = 0
    rd = 50
    xo = 200
    yc = 50
    zc = 50
    ry = 100 # half the horizontal range
    rz = 10 

    if (state == dType.DobotConnect.DobotConnect_NoError):
        print("Entering loop")
        #Clean Command Queued
        dType.SetQueuedCmdClear(api)

        #Async Motion Params Setting
        dType.SetHOMEParams(api, xoff, 0, zc, 0, isQueued = 0) #centre
        dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 0)
        dType.SetARCParams(api, 100, 100, 100, 100, isQueued = 0)

        dType.SetPTPCommonParams(api, 100, 100, isQueued = 0)

        #comment this to save time
        # dType.SetHOMECmd(api, temp = 0, isQueued = 1)

        p1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xoff,0,zc-rd,0,isQueued=0) #[1]
        for i in range (0, 1):
            
            po3 = dType.SetARCCmd(api,[xoff,-rd,zc,0],[xoff,0,zc+rd,0],isQueued=0) #( fv
            po4 = dType.SetARCCmd(api,[xoff,rd,zc,0],[xoff,0,zc-rd,0],isQueued=0) #) fv
            po5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xoff,-rd,zc+rd,0,isQueued=0) #\ left go up
            po6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xoff,0,zc-rd,0,isQueued=0) #\ left come back
            po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xoff,rd,zc+rd,0,isQueued=0) #/ right go up
            po8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xoff,0,zc-rd,0,isQueued=0) #/ right come back

            for j in range (0, 6): #up to down
                if i%2==0:
                    po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,0,rz+((10-j)*10),0,isQueued=0)
                else:
                    po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,0,rz+((10-j)*10),0,isQueued=0)
            
            po9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,-yc,zc,0,isQueued=0) #\ left diagonal up
            po10 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo+50,-yc,zc,0,isQueued=0) #\ left diagonal up FWD
            po11 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,-yc,zc,0,isQueued=0) #\ left diagonal up BCK
            po10 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo+50,-yc,zc,0,isQueued=0) #\ left diagonal up FWD
            po11 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,-yc,zc,0,isQueued=0) #\ left diagonal up BCK
            po12 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,yc,-zc,0,isQueued=0) #\ left diagonal down
            po13 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo+50,yc,-zc,0,isQueued=0) #\ left diagonal down FWD
            po14 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,yc,-zc,0,isQueued=0) #\ left diagonal down BCK
            po13 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo+50,yc,-zc,0,isQueued=0) #\ left diagonal down FWD
            po14 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,yc,-zc,0,isQueued=0) #\ left diagonal down BCK
            po15 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,0,0,0,isQueued=0) #centre


            for j in range (0, 6): #down to up
                if j%2==0:
                    po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,ry,rz+(j*10),0,isQueued=0)
                else:
                    po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,-ry,rz+(j*10),0,isQueued=0)

            for j in range (0, 6): #up to down
                if i%2==0:
                    po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,ry,rz+((10-j)*10),0,isQueued=0)
                else:
                    po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,-ry,rz+((10-j)*10),0,isQueued=0)
            
        p1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,-100,0,0,isQueued=0) #1
        po3 = dType.SetARCCmd(api,[xo,0,-50,0],[xo,100,0,0],isQueued=0) # 1-2-3 L to R
        po3 = dType.SetARCCmd(api,[xo,0,-45,0],[xo,-80,0,0],isQueued=0) # 3-4-5 R to L
        po3 = dType.SetARCCmd(api,[xo,0,-40,0],[xo,80,0,0],isQueued=0) # 5-6-7 L to R
        po3 = dType.SetARCCmd(api,[xo,0,-35,0],[xo,-60,0,0],isQueued=0) # 7-8-9 R to L
        po3 = dType.SetARCCmd(api,[xo,0,-30,0],[xo,60,0,0],isQueued=0) # 9-10-11 L to R
        po3 = dType.SetARCCmd(api,[xo,0,-25,0],[xo,-40,0,0],isQueued=0) # 11-12-13 R to L
        po3 = dType.SetARCCmd(api,[xo,0,-20,0],[xo,40,0,0],isQueued=0) # 13-14-15 L to R
        po3 = dType.SetARCCmd(api,[xo,0,-15,0],[xo,-20,0,0],isQueued=0) # 15-16-17 R to L
        po3 = dType.SetARCCmd(api,[xo,0,-10,0],[xo,20,0,0],isQueued=0) # 17-18-19 L to R
        po8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,0,0,0,isQueued=0) #/ right come back
        print("WELCOME!!!")

          # t.sleep(2)

    #Disconnect Dobot
    dType.DisconnectDobot(api)

###############################################################################################################









################################################################## program starts
# intro talk
# Good Moning/Afternoon/Evening
t.sleep(5)
greetMe()
win['adisp'].update('Welcome to the Open Day at CPDM, IISC Bengaluru')
t.sleep(0.5)
speak('Welcome to the Open Day at CPDM. IISC Bengaluru')
t.sleep(0.5)
speak('What is your name')
    #query = myCommand()
tic=t.time()
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Listening...")
    win['adisp'].update('Listening...')
    t.sleep(0.5)
    r.pause_threshold =  1
    audio = r.listen(source)
toc=t.time()
s_elapse = toc - tic
try:
    query = r.recognize_google(audio, language='en-in')
    print('Human:  ' + query + '\n')
    win['udisp'].update(query)
except sr.UnknownValueError or s_elapse>10:
    win['adisp'].update('Sorry! I didn\'t get that! Try typing the command!')
    t.sleep(0.5)
    speak('Sorry! I didn\'t get that! Try typing the command!')
    event, values = win.read()
    query = values[0]
    print('>>>>>The user wrote',values[0])
    win['udisp'].update(query)
query = query.lower()
q1 = query

# verify: tell the name
win['adisp'].update('Your name is '+q1)
t.sleep(0.5)
speak('Your name is '+q1)

# verify: if it is correct
win['adisp'].update('Am I correct? (YES or NO) ?')
t.sleep(0.5)
speak('Am I correct? (YES or NO) ?')
with sr.Microphone() as source:                                                                       
    print("Listening...")
    win['adisp'].update('Listening...')
    t.sleep(0.5)
    r.pause_threshold =  1
    audio = r.listen(source)
toc=t.time()
s_elapse = toc - tic
try:
    query = r.recognize_google(audio, language='en-in')
    print('Human:  ' + query + '\n')
    win['udisp'].update(query)
except sr.UnknownValueError or s_elapse>10:
    win['adisp'].update('Sorry! I didn\'t get that! Try typing the command!')
    t.sleep(0.5)
    speak('Sorry! I didn\'t get that! Try typing the command!')
    event, values = win.read()
    query = values[0]
    print('>>>>>The user wrote',values[0])
    win['udisp'].update(query)
query = query.lower()
namecor = query

# initialize the username bases on YES/NO
if 'yes' in namecor or 's' in namecor or 'yeah' in namecor or 'correct' in namecor:
    username = q1
else:
    win['adisp'].update('Can you please type your name?')
    speak("Can you please type your name?")
    event, values = win.read()
    username = values[0]

# Nmasthey + Name
win['adisp'].update('Namasthey ' + username +'!' + ' I am Robot ROHINI')
t.sleep(0.5)
speak('Namasthey ' + username +'!' + ' I am Robot ROHINI')

# Menu
win['adisp'].update('I can print a text, give you a candy, dance and tell you the time.')
t.sleep(0.5)
speak('I can print a text, give you a candy, dance and tell you the time.')


# Infinite loop
if __name__ == '__main__':
    while True:
        speak('What can I do for you?')
        tic=t.time()
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:                                                                       
            print("Listening...")
            win['adisp'].update('Listening...')
            t.sleep(0.5)
            r.pause_threshold =  1
            audio = r.listen(source)
        toc=t.time()
        s_elapse = toc - tic
        try:
            query = r.recognize_google(audio, language='en-in')
            print('Human:  ' + query + '\n')
            win['udisp'].update(query)
        except sr.UnknownValueError or s_elapse>10:
            win['adisp'].update('Sorry! I didn\'t get that! Try typing the command!')
            t.sleep(0.5)
            speak('Sorry! I didn\'t get that! Try typing the command!')
            event, values = win.read()
            query = values[0]
            print('>>>>>The user wrote',values[0])
            #query = str(input('Command: '))
            win['udisp'].update(query)
        query = query.lower()
        
        # Time
        if 'what\'s the time' in query or 'what is the time now' in query or 'what is the time now' in query or 'what is the time' in query:
            curH = int(datetime.datetime.now().hour)
            curM = int(datetime.datetime.now().minute)
            atext = 'The current time is '+str(curH)+' hours '+str(curM)+' minutes'
            win['adisp'].update(atext)
            t.sleep(0.5)
            speak(atext)
            atext = 'You are at CPDM IISC Bengaluru'
            win['adisp'].update(atext)
            t.sleep(0.5)
            speak(atext)

        # Greeting
        elif "what\'s up" in query or 'how are you' in query or 'how are you doing' in query or 'hi' in query or 'hello' in query or 'hey' in query or 'Namasthey' in query:
            greet1 = ['Hello. It is great to meet you.','Glad to meet you','Namasthey. It is very wonderful to meet you','Hi. Nice to meet you.']
            atext = random.choice(greet1)
            win['adisp'].update(atext)
            t.sleep(0.5)
            speak(atext)

        # Exit
        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'exit' in query or 'done' in query:
            atext = 'Ok. Bye. Have a good day.'
            win['adisp'].update(atext)
            t.sleep(0.5)
            speak(atext)
        # ****************************** DOBOT Dance
        elif 'play music' in query or 'music' in query or 'dance' in query:
            atext = 'Okay, here is your music! Enjoy!'
            win['adisp'].update(atext)
            t.sleep(0.5)
            speak(atext)
            dance()
            playsound('C:\\Users\\user7\\Music\\dobot_dance_audio_1.mp3')

        # *******************************DOBOT Text
        elif 'dobot text' in query or 'dobot' in query or 'text' in query or 'print a text' in query or 'print' in query or 'write' in query or 'right' in query or 'write a text' in query or 'right a text' in query or 'write my name' in query or 'right my name' in query:
            atext = 'Press 1 if the end effector is a pen and 2 if the end effector is a gripper'
            win['adisp'].update(atext)
            t.sleep(0.5)
            speak(atext)
            event, values = win.read()
            end_effector= values[0]
            if (end_effector == 1):
                pass
            else:
                t.sleep(25)
            if len(username)<10:
                tx1 = username
            else:
                tx1 = SHORTusername()
            dobotprint(tx1)

        # *******************************DOBOT Candy
        elif 'pick up a candy' in query or 'give me a candy' in query or 'pick up a chocolate' in query or 'give me a chocolate' in query or 'i want a candy' in query or 'i want a chocolate' in query or 'give' in query or 'candy' in query or 'chocolate' in query:
            atext = 'Press 1 if the end effector is a pen and 2 if the end effector is a gripper'
            win['adisp'].update(atext)
            t.sleep(0.5)
            speak(atext)
            event, values = win.read()
            end_effector= values[0]
            if (end_effector == 2):
                pass
            else:
                t.sleep(30)
            pickupacandy()

        # unidentified query
        else:
            atext = 'Sorry, I couldn\'t get that.'
            win['adisp'].update(atext)
            t.sleep(0.5)
            speak(atext)
            
        #print('Your entry is...',values[0])

win.close()
