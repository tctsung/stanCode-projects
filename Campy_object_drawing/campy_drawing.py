"""
File: my_drawing.py
Name: Ching-Tsung Tsai
----------------------
Time spent: ~10hr
"""
import random
from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLine, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Global variable:
window = GWindow(width=450, height=600)


def main():
    """
    1. Goal:
        This program will create a different landscape of aurora lights everytime you click the mouse
    2. Inspiration:
        Being a biostatistician, I've always been fascinated by the concept of randomness. To create a "random vibe" on
        my drawing, I decided to draw the sky in Alaska with many randomly arranged objects
    3. NOTED:
        Most of the objects in this drawing are create by the random package, including the pattern of aurora lights
        , the trees branches, the head & position of the shooting star, the stars position, and the mountain ridge.
        This means that everytime you run the program, it will turn to a different drawing !!!
    """
    # draw the image
    draw_1st()
    # once you click the mouse, the program will run again and create a slightly different image
    onmouseclicked(draw)


def draw_1st():
    # create a gradual color background
    ground_gradual()
    # create a dark sky
    sky()
    # create a teepee
    teepee()
    # create the body of the mountains
    ground()
    # create the silhouette of the mountains
    mount_ridge()
    # create the aurora lights in the sky
    aurora_lights()
    # create the stars
    stars()
    # create two trees
    trees()
    # create a shooting star
    shooting_stars()
    # write down my name
    label()


def draw(m):
    ground_gradual()
    sky()
    teepee()
    ground()
    mount_ridge()
    aurora_lights()
    stars()
    trees()
    shooting_stars()
    label()


def label():
    name = GLabel("Night of the Aurora Lights\n\t          by Deron")
    name.font = "Helvetica-12"
    name.color = "white"
    window.add(name, 255, window.height*0.95+20)


def ground_gradual():
    for i in range(255):
        blue_ground = GRect(window.width, 2)
        r = 10+i
        g = 33+i
        if r > 255:
            r = 255
        if g > 255:
            g = 255
        b = 54+i
        if b > 255:
            b = 255
        blue_ground.color = (r, g, b)
        blue_ground.filled = True
        # create 255 rectangle with gradually changed color
        blue_ground.fill_color = (r, g, b)
        window.add(blue_ground, x=0, y=i*blue_ground.height+200)


def sky():
    dark_sky = GRect(window.width, 200)
    dark_sky.color = (6, 33, 54)
    dark_sky.filled = True
    dark_sky.fill_color = (6, 33, 54)
    window.add(dark_sky, x=0, y=0)


def teepee():
    # top roof
    triangle = GPolygon()
    triangle.add_vertex((150, 330))
    triangle.add_vertex((150-23, 330+30))
    triangle.add_vertex((150 + 13, 330 + 30))
    triangle.filled = True
    triangle.fill_color = (48, 21, 15)
    triangle.color = (48, 21, 15)
    window.add(triangle)
    # body
    for i in range(120):
        hill = GRect(i//1.2, 1)
        hill.color = (200+i//3, i*2, 0)
        hill.filled = True
        hill.fill_color = (200+i//3, i*2, 0)
        window.add(hill, 150-i/1.7, 330+i*hill.height)
    # rack
    wood_1 = GPolygon()
    wood_1.add_vertex((150+30/1.7, 330-30*hill.height))
    wood_1.add_vertex((150-120/1.7-2, 330+120*hill.height))
    wood_1.add_vertex((150-120/1.7+5-2, 330+120*hill.height))
    wood_1.filled = True
    wood_1.fill_color = (87, 31, 17)
    wood_1.color = (87, 31, 17)
    window.add(wood_1)
    wood_2 = GPolygon()
    wood_2.add_vertex((150-10, 330-30*hill.height))
    wood_2.add_vertex((150 - 120 / 1.7+hill.width, 330 + 120 * hill.height))
    wood_2.add_vertex((150 - 120 / 1.7+hill.width+8, 330 + 120 * hill.height))
    wood_2.filled = True
    wood_2.fill_color = (87, 31, 17)
    wood_2.color = (87, 31, 17)
    window.add(wood_2)
    wood_3 = GPolygon()
    wood_3.add_vertex((150+3, 330 - 30 * hill.height))
    wood_3.add_vertex((150 - 10, 330 + 120 * hill.height))
    wood_3.add_vertex((150-18, 330 + 120 * hill.height))
    wood_3.filled = True
    wood_3.fill_color = (87, 31, 17)
    wood_3.color = (87, 31, 17)
    window.add(wood_3)
    # pattern on the teepee
    line_1 = GLine(150-40/1.7, 330+40*hill.height, 150-5, 330+40*hill.height+15)
    line_2 = GLine(150 - 5, 330 + 40 * hill.height + 14, 150+15, 330 + 40 * hill.height + 10)
    line_1.color = (87, 31, 17)
    line_2.color = (87, 31, 17)
    window.add(line_1)
    window.add(line_2)
    line_3 = GLine(150 - 70 / 1.7, 330 + 70 * hill.height, 150-12, 330 + 70 * hill.height + 15)
    line_4 = GLine(150 - 12, 330 + 70 * hill.height + 15, 150+20, 330 + 70 * hill.height + 12)
    line_3.color = (87, 31, 17)
    line_4.color = (87, 31, 17)
    window.add(line_3)
    window.add(line_4)


def ground():
    dark_ground = GRect(window.width, 150)
    dark_ground.filled = True
    dark_ground.color = (0, 0, 30)
    dark_ground.fill_color = (0, 0, 30)
    window.add(dark_ground, 0, window.height-150)


def mount_ridge():
    for i in range(100):
        m_vertex = random.randint(0, window.width)
        m_width = random.randint(0, 30)
        m_height = random.randint(-10, 0)
        m_ridge = GPolygon()
        m_ridge.add_vertex((m_vertex, m_height))
        m_ridge.add_vertex((m_vertex-m_width, 20))
        m_ridge.add_vertex((m_vertex+m_width, 20))
        m_ridge.filled = True
        m_ridge.fill_color = (0, 0, 30)
        window.add(m_ridge, x=0, y=window.height-170)


def aurora_lights():
    # color 1
    aurora_5 = GPolygon()
    aurora_5.add_vertex((99, 240))
    for i in range(90, 445):
        aurora_5_y = random.randint(50, int(-5/9*i+300)+20)
        aurora_5.add_vertex((i, aurora_5_y))
    aurora_5.add_vertex((window.width, 50))
    aurora_5.color = "yellowgreen"
    aurora_5.filled = True
    aurora_5.fill_color = "yellowgreen"
    window.add(aurora_5, x=-50, y=-50)
    # color 2
    aurora_4 = GPolygon()
    aurora_4.add_vertex((99, 240))
    for i in range(90, 445):
        aurora_4_y = random.randint(50, int(-5/9*i+300)+20)
        aurora_4.add_vertex((i, aurora_4_y))
    aurora_4.add_vertex((window.width, 50))
    aurora_4.color = "turquoise"
    aurora_4.filled = True
    aurora_4.fill_color = "turquoise"
    window.add(aurora_4, x=-50, y=-50)
    # color 3
    aurora = GPolygon()
    aurora.add_vertex((99, 245))
    for i in range(100, 445):
        aurora_y = random.randint(50, int(-5/9*i+300))
        aurora.add_vertex((i, aurora_y))
    aurora.add_vertex((window.width, 50))
    aurora.color = "lightgreen"
    aurora.filled = True
    aurora.fill_color = "lightgreen"
    window.add(aurora, x=-50, y=-40)
    # sky color, to hide the edge
    aurora_2 = GPolygon()
    aurora_2.add_vertex((99, 245))
    for i in range(150, 445):
        aurora_2_y = random.randint(50, int(-5/9*i+300))
        aurora_2.add_vertex((i, aurora_2_y+20))
    aurora_2.add_vertex((window.width, 50+20))
    aurora_2.color = (6, 33, 65)
    aurora_2.filled = True
    aurora_2.fill_color = (6, 33, 65)
    window.add(aurora_2, x=-50, y=-40)
    # sky color, to hide the edge
    aurora_3 = GPolygon()
    aurora_3.add_vertex((99, 245))
    for i in range(100, 445):
        aurora_3_y = random.randint(50, int(-5/9*i+300))
        aurora_3.add_vertex((i, aurora_3_y+30))
    aurora_3.add_vertex((window.width, 50+30))
    aurora_3.color = (6, 33, 54)
    aurora_3.filled = True
    aurora_3.fill_color = (6, 33, 54)
    window.add(aurora_3, x=-50, y=-30)


def stars():
    for i in range(120):
        star = GOval(0.5, 0.5)
        star_x = random.randint(3, window.width)
        star_y = random.randint(0, window.height//2+30)
        star.color = (255, 255, 255)
        star.filled = True
        star.fill_color = (255, 255, 255)
        window.add(star, x=star_x, y=star_y)


def trees():
    # trunk of tree 1
    trunk = GRect(10, 100)
    trunk.filled = True
    trunk.fill_color = (0, 0, 30)
    window.add(trunk, x=window.width*0.7, y=window.height*0.62)
    # branches of tree 1
    tree = GPolygon()
    tree.add_vertex((window.width*0.7-trunk.width/2, window.height*0.62))
    for i in range(80):
        tree_x = random.randint(window.width*0.7+10-30, window.width*0.7+10+30)
        tree_y = random.randint(window.height*0.62-50, window.height*0.62+30)
        tree.add_vertex((tree_x, tree_y))
    tree.color = (0, 0, 30)
    tree.filled = True
    tree.fill_color = (0, 0, 30)
    window.add(tree)
    # trunk of tree 2
    trunk_2 = GRect(10, 100)
    trunk_2.filled = True
    trunk_2.fill_color = (0, 0, 30)
    window.add(trunk_2, x=window.width*0.7+80, y=window.height*0.62+5)
    # branches of tree 2
    tree_2 = GPolygon()
    tree_2.add_vertex((window.width*0.7-trunk.width/2+80, window.height*0.62))
    for i in range(80):
        tree_2_x = random.randint(window.width*0.7+10-30+80, window.width*0.7+10+30+80)
        tree_2_y = random.randint(window.height*0.62-30+5, window.height*0.62+30+5)
        tree_2.add_vertex((tree_2_x, tree_2_y))
    tree_2.color = (0, 0, 30)
    tree_2.filled = True
    tree_2.fill_color = (0, 0, 30)
    window.add(tree_2, x=0, y=5)


def shooting_stars():
    # the tail of the shooting star
    location_x = random.randint(-70, 0)
    location_y = random.randint(-50, 80)
    for i in range(4):
        shooting_star = GArc(1000-i*100, 400, 90, 50, x=window.width/2-10+location_x, y=window.height/4-i*1.5+location_y)
        shooting_star.color = "white"
        shooting_star.filled = False
        window.add(shooting_star)
    # the front of the shooting star
    for i in range(10):
        diameter = random.randint(10, 20)
        position = random.randint(0, 15)
        strange_circle = GOval(diameter, diameter)
        strange_circle.color = "white"
        window.add(strange_circle, x=window.width/2+position+diameter+location_x, y=window.height/4+diameter//2-5+location_y)


if __name__ == '__main__':
    main()
