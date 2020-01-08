"""The template of the main script of the machine learning process
"""

import games.pingpong.communication as comm
from games.pingpong.communication import ( \
    SceneInfo, GameStatus, PlatformAction
)
 


def ml_loop(ml_1P):
    """The main loop of the machine learning process

    This loop is run in a separate process, and communicates with the game process.

    Note that the game process won't wait for the ml process to generate the
    GameInstruction. It is possible that the frame of the GameInstruction
    is behind of the current frame in the game process. Try to decrease the fps
    to avoid this situation.
    """

    # === Here is the execution order of the loop === #
    # 1. Put the initialization code here.

    # 2. Inform the game process that ml process is ready before start the loop.
    import pickle
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set_style("whitegrid")
    sns.set_context("paper")
    
    import warnings
    warnings.filterwarnings('ignore') 
    
    path_list = [
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_16-52-32.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_16-57-35.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_16-59-11.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-01-02.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-02-45.pickle",

        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-04-36.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-08-02.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-11-29.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-13-12.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-15-11.pickle",

        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-18-31.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-20-22.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-22-18.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-25-37.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-28-49.pickle",

        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-32-08.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-33-59.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-35-42.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-37-33.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-39-16.pickle",

        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-42-28.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-45-42.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-47-33.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-49-16.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-52-36.pickle",

        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-55-56.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_18-12-12.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_18-15-25.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_18-17-16.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_18-18-59.pickle",

        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_18-20-50.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_22-33-36.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_22-35-30.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_22-37-16.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_22-40-42.pickle",

        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_22-44-01.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_22-48-12.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-23-41.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-25-28.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-27-23.pickle",

        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-29-10.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-32-37.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-34-32.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-36-19.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-38-13.pickle",        

        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-40-00.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-43-26.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-46-45.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-48-40.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-53-47.pickle",

        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-59-01.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-19_00-00-48.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-19_00-02-43.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-19_00-04-30.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-19_00-08-02.pickle"

#        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_22-11-59.pickle",
#        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_22-13-55.pickle",
#        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_22-15-42.pickle"

        ]
    for flie_list in path_list :
        with open(flie_list,"rb") as f :
            data_list = pickle.load(f)


    Frame = []
    Status = []
    Ballposition = []
    PlatformPosition_1P = []
    for i in range(0,len(data_list)):
        Frame.append(data_list[i].frame)
        Status.append(data_list[i].status)
        Ballposition.append(data_list[i].ball)
        PlatformPosition_1P.append(data_list[i].platform_1P)

    np.set_printoptions(threshold=np.inf)
    PlatX = np.array(PlatformPosition_1P)[:,0][:,np.newaxis]
    PlatX_next = PlatX[1:,:]
    instruct = (PlatX_next - PlatX[0:len(PlatX_next),0][:, np.newaxis])//5

    BallX=np.array(Ballposition)[:,0][:,np.newaxis]
    BallX_next=BallX[1:,:]
    vx=(BallX_next-BallX[0:len(BallX_next),0][:,np.newaxis])

    BallY=np.array(Ballposition)[:,1][:,np.newaxis]
    BallY_next=BallY[1:,:]
    vy=(BallY_next-BallY[0:len(BallY_next),0][:,np.newaxis])

    Ballarray = np.array(Ballposition[:-1])

    x = np.hstack((Ballarray , PlatX[0:-1,0][:,np.newaxis],vx,vy))
    y = instruct.flatten()
    print(x)

#    vx = 0
#    vy = 0
#    filename = "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\ml\\knn_1P.sav"
#    model = pickle.load(open(filename,'rb'))
    comm.ml_ready()
    
    
    
    ball_center_record = []

    # 3. Start an endless loop.
    while True:
        # 3.1. Receive the scene information sent from the game process.
        scene_info = comm.get_scene_info()
        ball_center_record.append(scene_info.ball)
        platform_center_1p = scene_info.platform_1P[0]+20
        
        if(len(ball_center_record) > 1):
            vx_new = ball_center_record[-1][0]-ball_center_record[-2][0]
            vy_new = ball_center_record[-1][1]-ball_center_record[-2][1]
            inp_temp=np.array([scene_info.ball[0], scene_info.ball[1], scene_info.platform_1P[0],vx_new,vy_new])
            input = inp_temp[np.newaxis, :]
            
            
        # ball_center_record.append(scene_info.ball)
        # Platform_center_x = scene_info.platform[0]+20
        # if(len(ball_center_record))==1:
        #     ball_going_down = 0
        # elif ball_center_record[-1][1]-ball_center_record[-2][1] > 0:
        #     ball_going_down = 1
        #     vy = ball_center_record[-1][1]-ball_center_record[-2][1]
        #     vx = ball_center_record[-1][0]-ball_center_record[-2][0]
        #     ball_destination = ball_center_record[-1][0]+(395-ball_center_record[-1][1])*vx/vy

        #     while ball_destination < 0 or ball_destination > 200:
        #         if ball_destination >200:
        #             ball_destination = 400-ball_destination
        #         else:
        #             ball_destination =  - ball_destination

        #     if Platform_center_x < ball_destination:
        #         comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
        #     else:
        #         comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT) 
        # else:
        #     bell_going_down = 0 
        #     if Platform_center_x < 100:
        #         comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
        #     else:
        #         comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)                          

        # 3.2. If the game is over or passed, the game process will reset
        #      the scene and wait for ml process doing resetting job.
        # Platform_center_x = scene_info.platform[0]+20
        # inp_temp = np.array([scene_info.ball[0],scene_info.ball[1],scene_info.platform[0]])
        # input = inp_temp[np.newaxis,:]


        if scene_info.status == GameStatus.GAME_1P_WIN or \
           scene_info.status == GameStatus.GAME_2P_WIN:
            # Do some stuff if needed
            #scene_info = comm.get_scene_infso()
            # 3.2.1. Inform the game process that ml process is ready
            comm.ml_ready()
            continue
        if(len(ball_center_record) > 1):            
            move=classify(input, x, y, 3)
        else:
            move=0
        print(move)

        if move < 0:
            comm.send_instruction(scene_info.frame,PlatformAction.MOVE_LEFT)
        elif move > 0:
            comm.send_instruction(scene_info.frame,PlatformAction.MOVE_RIGHT)
        else :
            comm.send_instruction(scene_info.frame,PlatformAction.NONE)

        # 3.3. Put the code here to handle the scene information

        # 3.4. Send the instruction for this frame to the game process

def classify(input, dataSet, label, k):
    import numpy as np
    import operator
    dataSize = dataSet.shape[0]
    ## 重複input為dataSet的大小
    diff = np.tile(input, (dataSize, 1)) - dataSet
    sqdiff = diff**2
    ## 列向量分別相加，得到一列新的向量
    squareDist = np.array([sum(x) for x in sqdiff])
    dist = squareDist**0.5
    
    ## 對距離進行排序
    ## argsort()根據元素的值從大到小對元素進行排序，返回下標
    sortedDistIndex = np.argsort(dist)
    
    classCount = {}
    for i in range(k):
        ## 因為已經對距離進行排序，所以直接迴圈sortedDistIndx
        voteLabel = label[sortedDistIndex[i]]
        ## 對選取的k個樣本所屬的類別個數進行統計
        ## 如果獲取的標籤不在classCount中，返回0
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    ## 選取出現的類別次數最多的類別
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key
    
    return classes
          