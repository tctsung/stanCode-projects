"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics
import random
# Constants
FRAME_RATE = 1000 / 120                                       # 120 frames per second
NUM_LIVES = 3			                                      # Number of attempts


def main():
    """
    There are ___ extensions in this file
    1. score board
    2. randomly change the direction in x-axis every ten points
    3. change the ball direction in x-axis, if the ball hits the left-portion of the paddle, if will go left
       , if the ball hits the right-portion, it will go right
    4. one heart represent one life
    5. The end animation
    """
    add_speed = 1                                             # Times of adding speed
    graphics = BreakoutGraphics()
    ball_x_speed = graphics.ball_x_speed()
    ball_y_speed = graphics.ball_y_speed()
    die = 0                                                   # number of failed times
    perfect_score = graphics.perfect_score()
    while True:
        pause(FRAME_RATE)
        if graphics.game_start():                             # start the game once you click the mouse
            graphics.ball.move(ball_x_speed, ball_y_speed)
            if graphics.ball.y > graphics.window.height-graphics.ball.height:
                die += 1                                      # lose 1 live when hit the ground
                graphics.remove_heart()
                graphics.ball.x = graphics.window.width / 2
                graphics.ball.y = graphics.window.height / 2
                graphics.restart()                            # restart the game once you click the mouse
            if die == NUM_LIVES or graphics.clear_all():      # game over if die > "NUM_LIVE" or all bricks were cleared
                graphics.end()
                break
            # bounce back if the ball is out of window
            if 0 > graphics.ball.x:
                if ball_x_speed < 0:
                    ball_x_speed = -ball_x_speed
            if graphics.ball.x > graphics.window.width-graphics.ball.width:
                if ball_x_speed > 0:
                    ball_x_speed = -ball_x_speed
            if not 0 < graphics.ball.y:
                ball_y_speed = -ball_y_speed

            # if the ball hits a brick, remove the brick and return True
            if graphics.check_ball():
                if graphics.ball.y+graphics.ball.height < graphics.paddle.y+graphics.paddle.height:
                    ball_y_speed = -ball_y_speed
                if graphics.direction == 0:
                    pass
                elif graphics.direction == 1:
                    if ball_x_speed < 0:
                        ball_x_speed = -ball_x_speed
                elif graphics.direction == 2:
                    if ball_x_speed > 0:
                        ball_x_speed = -ball_x_speed
                graphics.direction = 0

            # to switch speed every ten points
            score = graphics.get_score()
            if score > perfect_score*0.1*add_speed:
                graphics.ball.fill_color = (add_speed*22, 100, 100)
                ball_x_speed = random.randint(1, 7)
                add_speed += 1


if __name__ == '__main__':
    main()
