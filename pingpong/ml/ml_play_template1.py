"""
The template of the script for the machine learning process in game pingpong
"""

# Import the necessary modules and classes
import games.pingpong.communication as comm
from games.pingpong.communication import (
    SceneInfo, GameStatus, PlatformAction
)

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
    ball_center_record = []
    ball_speed_record = []
    #me_hit_x _record = []
    #opponent_strike_back_x_record = []
    state = 0
    me_hit_x = 0
    me_next_hit_x = 0
    opponent_strike_back_x = 0
    
    UP_or_DOWN = 0
    init_ballx = 0
    init_bally = 0
    
    left_height = 0
    right_height = 0
    
    lx=0
    ly=0
    rx=0
    ry=0
    # 2. Inform the game process that ml process is ready
    comm.ml_ready()

    # 3. Start an endless loop
    while True:
        # 3.1. Receive the scene information sent from the game process
        scene_info = comm.get_scene_info()
        ball_center_record.append(scene_info.ball)
        ball_speed_record.append(scene_info.ball_speed)
        ball_x = scene_info.ball[0]
        ball_y = scene_info.ball[1]
        ball_speed =  scene_info.ball_speed
        #print(ball_speed)
        print(scene_info.ball)
        platform_center_1P=  scene_info.platform_1P[0]+20
        platform_center_2P=  scene_info.platform_2P[0]+20
        #platform_1P_height =  scene_info.platform_1P[1]-5       #1p平板擊球左上角高度 default=420-5
        #platform_2P_height =  scene_info.platform_2P[1]+30     #2p平板擊球左上角高度default=50+30
        # 3.2. If either of two sides wins the game, do the updating or
        #      resetting stuff and inform the game process wh`12wEen the ml process
        #      is ready.
        if scene_info.status == GameStatus.GAME_1P_WIN or \
           scene_info.status == GameStatus.GAME_2P_WIN:
            # Do some updating or resetting stuff
            state = state_list[0]
            # 3.2.1 Inform the game process that
            #       the ml process is ready for the next round
            comm.ml_ready()
            continue

        # 3.3 Put the code here to handle the scene information
        # 3.4 Send the instruction for this frame to the game process
        if state == 0:
            if  ball_center_record[-1][1] < ball_y: #球往下
                UP_or_DOWN = 1
                init_ballx = ball_x
                init_bally = ball_y
            elif ball_center_record[-1][1] > ball_y:#球往上
                UP_or_DOWN = 0
                init_ballx = ball_x
                init_bally = ball_y
                pass
            pass
            
        elif state == 1:        
            if platform_center_1P < me_hit_x :
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            elif platform_center_2P > me_hit_x:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                pass
            pass
            
        elif state  == 2:
            
            pass
            
    ############################################################################
    if state ==0:
        if UP_or_DOWN == 0:
            
        elif UP_or_DOWN == 1:
            
    elif state == 1:
        
    elif: state == 2:
        
