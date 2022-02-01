"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constants
BRICK_SPACING = 5       # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40        # Height of a brick (in pixels).
BRICK_HEIGHT = 15       # Height of a brick (in pixels).
BRICK_ROWS = 10         # Number of rows of bricks.
BRICK_COLS = 10         # Number of columns of bricks.
BRICK_OFFSET = 50       # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10        # Radius of the ball (in pixels).
PADDLE_WIDTH = 75       # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15      # Height of the paddle (in pixels).
PADDLE_OFFSET = 50      # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7     # Initial vertical speed for the ball.
MAX_X_SPEED = 5         # Maximum initial horizontal speed for the ball.

# global variable
click_time = 0          #
break_count = 0


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.__start = False
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
        # Initialize our mouse listeners
        onmouseclicked(self.count_click)
        onmousemoved(self.paddle_move)
        # Draw bricks
        self.b_col = brick_cols
        self.b_row = brick_rows
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                r = 255-int((j+i)*255/(brick_rows+brick_height))
                # create a smooth color gradient
                brick.color = brick.fill_color = (0, r, 180)
                self.window.add(brick, x=j*(brick_width+brick_spacing), y=BRICK_OFFSET+i*(brick_height+brick_spacing))
        self.__break_count = 0

    def clear_all(self):
        """
        This method will return True and end the game if all bricks are cleared
        :return: boolean, the answer of whether the bricks are cleared
        """
        if self.__break_count == self.b_row * self.b_col:
            return True
        return False

    # the four methods below are similar but simply checking different position of the ball:
    def check_ball(self):
        """
                This method will check whether the ball bump into a brick or paddle
                :return: boolean, hit sth or not
                """
        brick_tl = self.window.get_object_at(self.ball.x, self.ball.y)
        brick_tr = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        brick_bl = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        brick_br = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if BRICK_OFFSET < self.ball.y:  # avoid removing the score board and hearts
            if brick_tl:
                if brick_tl is not self.paddle:
                    self.window.remove(brick_tl)
                return True
            elif brick_tr:
                if brick_tr is not self.paddle:
                    self.window.remove(brick_tr)
                return True
            elif brick_bl:
                if brick_bl is not self.paddle:
                    self.window.remove(brick_bl)
                return True
            elif brick_br:
                if brick_br is not self.paddle:
                    self.window.remove(brick_br)
                return True
        return False

    def restart(self):
        """
        This method clears the mouseclick number, therefore once you click the mouse again, the game will restart
        """
        global click_time
        click_time = 0

    def game_start(self):
        """
        This methods will detect the first click of the player and start the game
        :return: boolean, the program will start the game if return True
        """
        global click_time
        if click_time >= 1:
            return True
        return False

    def count_click(self, m):
        """
        This method will count the number of mouse click event
        :param m: MouseEvent, contain the information of the mouseclick
        """
        global click_time
        click_time += 1

    def paddle_move(self, m):
        """
        This method will help the paddle move in X-axis with the mouse
        :param m: MouseEvent, contain the information of the moving mouse
        """
        if self.paddle.width/2 <= m.x <= self.window.width-self.paddle.width/2:
            self.paddle.x = m.x - self.paddle.width/2

    # getters
    def ball_x_speed(self):
        """
        :return: int, the speed of the ball toward X-axis
        """
        return self.__dx

    def ball_y_speed(self):
        """
        :return: int, the speed of the ball toward Y-axis
        """
        return self.__dy
