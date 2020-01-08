"""
The template of the script for the machine learning process in game pingpong
"""
import math
import pickle
# Import the necessary modules and classes
import games.pingpong.communication as comm
from games.pingpong.communication import ( \
    SceneInfo, GameStatus, PlatformAction
)
import numpy as np

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
    filename = "C:\\Users\\Student\\Desktop\\MLGame-master\\games\\pingpong\\my_tree_1P.sav"
    model = pickle.load(open(filename,'rb'))
    filename = "C:\\Users\\Student\\Desktop\\MLGame-master\\games\\pingpong\\my_tree_2P.sav"
    model_2P = pickle.load(open(filename,'rb'))

    
    ball_location = [0,0]
    
    # 2. Inform the game process that ml process is ready
    comm.ml_ready()
    scene_info = comm.get_scene_info()
    
    # 3. Start an endless loop
    if side == "1P":
        while True:
            last_ball_location = ball_location
            
            ball_location = scene_info.ball
            scene_info = comm.get_scene_info()
            if scene_info.status == GameStatus.GAME_1P_WIN or \
               scene_info.status == GameStatus.GAME_2P_WIN:
                # Some updating or reseting code here
                comm.ml_ready()
                continue
            if(int(last_ball_location[1]) - int(ball_location[1]) < 0):
                    # go to down
                if(int(last_ball_location[0]) - int(ball_location[0]) < 0):
                           #go RD
                    LRUP = 2
                else:
                    LRUP = 1
                            #go LD
            else:
                    #upping
                if(int(last_ball_location[0]) - int(ball_location[0]) < 0):
                           #go RU
                    LRUP = 4
                else:
                    LRUP = 3
                            #go LU

            inp_temp = [scene_info.ball[0],scene_info.ball[1],LRUP, \
                                 (200 - int(scene_info.ball[0]))]

            move = str(model.classify_test(inp_temp))
#            print(inp_temp)
#            print(move)
            try:
                ans = move[1:3]
                ans = int(ans) *10
            except:
                ans = move[1:2]
                ans = int(ans) *10
        
            if(scene_info.platform_1P[0] +20 > ans):
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            elif(scene_info.platform_1P[0] +20 < ans):
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            else:
                comm.send_instruction(scene_info.frame, PlatformAction.NONE)

    else:
#        2P

        while True:
            last_ball_location = ball_location
            scene_info = comm.get_scene_info()
            ball_location = scene_info.ball
            
            if scene_info.status == GameStatus.GAME_1P_WIN or \
               scene_info.status == GameStatus.GAME_2P_WIN:
                # Some updating or reseting code here
                comm.ml_ready()
                continue
            if(int(last_ball_location[1]) - int(ball_location[1]) > 0):
                    # go to up
                    
                if(int(last_ball_location[0]) - int(ball_location[0]) > 0):
                           #go LU
                    LRUP = 1
                else:
                    LRUP = 2
                            #go RU
            else:
                    #down
                if(int(last_ball_location[0]) - int(ball_location[0]) > 0):
                           #go LD
                    LRUP = 3
                else:
                    LRUP = 4
                            #go RD
              
        
            inp_temp = [scene_info.ball[0],scene_info.ball[1],LRUP, \
                                 (200 - int(scene_info.ball[0]))]
            move = str(model_2P.classify_test(inp_temp))
#            print(inp_temp)
#            print(move)
            try:
                ans = move[1:3]
                ans = int(ans) *10
            except:
                ans = move[1:2]
                ans = int(ans) *10
            if(ans<50 and scene_info.ball_speed == 21 ):
#                print('move')
                ans += 10
            if(scene_info.platform_2P[0] +20 > ans):
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            elif(scene_info.platform_2P[0] +20 < ans):
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            else:
                comm.send_instruction(scene_info.frame, PlatformAction.NONE)
    
    
