import threading
import DobotDllType as dType
import time as t
CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

#Load Dll
api = dType.load()
dobot_coord = []


#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])

if (state == dType.DobotConnect.DobotConnect_NoError):
    print("Entering if")
    #Clean Command Queued
    dType.SetQueuedCmdClear(api)
    current_pose = dType.GetPose(api)
    #Async Motion Params Setting
    dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 0)
    dType.SetPTPJointParams(api, 100, 100, 100, 100, 100, 100, 100, 100, isQueued = 0)
    dType.SetPTPCommonParams(api, 100, 100, isQueued = 0)   
    with open('coordinates_voice.txt', 'r') as filehandle:
        for line in filehandle:
            dobot_coord.append(line[:-1])

    print(dobot_coord[0], dobot_coord[1])
    
    t.sleep(3)
    
    p1 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,float(dobot_coord[0]),float(dobot_coord[1]),0,0,isQueued=0)
    print("completed p1")
    t.sleep(1)
    p2 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,float(dobot_coord[0]),float(dobot_coord[1]),-75,0,isQueued=0)
    print("completed p2")
    t.sleep(3)
    p3 = dType.SetEndEffectorSuctionCup(api,1,1,isQueued=1)[0]    # SUCTION CUP HOLD
    print("completed p3")
    t.sleep(2)
    p4 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,float(dobot_coord[0]),float(dobot_coord[1]),70,0,isQueued=0)
    t.sleep(2)
    print("completed p4")
    p5 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,176, 227, 100,-50,isQueued=0)
    print("completed p5")
    t.sleep(1)
    p6 = dType.SetEndEffectorSuctionCup(api,0,1,isQueued=0)[0]    # SUCTION CUP release
    print("completed p6")
    t.sleep(1)
    p7 = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode,22, -214, 100,0,isQueued=0)
    
    
dType.DisconnectDobot(api)
