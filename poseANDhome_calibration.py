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
    dType.SetHOMEParams(api, 250, 150, 0, 0, isQueued = 1)
    dType.SetPTPJointParams(api, 100, 100, 100, 100, 100, 100, 100, 100, isQueued = 1)
    dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)
    #Async Home
    dType.SetHOMECmd(api, temp = 0, isQueued = 1)
    while 1:
        pos = dType.GetPose(api)
        print(int(pos[0]),", ",int(pos[1]),", ",int(pos[2]))
        t.sleep(1)
        
#Disconnect Dobot
dType.DisconnectDobot(api)
