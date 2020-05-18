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

xoff = 200
zc = 0
rd = 50

if (state == dType.DobotConnect.DobotConnect_NoError):
    print("Entering loop")
    #Clean Command Queued
    dType.SetQueuedCmdClear(api)

    #Async Motion Params Setting
    dType.SetHOMEParams(api, xoff, 0, zc, 0, isQueued = 0) #centre
    dType.SetPTPJointParams(api, 100, 100, 100, 100, 100, 100, 100, 100, isQueued = 0)
    dType.SetPTPCommonParams(api, 90, 90, isQueued = 0)

    #comment this to save time
    #dType.SetHOMECmd(api, temp = 0, isQueued = 1)

    p1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xoff,0,zc-rd,0,isQueued=0) #[1]
    for i in range (0, 3):
        po3 = dType.SetARCCmd(api,[xoff,-rd,zc,0],[xoff,0,zc+rd,0],isQueued=0) #( fv
        po4 = dType.SetARCCmd(api,[xoff,rd,zc,0],[xoff,0,zc-rd,0],isQueued=0) #) fv
        po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xoff,-rd,zc+rd,0,isQueued=0) #\ left go up
        po8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xoff,0,zc-rd,0,isQueued=0) #\ left come back
        po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xoff,rd,zc+rd,0,isQueued=0) #/ right go up
        po8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xoff,0,zc-rd,0,isQueued=0) #/ right come back
        print("WELCOME!!!")
      # t.sleep(2)

#Disconnect Dobot
dType.DisconnectDobot(api)
