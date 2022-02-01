"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
-----
Author: Ching-Tsung Tsai (Deron)
This is the extension version of my breakout game, containing three special bricks
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

# Constants
BRICK_SPACING = 5       # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40        # Height of a brick (in pixels).
BRICK_HEIGHT = 15       # Height of a brick (in pixels).
BRICK_ROWS = 10         # Number of rows of bricks.
BRICK_COLS = 10         # Number of columns of bricks.
BRICK_OFFSET = 50       # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 12        # Radius of the ball (in pixels).
PADDLE_WIDTH = 100       # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15      # Height of the paddle (in pixels).
PADDLE_OFFSET = 50      # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7     # Initial vertical speed for the ball.
MAX_X_SPEED = 3         # Maximum initial horizontal speed for the ball.

# global variable
click_time = 0          # the number of mouse click
die = 0                 # the number of failed time
shrink = 1


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
        # Life
        self.heart = GImage("rsz_heart.png")
        self.window.add(self.heart, x=self.window.width-self.heart.width*3, y=0)
        self.heart_2 = GImage("rsz_heart.png")
        self.window.add(self.heart_2, x=self.window.width-self.heart.width*2, y=0)
        self.heart_3 = GImage("rsz_heart.png")
        self.window.add(self.heart_3, x=self.window.width-self.heart.width*1, y=0)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.br = ball_radius
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
        self.__start = False               # start threshold
        # Draw bricks
        self.b_col = brick_cols
        self.b_row = brick_rows
        self.secret_1 = random.randrange(2, brick_rows//2), random.randrange(1, brick_cols//2)
        self.secret_2 = random.randrange(brick_rows//2, brick_rows), random.randrange(brick_cols//2, brick_cols)
        self.secret_3 = random.randrange(1, brick_rows), random.randrange(1, brick_cols)
        for i in range(brick_rows):
            for j in range(brick_cols):
                bricks = GRect(brick_width, brick_height)
                bricks.filled = True
                # create 3 special bricks
                if (i, j) == self.secret_1:
                    bricks.color = bricks.fill_color = "red"
                elif (i, j) == self.secret_2:
                    bricks.color = bricks.fill_color = "magenta"
                elif (i, j) == self.secret_3:
                    bricks.color = bricks.fill_color = "black"
                # create a smooth color gradient
                else:
                    r = 255-int((j+i)*255/(brick_rows+brick_height))
                    bricks.color = bricks.fill_color = (0, r, 180)
                self.window.add(bricks, x=j * (brick_width + brick_spacing),
                                y=BRICK_OFFSET + i * (brick_height + brick_spacing))
        # Score
        self.__break_count = 0
        self.__score_label = GLabel(f"Score: {self.__break_count}/ {self.b_col*self.b_row}")
        self.__score_label.font = "Helvetica-16"
        self.window.add(self.__score_label, x=0, y=self.__score_label.height+10)
        # the direction of the ball
        self.direction = 0
        # to close the specific brick method after being activated once
        self.black_threshold = True
        self.magenta_threshold = True
        self.red_threshold = True
        self.paddle_width = paddle_width

    def end(self):
        text = "The End"
        for i in range(len(text)):
            end = GLabel(text[i])
            if i == 2:
                end.color = "white"
            end.font = "Helvetica-31"
            pause(10000/120)
            self.window.add(end, x=150+self.window.width/2-30*(7-i), y=self.window.height/2+13*i+5)

    def remove_heart(self):
        """
        This method calculates the time of dying in the game
        """
        global die
        die += 1
        if die == 1:
            self.window.remove(self.heart)
        elif die == 2:
            self.window.remove(self.heart_2)
        elif die == 3:
            self.window.remove(self.heart_3)

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
        brick_tr = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        brick_bl = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        brick_br = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)
        if BRICK_OFFSET < self.ball.y:              # avoid removing the score board and hearts
            if brick_tl:
                if self.check_brick(brick_tl):
                    self.window.remove(brick_tl)
                    self.add_score()
                    self.check_color()
                return True
            elif brick_tr:
                if self.check_brick(brick_tr):
                    self.window.remove(brick_tr)
                    self.add_score()
                    self.check_color()
                return True
            elif brick_bl:
                if self.check_brick(brick_bl):
                    self.window.remove(brick_bl)
                    self.add_score()
                    self.check_color()
                return True
            elif brick_br:
                if self.check_brick(brick_br):
                    self.window.remove(brick_br)
                    self.add_score()
                    self.check_color()
                return True
        return False

    def check_color(self):
        #### I found out that this part may cause my program runs pretty slow ####
        x_red = self.secret_1[1] * (BRICK_WIDTH + BRICK_SPACING)
        y_red = BRICK_OFFSET + self.secret_1[0] * (BRICK_HEIGHT + BRICK_SPACING)
        red_brick = self.window.get_object_at(x_red, y_red)
        x_magenta = self.secret_2[1] * (BRICK_WIDTH + BRICK_SPACING)
        y_magenta = BRICK_OFFSET + self.secret_2[0] * (BRICK_HEIGHT + BRICK_SPACING)
        magenta_brick = self.window.get_object_at(x_magenta, y_magenta)
        x_black = self.secret_3[1] * (BRICK_WIDTH + BRICK_SPACING)
        y_black = BRICK_OFFSET + self.secret_3[0] * (BRICK_HEIGHT + BRICK_SPACING)
        black_brick = self.window.get_object_at(x_black, y_black)

        if self.red_threshold and not red_brick:
            self.shorter_paddle()
        if self.black_threshold and not black_brick:
            self.longer_paddle()
        if self.magenta_threshold and not magenta_brick:
            self.tnt()

    def tnt(self):
        """
        :return: blow up the whole row and col of the magenta brick
        """
        self.magenta_threshold = False
        for i in range(self.b_col):
            whole_col = self.window.get_object_at(self.secret_2[1] * (BRICK_WIDTH + BRICK_SPACING), BRICK_OFFSET
                                                  + i * (BRICK_HEIGHT + BRICK_SPACING))
            if whole_col:
                if whole_col is not self.ball:
                    self.window.remove(whole_col)
                    self.add_score()
        for j in range(self.b_row):
            whole_row = self.window.get_object_at(j * (BRICK_WIDTH + BRICK_SPACING), BRICK_OFFSET
                                                  + self.secret_2[0] * (BRICK_HEIGHT + BRICK_SPACING))
            if whole_row:
                if whole_row is not self.ball:
                    self.window.remove(whole_row)
                    self.add_score()

    def shorter_paddle(self):
        """
        This method will make the paddle 0.75X shorter
        """
        self.paddle_width *= 0.75
        self.window.remove(self.paddle)
        self.paddle = GRect(self.paddle_width, PADDLE_HEIGHT, x=(self.window.width - self.paddle_width) / 2,
                            y=self.window.height - PADDLE_OFFSET)
        self.paddle.filled = True
        self.window.add(self.paddle)
        self.red_threshold = False

    def longer_paddle(self):
        """
        This method will make the paddle 1.5X longer
        """
        self.paddle_width *= 1.5
        self.window.remove(self.paddle)
        self.paddle = GRect(self.paddle_width, PADDLE_HEIGHT, x=(self.window.width - self.paddle_width) / 2,
                            y=self.window.height - PADDLE_OFFSET)
        self.paddle.filled = True
        self.window.add(self.paddle)
        self.black_threshold = False

    def paddle_move(self, m):
        """
        This method will help the paddle move in X-axis with the mouse
        :param m: MouseEvent, contain the information of the moving mouse
        """
        if self.paddle.width / 2 <= m.x <= self.window.width - self.paddle.width / 2:
            self.paddle.x = m.x - self.paddle.width / 2

    def check_brick(self, brick):
        """
        :param brick: object, the object being hit by the ball
        :return: boolean, True if it's a brick
        """
        if brick is self.paddle:
            if self.ball.x > self.paddle.x + self.paddle.width/2:
                self.direction = 1      # the ball will go right
            else:
                self.direction = 2      # the ball will go left
            return False
        return True

    def add_score(self):
        """
        This method calculate the number of removed bricks
        """
        self.__break_count += 1
        self.__score_label.text = f"Score: {self.__break_count}/ {self.b_col * self.b_row}"

    @staticmethod
    def restart():
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

    # getters
    def perfect_score(self):
        """
        :return: int, the score of winning the game
        """
        return self.b_col * self.b_row

    def get_score(self):
        """
        :return: int, the current score
        """
        return self.__break_count

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
