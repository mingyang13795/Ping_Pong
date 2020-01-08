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
        print(scene_info.ball)
        platform_center_1P=  scene_info.platform_1P[0]+20
        platform_center_2P=  scene_info.platform_2P[0]+20
        platform_1P_height =  scene_info.platform_1P[1]-5       #1p平板擊球左上角高度 default=420-5
        platform_2P_height =  scene_info.platform_2P[1]+30     #2p平板擊球左上角高度default=50+30

        # 3.2. If either of two sides wins the game, do the updating or
        #      resetting stuff and inform the game process when the ml process
        #      is ready.
        if scene_info.status == GameStatus.GAME_1P_WIN or \
           scene_info.status == GameStatus.GAME_2P_WIN:
            # Do some updating or resetting stuff

            # 3.2.1 Inform the game process that
            #       the ml process is ready for the next round
            comm.ml_ready()
            continue

        # 3.3 Put the code here to handle the scene information

        # 3.4 Send the instruction for this frame to the game process
        if ball_y<= 250:
            if ball_x > 100:
                if platform_center_1P < 50 :
                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                elif platform_center_1P > 50   :
                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                pass
            elif ball_x < 100: 
                if platform_center_1P < 150    :
                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                elif platform_center_1P > 150  : 
                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                pass
            pass
        elif ball_y>= 250:
            if platform_center_1P < ball_x:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            elif platform_center_1P > ball_x:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            pass
        pass 
        if  ball_center_record[-1][0] < ball_x:#往右
            右高: ((1+(195-ball_x//ball_speed))*ball_speed)
            左高: