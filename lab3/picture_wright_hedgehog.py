from graph import *

windowSize(800, 800)
penSize(0)
c = canvas()

import math


def tree(x1, y1, x2, y2):
    penSize(0)
    brushColor(243, 229, 9)
    rectangle(x1, y1, x2, y2)


def mushroom(a, x_m, y_m):
    c.create_oval(a * (-7.5) + x_m, a * (-15) + y_m, a * 7.5 + x_m, a * 15 + y_m, outline='white', fill='white',
                  width=0)
    c.create_oval(a * (-27.5) + x_m, a * (-25) + y_m, a * 27.5 + x_m, a * (-10) + y_m, outline='white', fill='red',
                  width=0)
    c.create_oval(a * (-17.5) + x_m, a * (-23) + y_m, a * (-7.5) + x_m, a * (-20) + y_m, outline='white', fill='white',
                  width=1)
    c.create_oval(a * (-2.5) + x_m, a * (-19) + y_m, a * 3.5 + x_m, a * (-16) + y_m, outline='white', fill='white',
                  width=1)
    c.create_oval(a * 6.5 + x_m, a * (-23) + y_m, a * 16.5 + x_m, a * (-20) + y_m, outline='white', fill='white',
                  width=1)


def hedgehog(a, x, y):
    def needle(x1, y1, theta):  # needle
        penSize(2)
        penColor('black')
        brushColor('#290000')
        polygon([(a * 0 * math.cos(theta) + a * 0 * math.sin(theta) + x1,
                  a * (-0) * math.sin(theta) + a * 0 * math.cos(theta) + y1),
                 (a * 16 * math.cos(theta) + a * 0 * math.sin(theta) + x1,
                  a * (-16) * math.sin(theta) + a * 0 * math.cos(theta) + y1),
                 (a * 8 * math.cos(theta) + a * (-70) * math.sin(theta) + x1,
                  a * (-8) * math.sin(theta) + a * (-70) * math.cos(theta) + y1)])

    needle(a * (-62) + x, a * 15 + y, 3.14 / 4)
    needle(a * (-52) + x, a * 17 + y, 3.14 / 6)
    needle(a * (-42) + x, a * 10 + y, 0 / 18)
    needle(a * (-27) + x, a * 1 + y, 0 / 18)
    needle(a * (-10) + x, a * 4 + y, -3.14 / 10)
    needle(a * 8 + x, a * 8 + y, -3.14 / 6)
    needle(a * 26 + x, a * 7 + y, -3.14 / 4)

    penSize(3)
    c.create_oval(a * 57 + x, a * 5 + y, a * 80 + x, a * 20 + y, outline='white', fill='#50292a',
                  width=1)  # right upper leg
    c.create_oval(a * (-75) + x, a * 5 + y, a * (-53) + x, a * 20 + y, outline='white', fill='#50292a',
                  width=1)  # left upper leg

    c.create_oval(a * (-75) + x, a * (-35) + y, a * 75 + x, a * 35 + y, outline='white', fill='#50292a',
                  width=1)  # body
    c.create_oval(a * 45 + x, a * (-10) + y, a * 95 + x, a * 15 + y, outline='white', fill='#50292a', width=1)  # head

    c.create_oval(a * 90 + x, a * (-2) + y, a * 95 + x, a * 3 + y, outline='white', fill='#50292a', width=1)  # nose
    c.create_oval(a * 73 + x, a * (-8) + y, a * 81 + x, a * 0 + y, outline='white', fill='black', width=1)  # eye 1
    c.create_oval(a * 65 + x, a * (-2) + y, a * 73 + x, a * 6 + y, outline='white', fill='black', width=1)  # eye 2

    c.create_oval(a * 42 + x, a * 20 + y, a * 65 + x, a * 35 + y, outline='white', fill='#50292a',
                  width=1)  # right lower leg
    c.create_oval(a * (-70) + x, a * 20 + y, a * (-47) + x, a * 35 + y, outline='white', fill='#50292a',
                  width=1)  # left lower leg

    #   other needles behind the body:

    needle(a * (-55) + x, a * (-5) + y, 3.14 / 6)
    needle(a * (-40) + x, a * (-12) + y, 3.14 / 18)
    needle(a * (-30) + x, a * (-15) + y, 0 / 18)
    needle(a * (-15) + x, a * (-20) + y, 0 / 18)
    needle(a * 2 + x, a * (-20) + y, -3.14 / 36)
    needle(a * 20 + x, a * (-15) + y, -3.14 / 18)
    needle(a * 38 + x, a * (-15) + y, -3.14 / 9)

    #   mushroom:

    mushroom(a, -2.5 * a + x, -65 * a + y)

    #   apple:

    c.create_oval(a * (-75) + x, a * (-50) + y, a * (-45) + x, a * (-20) + y, outline='white', fill='#fe8800', width=0)

    #   other needles behind the body:

    needle(a * (-55) + x, a * 7 + y, 3.14 / 3)
    needle(a * (-55) + x, a * 3 + y, 3.14 / 50)
    needle(a * (-45) + x, a * 0 + y, 0 / 18)
    needle(a * (-20) + x, a * (-5) + y, 0 / 18)
    needle(a * (-8) + x, a * (-5) + y, -3.14 / 25)
    needle(a * 5 + x, a * (-1) + y, -3.14 / 12)
    needle(a * 37 + x, a * 0 + y, -3.14 / 7)

    #   other apples:

    c.create_oval(a * 5 + x, a * (-55) + y, a * 45 + x, a * (-15) + y, outline='white', fill='red', width=0)
    c.create_oval(a * (-55) + x, a * (-55) + y, a * (-25) + x, a * (-25) + y, outline='white', fill='#fe8800', width=0)

    #   needles in front of the body:

    needle(a * (-55) + x, a * 20 + y, 3.14 / 6)
    needle(a * (-45) + x, a * 22 + y, 3.14 / 12)
    needle(a * (-35) + x, a * 15 + y, 0 / 18)
    needle(a * (-20) + x, a * 8 + y, 0 / 18)
    needle(a * (-3) + x, a * 10 + y, -3.14 / 25)
    needle(a * 15 + x, a * 13 + y, -3.14 / 12)
    needle(a * 33 + x, a * 15 + y, -3.14 / 4)


# background:

brushColor(66, 205, 91)
rectangle(0, 0, 600, 800)
brushColor(170, 128, 106)
rectangle(0, 400, 600, 600)

# trees:

tree(0, 0, 40, 430)
hedgehog(0.3, 170, 420)
tree(60, 0, 170, 600)
tree(400, 0, 440, 430)
tree(470, 0, 660, 470)

# hedgehogs:

hedgehog(0.8, 320, 500)
hedgehog(0.4, 450, 450)
hedgehog(0.6, 0, 550)

# background mushrooms:

mushroom(1.5, 450, 590)
mushroom(1.4, 370, 590)
mushroom(1.3, 260, 610)
mushroom(1, 200, 590)
mushroom(0.9, 420, 590)

run()
