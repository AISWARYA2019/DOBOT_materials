import cv2
import numpy as np
import imutils


cap = cv2.VideoCapture(0)

#Setting resolution
cap.set(3,640)
cap.set(4,480)

while True:

    _,frame = cap.read()
    hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)

    ret, frame = cap.read()  # capture the image

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert BGR to HSV

    lower_purple = np.array([159, 113, 91])
    upper_purple = np.array([180, 255, 255])

    lower_yellow = np.array([25, 45, 120])
    upper_yellow = np.array([40, 255, 255])

    lower_red = np.array([0, 53, 0])
    upper_red = np.array([6, 255, 255])
    
    lower_blue = np.array([90, 60, 120])
    upper_blue = np.array([121, 255, 255])
    
    lower_dark_brown = np.array([0,0,0])
    upper_dark_brown = np.array([53, 181,89])

    mask1 = cv2.inRange(hsv_frame, lower_blue, upper_blue)  # mask for blue
    mask2 =cv2.inRange(hsv_frame, lower_yellow, upper_yellow) #mask for yellow
    mask3 = cv2.inRange(hsv_frame, lower_red, upper_red)
    mask4 = cv2.inRange(hsv_frame, lower_dark_brown, upper_dark_brown)
    mask5 = cv2.inRange(hsv_frame, lower_purple, upper_purple)

    blue = cv2.bitwise_and(frame, frame, mask=mask1)
    yellow = cv2.bitwise_and(frame, frame, mask= mask2)
    red = cv2.bitwise_and(frame,frame,mask = mask3)
    dark_brown = cv2.bitwise_and(frame,frame,mask = mask4)
    purple = cv2.bitwise_and(frame,frame,mask = mask5)

    cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = imutils.grab_contours(cnts2)

    cnts1 = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts1 = imutils.grab_contours(cnts1)

    cnts3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts3 = imutils.grab_contours(cnts3)

    cnts4 = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts4 = imutils.grab_contours(cnts4)

    cnts5 = cv2.findContours(mask5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts5 = imutils.grab_contours(cnts5)


    for c in cnts1:
        area1 = cv2.contourArea(c)
        if area1 > 1000:
            cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx_1 = int(M["m10"] / M["m00"])
            cy_1 = int(M["m01"] / M["m00"])
            cv2.circle(frame,(cx_1,cy_1),7,(255,0,0),-1)
            cv2.putText(frame,"Orbit Blue", (cx_1-20, cy_1-20), cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),2)
            #print("area is :", area1)
            #print("centroid is at :",cx,cy)
            if cv2.waitKey(1) & 0xFF == ord('b'):
                cam_cord = [cx_1, cy_1]

                #print(coordinates)
                dobot_cord_x = 0.5426*cam_cord[0]+146.98 
                dobot_cord_y = -0.6249*cam_cord[1]+208.54
                dobot_cord = (dobot_cord_x, dobot_cord_y)
                # print(cam_cord[2])
                with open('coordinates_orbit_blue.txt', 'w') as file:
                    for listitem in dobot_cord:
                        file.write('%d\n' % listitem)
                print('stored blue orbit coordinates')



    for c in cnts2:
        area2 = cv2.contourArea(c)
        if area2 > 1000:
            cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx_2 = int(M["m10"] / M["m00"])
            cy_2 = int(M["m01"] / M["m00"])
            cv2.circle(frame,(cx_2,cy_2),7,(255,0,0),-1)
            cv2.putText(frame,"Orbit Yellow", (cx_2-20, cy_2-20), cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),2)
            #print("area is :", area2)
            #print("centroid is at :",cx,cy)
            if cv2.waitKey(1) & 0xFF == ord('y'):
                cam_cord = [cx_2, cy_2]

                #print(coordinates)
                dobot_cord_x = 0.5426*cam_cord[0]+146.98 
                dobot_cord_y = -0.6249*cam_cord[1]+208.54
                dobot_cord_yellow = (dobot_cord_x, dobot_cord_y)
                # print(cam_cord[2])
                with open('coordinates_orbit_yellow.txt', 'w') as file:
                    for listitem in dobot_cord_yellow:
                        file.write('%d\n' % listitem)
                print('stored yellow orbit coordinates')

                exit()

    for c in cnts3:
        area3 = cv2.contourArea(c)
        if area3 > 1000:
            cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx_3 = int(M["m10"] / M["m00"])
            cy_3 = int(M["m01"] / M["m00"])
            cv2.circle(frame,(cx_3,cy_3),7,(255,0,0),-1)
            cv2.putText(frame,"KitKat", (cx_3-20, cy_3-20), cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),2)
            #print("area is :", area2)
            #print("centroid is at :",cx,cy)
            if cv2.waitKey(1) & 0xFF == ord('r'):
                cam_cord = [cx_3, cy_3]

                #print(coordinates)
                dobot_cord_x = 0.5426*cam_cord[0]+146.98 
                dobot_cord_y = -0.6249*cam_cord[1]+208.54
                dobot_cord_red = (dobot_cord_x, dobot_cord_y)
                # print(cam_cord[2])
                with open('coordinates_orbit_red.txt', 'w') as file:
                    for listitem in dobot_cord_red:
                        file.write('%d\n' % listitem)
                print('stored KitKat coordinates')

    for c in cnts4:
        area4 = cv2.contourArea(c)
        if area4 > 500:
            cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx_4 = int(M["m10"] / M["m00"])
            cy_4 = int(M["m01"] / M["m00"])
            cv2.circle(frame,(cx_4,cy_4),7,(255,0,0),-1)
            cv2.putText(frame,"Dark Fantasy", (cx_4-20, cy_4-20), cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),2)
            #print("area is :", area2)
            #print("centroid is at :",cx,cy)
            if cv2.waitKey(1) & 0xFF == ord('r'):
                cam_cord = [cx_4, cy_4]

                #print(coordinates)
                dobot_cord_x = 0.5426*cam_cord[0]+146.98 
                dobot_cord_y = -0.6249*cam_cord[1]+208.54
                dobot_cord_red = (dobot_cord_x, dobot_cord_y)
                # print(cam_cord[2])
                with open('coordinates_orbit_red.txt', 'w') as file:
                    for listitem in dobot_cord_red:
                        file.write('%d\n' % listitem)
                print('stored Dark_Fantasy coordinates')

    for c in cnts5:
        area5 = cv2.contourArea(c)
        if area5 > 200:
            cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx_5 = int(M["m10"] / M["m00"])
            cy_5 = int(M["m01"] / M["m00"])
            cv2.circle(frame,(cx_5,cy_5),7,(255,0,0),-1)
            cv2.putText(frame,"Boomer", (cx_5-20, cy_5-20), cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),2)
            #print("area is :", area2)
            #print("centroid is at :",cx,cy)
            if cv2.waitKey(1) & 0xFF == ord('r'):
                cam_cord = [cx_5, cy_5]

                #print(coordinates)
                dobot_cord_x = 0.5426*cam_cord[0]+146.98 
                dobot_cord_y = -0.6249*cam_cord[1]+208.54
                dobot_cord_red = (dobot_cord_x, dobot_cord_y)
                # print(cam_cord[2])
                with open('coordinates_orbit_red.txt', 'w') as file:
                    for listitem in dobot_cord_red:
                        file.write('%d\n' % listitem)
                print('stored Boomer coordinates')
    cv2.imshow("frame", frame)
        # cv2.imshow("mask", yellow)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destoryAllWindows()
