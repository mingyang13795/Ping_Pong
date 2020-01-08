# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 12:13:40 2019

@author: DK
"""

"""
The template of the script for the machine learning process in game pingpong
"""

# Import the necessary modules and classes
import pickle
import games.pingpong.communication as comm
from games.pingpong.communication import (
    SceneInfo,GameStatus, PlatformAction
)
import numpy as np
def predict_1P(ball_x,ball_y,last_ball_x,last_ball_y,speed):
    pre_x = ball_x
    pre_y = ball_y
    if(ball_x - last_ball_x >0):
        delta_x = 1
    else:
        delta_x = -1
    if(ball_y - last_ball_y >0):
        delta_y =  1
    else:
        delta_y = -1
    if(speed < 100):
        while(pre_y<=420):
            if(pre_x == 0 or pre_x == 200):
                delta_x *= -1
            pre_x += delta_x
            pre_y += delta_y
    else:
        while(pre_y<=450):
            if(pre_x == 0 or pre_x == 200):
                delta_x *= -1
            pre_x += delta_x
            pre_y += delta_y
    return pre_x,delta_x,delta_y
def predict_2P(ball_x,ball_y,last_ball_x,last_ball_y,speed):
    pre_x = ball_x
    pre_y = ball_y
    if(ball_x - last_ball_x >0):
        delta_x = 1
    else:
        delta_x = -1
    if(ball_y - last_ball_y >0):
        delta_y =  1
    else:
        delta_y = -1
    if(speed < 100):
        while(pre_y>=80):
            if(pre_x == 0 or pre_x == 200):
                delta_x *= -1
            pre_x += delta_x
            pre_y += delta_y
    else:
        while(pre_y>=50):
            if(pre_x == 0 or pre_x == 200):
                delta_x *= -1
            pre_x += delta_x
            pre_y += delta_y
        
    return pre_x,delta_x,delta_y
def ml_loop(side: str):
    """
    The main loop for the machine learning process

    The `side` parameter can be used for switch the code for either of both sides,
    so you can write the code for both sides in the same script. Such as:
    ```python
    if side == "1P":
        ml_loop_for_1P()
    else:
        ml_loop_for_2P()
    ```

    @param side The side which this script is executed for. Either "1P" or "2P".
    """

    # === Here is the execution order of the loop === #
    # 1. Put the initialization code here
    ball_location = [0,0]
    plat_location = [0,0]

    # 2. Inform the game process that ml process is ready
    comm.ml_ready()

    # 3. Start an endless loop
    if side == "1P":
        #filename = "F:\\Documents\\MachineLearning\\MLGame-master\\knn_test.sav"
		
        filename = "C:\\MLGame-master\\games\\pingpong\\ml\\knn_test.sav"
        model = pickle.load(open(filename,'rb'))
        last_ball_x = 0
        last_ball_y = 0
        comm.ml_ready()
    
        scene_info = comm.get_scene_info()
        while True:
            last_ball_x = scene_info.ball[0]
            last_ball_y = scene_info.ball[1]
            scene_info = comm.get_scene_info()
            plat_cneter_x = scene_info.platform_1P[0]+20
        
            if(last_ball_x - scene_info.ball[0] > 0):
                LR = 1
            else:
                LR = 0
            if(last_ball_y - scene_info.ball[1] > 0):
                UP = 0
            else:
                UP = 1
            inp_temp = np.array([scene_info.ball[0],scene_info.ball[1],LR,UP,scene_info.platform_1P[0]])
            input = inp_temp[np.newaxis,:]
            if scene_info.status == GameStatus.GAME_1P_WIN or \
               scene_info.status == GameStatus.GAME_2P_WIN:
                # Some updating or reseting code here
                comm.ml_ready()
                continue
            move = model.predict(input)
            if(move<0):
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            elif(move>0):
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            else:
                comm.send_instruction(scene_info.frame, PlatformAction.NONE)
#        # 3.1. Receive the scene information sent from the game process.
#            scene_info = comm.get_scene_info()
#            if(scene_info.frame == 0):
#                print(scene_info.ball)    		
#            # 3.2. If the game is over or passed, the game process will reset
#            #      the scene and wait for ml process doing resetting job.
#            
#            last_ball_location = ball_location
#            ball_location = scene_info.ball
#            plat_location = scene_info.platform_1P 
#            if scene_info.status == GameStatus.GAME_1P_WIN or \
#               scene_info.status == GameStatus.GAME_2P_WIN:
#                # Some updating or reseting code here
#                comm.ml_ready()
#                continue
#            
#            if(int(ball_location[0]) + int(ball_location[1]) != 0):
#                if(int(ball_location[1]) - int(last_ball_location[1]) > 0):
#                    # go to 1P
#                        
#                    next_x,delta_x,delta_y = predict_1P(ball_location[0],ball_location[1] \
#                                        ,last_ball_location[0],last_ball_location[1],scene_info.ball_speed)
#
#                else:
#                    next_x,delta_x,delta_y = predict_2P(ball_location[0],ball_location[1] \
#                                        ,last_ball_location[0],last_ball_location[1],15)
#                    next_x,delta_x,delta_y = predict_1P(next_x + 7*delta_x ,80 + delta_y*-1 \
#                                        ,next_x,80,scene_info.ball_speed)
#                     
#            if( next_x%5 > 2.5):
#                next_x = next_x + (5 - next_x%5)
#            else:
#                next_x = next_x  - next_x%5
#                
#
#            # 3.3 Put the code here to handle the scene information
#            # 3.4 Send the instruction for this frame to the game process
#            if(int(plat_location[0])+20>next_x):
#                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
#            elif(int(plat_location[0])+20<next_x):
#                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
#            else:
#                comm.send_instruction(scene_info.frame, PlatformAction.NONE)
    
    
    
    #2P------------------------------------------------------------------------------------------
    
    
    else:
        while True:
        # 3.1. Receive the scene information sent from the game process.
            scene_info = comm.get_scene_info()
    		
            # 3.2. If the game is over or passed, the game process will reset
            #      the scene and wait for ml process doing resetting job.
            if scene_info.status == GameStatus.GAME_1P_WIN or \
               scene_info.status == GameStatus.GAME_2P_WIN:
                # Some updating or reseting code here
                comm.ml_ready()
                continue
            last_ball_location = ball_location
            ball_location = scene_info.ball
            plat_location = scene_info.platform_2P 
            
            
            if(int(ball_location[0]) + int(ball_location[1]) != 0):
                if(int(ball_location[1]) - int(last_ball_location[1]) > 0):
                    # go to 1P
                    next_x,delta_x,delta_y = predict_1P(ball_location[0],ball_location[1] \
                                        ,last_ball_location[0],last_ball_location[1],18)
                    next_x,delta_x,delta_y = predict_2P(next_x + 7*delta_x ,420 + delta_y*-1 \
                                        ,next_x,420,scene_info.ball_speed)
                    
                else:
                    # go to 2P
                    next_x,delta_x,delta_y = predict_2P(ball_location[0],ball_location[1] \
                                        ,last_ball_location[0],last_ball_location[1],scene_info.ball_speed)



                   
                    
            if( next_x%5 > 2.5):
                next_x = next_x + (5 - next_x%5)
            else:
                next_x = next_x  - next_x%5


            # 3.3 Put the code here to handle the scene information
            # 3.4 Send the instruction for this frame to the game process
            if(int(plat_location[0])+20>next_x):
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            elif(int(plat_location[0])+20<next_x):
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            else:
                comm.send_instruction(scene_info.frame, PlatformAction.NONE)
    
    
