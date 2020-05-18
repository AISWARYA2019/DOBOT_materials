# VERTICAL ZIG-ZAG in YZ plane

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

xo = 200
ry = 10
rz = -50

if (state == dType.DobotConnect.DobotConnect_NoError):
    print("Entering loop")
    #Clean Command Queued
    dType.SetQueuedCmdClear(api)

    #Async Motion Params Setting
    dType.SetHOMEParams(api, xoff, 0, zc, 0, isQueued = 0) #centre
    dType.SetPTPJointParams(api, 100, 100, 100, 100, 100, 100, 100, 100, isQueued = 0)
    dType.SetPTPCommonParams(api, 100, 100, isQueued = 0)

    #comment this to save time&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&   comment to save time
    dType.SetHOMECmd(api, temp = 0, isQueued = 1)

    for i in range (0, 11): #down to up
        if i%2==0:
            po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,ry,rz+(i*10),0,isQueued=0)
        else:
            po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,-ry,rz+(i*10),0,isQueued=0)

    for i in range (0, 10): #up to down
        if i%2==0:
            po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,ry,rz+((10-i)*10),0,isQueued=0)
        else:
            po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,-ry,rz+((10-i)*10),0,isQueued=0)

#Disconnect Dobot
dType.DisconnectDobot(api)