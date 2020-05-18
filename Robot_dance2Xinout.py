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
yc = 50
zc = 50

if (state == dType.DobotConnect.DobotConnect_NoError):
    print("Entering loop")
    #Clean Command Queued
    dType.SetQueuedCmdClear(api)

    #Async Motion Params Setting
    dType.SetHOMEParams(api, xo, 0, 0, 0, isQueued = 0) #centre
    dType.SetPTPJointParams(api, 100, 100, 100, 100, 100, 100, 100, 100, isQueued = 0)
    dType.SetPTPCommonParams(api, 100, 100, isQueued = 0)

    #comment this to save time
    dType.SetHOMECmd(api, temp = 0, isQueued = 1)

    for i in range (0, 3):
        po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,-yc,zc,0,isQueued=0) #\ left diagonal up
        po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo+50,-yc,zc,0,isQueued=0) #\ left diagonal up FWD
        po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,-yc,zc,0,isQueued=0) #\ left diagonal up BCK
        
        po8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,yc,-zc,0,isQueued=0) #\ left diagonal down
        po8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo+50,yc,-zc,0,isQueued=0) #\ left diagonal down FWD
        po8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,yc,-zc,0,isQueued=0) #\ left diagonal down BCK
        
        po8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,0,0,0,isQueued=0) #centre
        
        po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,yc,zc,0,isQueued=0) #/ right diagonal up
        po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo+50,yc,zc,0,isQueued=0) #/ right diagonal up FWD
        po7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,yc,zc,0,isQueued=0) #/ right diagonal up BCK
        
        po8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,-yc,-zc,0,isQueued=0) #/ right diagonal down
        po8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo+50,-yc,-zc,0,isQueued=0) #/ right diagonal down FWD
        po8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,-yc,-zc,0,isQueued=0) #/ right diagonal down BCK
        
        po8 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,xo,0,0,0,isQueued=0) #centre
        print("WELCOME!!!")
      # t.sleep(2)

#Disconnect Dobot
dType.DisconnectDobot(api)
