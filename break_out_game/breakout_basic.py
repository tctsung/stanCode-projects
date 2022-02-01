"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120                                       # 120 frames per second
NUM_LIVES = 3			                                      # Number of attempts


def main():
    graphics = BreakoutGraphics()
    ball_x_speed = graphics.ball_x_speed()
    ball_y_speed = graphics.ball_y_speed()
    die = 0                                                   # number of failed times
    while True:
        pause(FRAME_RATE)
        if graphics.game_start():                             # start the game once you click the mouse
            graphics.ball.move(ball_x_speed, ball_y_speed)
            if graphics.ball.y > graphics.window.height-graphics.ball.height:
                die += 1                                      # lose 1 live when hit the ground
                graphics.ball.x = graphics.window.width / 2
                graphics.ball.y = graphics.window.height / 2
                graphics.restart()                            # restart the game once you click the mouse
            if die == NUM_LIVES or graphics.clear_all():      # game over if die > "NUM_LIVE" or all bricks were cleared
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
            # because the ball may hit two bricks at the same time, 4 sensor were set
            if graphics.check_ball():
                ball_y_speed = -ball_y_speed


if __name__ == '__main__':
    main()
