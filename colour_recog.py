import pyttsx3
import webbrowser
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


engine = pyttsx3.init()#'dummy')#'sapi5')
client = wolframalpha.Client('89K64G-LQ9AGWR8GU')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
	print('Jarvis: ' + audio)
	engine.say(audio)
	engine.runAndWait()

def greetMe():
	t.sleep(4)
	currentH = int(datetime.datetime.now().hour)
	if currentH >= 0 and currentH < 12:
		speak('Good Morning!')

	if currentH >= 12 and currentH < 18:
		speak('Good Afternoon!')

	if currentH >= 18 and currentH !=0:
		speak('Good Evening!')
	 
def myCommand():
	r = sr.Recognizer() 
	tic = t.time()                                                                                  
	with sr.Microphone() as source:                                                                       
		print("Listening...")
		r.pause_threshold =  1
		audio = r.listen(source)
	talk = t.time()
	delay = talk - tic
	try:
		query = r.recognize_google(audio, language='en-in')
		print('Human:  ' + query + '\n')
		
	except sr.UnknownValueError or delay>10 :
		speak('Sorry! I didn\'t get that! Try typing the command!')
		query = str(input('Command: '))

	return query

def blue(): ## Time
	
	cap = cv2.VideoCapture(0)

	#Setting resolution
	cap.set(3,640)
	cap.set(4,480)


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
				print('Located blue orbit coordinates')
				speak('Orbit Blue is my favorite candy too, so save some for me!')
				exit()
		cv2.imshow("frame", frame)

def yellow(): 
	
	cap = cv2.VideoCapture(0)

	#Setting resolution
	cap.set(3,640)
	cap.set(4,480)


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
				print('Located yellow orbit coordinates')
				speak('I dont like the Orbit yellow very much, so you can have it all')
				exit()
		cv2.imshow("frame", frame)

###############################################################################################################

def red(): 
	
	cap = cv2.VideoCapture(0)

	#Setting resolution
	cap.set(3,640)
	cap.set(4,480)


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
				print('Located coordinates')
				speak('Interesting choice, here you go!')
				exit()
		cv2.imshow("frame", frame)

def brown(): 
	
	cap = cv2.VideoCapture(0)

	#Setting resolution
	cap.set(3,640)
	cap.set(4,480)


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
				print('Located Dark Fantasy coordinates')
				speak('Yummy, great choice! I love chocolate filled biscuits, enjoy!')
				exit()
		cv2.imshow("frame", frame)

def purple(): 
	
	cap = cv2.VideoCapture(0)

	#Setting resolution
	cap.set(3,640)
	cap.set(4,480)


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
				print('Located Boomer coordinates')
				speak('Enjoy your Boomer')
				exit()
		cv2.imshow("frame", frame)

speak('What is the colour of your favorite candy?')

query = myCommand();
query = query.lower()

if 'pick up blue chocolate' in query or 'blue chocolate' in query or 'blue' in query or 'blue orbit' in query:
	print('Identified blue Orbit')
	blue()
elif 'pick up red chocolate' in query or 'red chocolate' in query or 'red' in query or 'kit kat' in query:
	print('Identified Red candy')
	red()
	
elif 'yellow chocolate' in query or 'yellow' in query or 'yellow orbit' in query:
	print('Identified Yellow Orbit')
	yellow()

elif 'pick up boomer' in query or 'boomer' in query or 'purple'in query or 'pink' in query or 'gum' in query or 'bubble gum' in query:
	print('Identified Boomer')
	purple()

elif 'dark fantasy' in query or 'biscuit' in query or 'Brown' in query or 'black' or 'dark brown' in query:
	print('Identified Dark Fantasy')
	brown()

elif 'done' in query: 
	exit()

cv2.imshow("frame", frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
	exit()

cap.release()
cv2.destoryAllWindows()
