# PENDULUM in YZ plane

import threading
import DobotDllType as dType
import time as t

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

#Load Dll
api = dType.load()

xo = 200

#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])

if (state == dType.DobotConnect.DobotConnect_NoError):
    print("Entering loop")
    #Clean Command Queued
    dType.SetQueuedCmdClear(api)

    #Async Motion Params Setting
    dType.SetHOMEParams(api, xoff, 0, zc, 0, isQueued = 0) #centre
    dType.SetPTPJointParams(api, 100, 100, 100, 100, 100, 100, 100, 100, isQueued = 0)
    dType.SetPTPCommonParams(api, 100, 100, isQueued = 0)

    #comment this to save time <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< comment this line to save time
    dType.SetHOMECmd(api, temp = 0, isQueued = 1)

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
    
#Disconnect Dobot
dType.DisconnectDobot(api)
