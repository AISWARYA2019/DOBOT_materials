# Suction cup/Pneumatic gripper operation
import threading
import DobotDllType as dType
import time as t

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

#Load Dll
api = dType.load()

#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])

if (state == dType.DobotConnect.DobotConnect_NoError):

    #Clean Command Queued
    dType.SetQueuedCmdClear(api)

    #Async Motion Params Setting
    dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 1)
    dType.SetPTPJointParams(api, 50, 50, 50, 50, 50, 50, 50, 50, isQueued = 1)
    dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)

    #Async Home
    dType.SetHOMECmd(api, temp = 0, isQueued = 1)

    #Async PTP Motion
    for i in range(0, 2):            
        #p07 = dType.SetEndEffectorGripper(api,0,1,isQueued = 1)[0]  #ON---0-1
        #p117 = dType.SetEndEffectorGripper(api,1,0,isQueued = 1)[0] 
        #pc = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,xi,yi,85,0,isQueued=1)[0]
        p1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,200,0,85,0,isQueued=0)[0] #A
        p2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,200,-100,85,0,isQueued=0)[0] #B
        p3 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,200,-(100+(i*95)),-40,0,isQueued=0)[0] #C
        p35 = dType.SetEndEffectorSuctionCup(api,1,1,isQueued=0)[0]    # SUCTION CUP HOLD
        #p37 = dType.SetEndEffectorGripper(api,1,1,isQueued = 1)[0] #close---1-1
        p4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,200,-100,85,0,isQueued=0)[0] #B
        #p5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,200,0,85,0,isQueued=1)[0] #A
        p6 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,200,100,85,0,isQueued=0)[0] #D
        p7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,200,100 + (i*95),-40,0,isQueued=0)[0] #E
        p75 = dType.SetEndEffectorSuctionCup(api,0,1,isQueued=1)[0]    # SUCTION CUP release
        #p77 = dType.SetEndEffectorGripper(api,1,0,isQueued = 1)[0]  #open---1-0
        p8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,200,100,85,0,isQueued=0)[0] #D
        p9 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,200,0,85,0,isQueued=0)[0] #A
        #p97 = dType.SetEndEffectorGripper(api,0,0,isQueued = 1)[0]  #OFF ---0-0
        
    #Start to Execute Command Queued
    dType.SetQueuedCmdStartExec(api)

    #while pa > dType.GetQueuedCmdCurrentIndex(api)[0]:
        #posa = dType.GetPose(api)
        #print(" a X: ",int(posa[0])," Y: ",int(posa[1])," Z: ",int(posa[2]))
        #dType.dSleep(100)

    #while pb > dType.GetQueuedCmdCurrentIndex(api)[0]:
        #posb = dType.GetPose(api)
        #print(" b X: ",int(posb[0])," Y: ",int(posb[1])," Z: ",int(posb[2]))
        #dType.dSleep(100)

    while p1 > dType.GetQueuedCmdCurrentIndex(api)[0]:
        pos1 = dType.GetPose(api)
        print(" 1 X: ",int(pos1[0])," Y: ",int(pos1[1])," Z: ",int(pos1[2]))
        #dType.dSleep(100)

    while p2 > dType.GetQueuedCmdCurrentIndex(api)[0]:
        pos2 = dType.GetPose(api)
        print(" 2 X: ",int(pos2[0])," Y: ",int(pos2[1])," Z: ",int(pos2[2]))
        #dType.dSleep(100)

    while p3 > dType.GetQueuedCmdCurrentIndex(api)[0]:
        pos3 = dType.GetPose(api)
        print(" 3 X: ",int(pos3[0])," Y: ",int(pos3[1])," Z: ",int(pos3[2]))
        #dType.dSleep(100)

    while p35 > dType.GetQueuedCmdCurrentIndex(api)[0]:
        pos35 = dType.GetPose(api)
        print(" Suction ON  X: ",int(pos35[0])," Y: ",int(pos35[1])," Z: ",int(pos35[2]))
        #dType.dSleep(100)
        
    while p4 > dType.GetQueuedCmdCurrentIndex(api)[0]:
        pos4 = dType.GetPose(api)
        print(" 4 X: ",int(pos4[0])," Y: ",int(pos4[1])," Z: ",int(pos4[2]))
        #dType.dSleep(100)

    #while p5 > dType.GetQueuedCmdCurrentIndex(api)[0]:
        #pos5 = dType.GetPose(api)
        #print(" 5 X: ",int(pos5[0])," Y: ",int(pos5[1])," Z: ",int(pos5[2]))
        #dType.dSleep(100)

    while p6 > dType.GetQueuedCmdCurrentIndex(api)[0]:
        pos6 = dType.GetPose(api)
        print(" 6 X: ",int(pos6[0])," Y: ",int(pos6[1])," Z: ",int(pos6[2]))
        #dType.dSleep(100)

    while p7 > dType.GetQueuedCmdCurrentIndex(api)[0]:
        pos7 = dType.GetPose(api)
        print(" 7 X: ",int(pos7[0])," Y: ",int(pos7[1])," Z: ",int(pos7[2]))
        #dType.dSleep(100)

    while p75 > dType.GetQueuedCmdCurrentIndex(api)[0]:
        pos75 = dType.GetPose(api)
        print(" Suction OFF X: ",int(pos75[0])," Y: ",int(pos75[1])," Z: ",int(pos75[2]))
        dType.dSleep(50)

    while p8 > dType.GetQueuedCmdCurrentIndex(api)[0]:
        pos8 = dType.GetPose(api)
        print(" 8 X: ",int(pos8[0])," Y: ",int(pos8[1])," Z: ",int(pos8[2]))
        #dType.dSleep(100)

    #Wait for Executing Last Command

    while p9 > dType.GetQueuedCmdCurrentIndex(api)[0]:
        pos9 = dType.GetPose(api)
        print(" 9 X: ",int(pos9[0])," Y: ",int(pos9[1])," Z: ",int(pos9[2]))
        dType.dSleep(50)

    #while p97 > dType.GetQueuedCmdCurrentIndex(api)[0]:
        #pos9 = dType.GetPose(api)
        #print(" 9 X: ",int(pos9[0])," Y: ",int(pos9[1])," Z: ",int(pos9[2]))
        #dType.dSleep(50)

    #Stop to Execute Command Queued
    dType.SetQueuedCmdStopExec(api)

#Disconnect Dobot
dType.DisconnectDobot(api)
