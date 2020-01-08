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
    # 2. Inform the game process that ml process is ready
    comm.ml_ready()

    # 3. Start an endless loop
    while True:
        # 3.1. Receive the scene information sent from the game process
        scene_info = comm.get_scene_info()
        ball_center_record.append(scene_info.ball)
        ball_speed =  scene_info.ball_speed
        platform_center_1p = scene_info.platform_1P[0]+20
        platform_center_2p = scene_info.platform_2P[0]+20
    
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
        if(len(ball_center_record))==1:
            ball_going_down = 0
        elif ball_center_record[-1][1]-ball_center_record[-2][1] < 0:
            ball_going_down = 1

            vx = ball_center_record[-1][0] - ball_center_record[-2][0]
            vy = ball_center_record[-1][1] - ball_center_record[-2][1]
            ball_position_pridictonplatform = ball_center_record[-1][0] +(80-ball_center_record[-1][1])*vx/vy

            while ball_position_pridictonplatform < 0 or ball_position_pridictonplatform > 200:

                if ball_position_pridictonplatform > 200:
                    ball_position_pridictonplatform = 400 - ball_position_pridictonplatform
                else:
                    ball_position_pridictonplatform = -ball_position_pridictonplatform
                pass

            if platform_center_2p < ball_position_pridictonplatform:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            elif platform_center_2p > ball_position_pridictonplatform:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            else:
                continue
        else:
            ball_going_down = 0

            if platform_center_2p < 100:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            elif platform_center_2p > 100:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            else:
                continue
            
        # 3.4 Send the instruction for this frame to the game process
        
