"""The template of the main script of the machine learning process
"""

import games.pingpong.communication as comm
from games.pingpong.communication import ( \
    SceneInfo, GameStatus, PlatformAction
)
 


def ml_loop(ml_2P):
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
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_16-50-55_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_16-54-08_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_16-55-44_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-06-11_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-09-38_2P.pickle",
         
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-16-48_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-23-54_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-27-13_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-30-26_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-40-52_2P.pickle",
         
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-44-06_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-50-53_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_17-54-13_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_18-10-29_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_18-13-49_2P.pickle",
  
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_22-30-18_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_22-31-57_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_22-38-56_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_22-42-21_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-30-50_2P.pickle",

        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-41-39_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-45-06_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-50-19_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-52-00_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_23-53-19_2P.pickle",

        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-55-27_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-18_23-57-06_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-19_00-06-14_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_22-10-13_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_22-43-10_2P.pickle",

        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_22-44-51_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_22-46-34_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_22-48-15_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_22-55-20_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_23-13-35_2P.pickle",
 
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_23-15-16_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_23-16-57_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_23-27-51_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_23-40-50_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_23-46-10_2P.pickle",
         
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_23-53-19_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_23-55-00_2P.pickle", 
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-23_23-56-42_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-24_00-07-38_2P.pickle", 
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-24_00-10-59_2P.pickle",
         
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-24_00-16-25_2P.pickle", 
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-24_00-18-07_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-24_00-21-31_2P.pickle",        
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-24_00-25-01_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-24_00-30-27_2P.pickle",
         
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-24_00-32-09_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-24_00-35-38_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-24_00-52-01_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-24_00-53-43_2P.pickle",
        "C:\\Users\\B510\\Downloads\\MLGame-master (1)\\games\\pingpong\\log\\2019-12-24_00-57-06_2P.pickle"

        #"C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-24_00-58-47_2P.pickle",
        #"C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-24_01-00-29_2P.pickle",
        #"C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-24_01-05-49_2P.pickle"




        ]
    for flie_list in path_list :
        with open(flie_list,"rb") as f :
            data_list = pickle.load(f)


    Frame = []
    Status = []
    Ballposition = []
    PlatformPosition_2P = []
    for i in range(0,len(data_list)):
        Frame.append(data_list[i].frame)
        Status.append(data_list[i].status)
        Ballposition.append(data_list[i].ball)
        PlatformPosition_2P.append(data_list[i].platform_2P)

    np.set_printoptions(threshold=np.inf)
    PlatX = np.array(PlatformPosition_2P)[:,0][:,np.newaxis]
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
        platform_center_2p = scene_info.platform_2P[0]+20
        
        if(len(ball_center_record) > 1):
            vx_new = ball_center_record[-1][0]-ball_center_record[-2][0]
            vy_new = ball_center_record[-1][1]-ball_center_record[-2][1]
            inp_temp=np.array([scene_info.ball[0], scene_info.ball[1], scene_info.platform_2P[0],vx_new,vy_new])
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
          