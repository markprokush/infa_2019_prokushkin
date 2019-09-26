from graph import *

windowSize(800, 800)
penSize(0)
c = canvas()
# фон
brushColor(66, 205, 91)
rectangle(0, 0, 600, 800)
brushColor(170, 128, 106)
rectangle(0, 400, 600, 600)
# деревья
brushColor(243, 229, 9)
rectangle(0, 0, 40, 430)
rectangle(60, 0, 170, 600)
rectangle(400, 0, 440, 430)
rectangle(470, 0, 660, 470)

import math


def needle(x1, y1, theta):  # иголка
    penSize(2)
    penColor('black')
    brushColor('#290000')
    polygon([(0 * math.cos(theta) + 0 * math.sin(theta) + x1, -0 * math.sin(theta) + 0 * math.cos(theta) + y1),
             (16 * math.cos(theta) + 0 * math.sin(theta) + x1, -16 * math.sin(theta) + 0 * math.cos(theta) + y1),
             (8 * math.cos(theta) + (-70) * math.sin(theta) + x1, -8 * math.sin(theta) + (-70) * math.cos(theta) + y1)])


needle(313, 520, 3.14 / 4)
needle(323, 522, 3.14 / 6)
needle(333, 515, 0 / 18)
needle(348, 506, 0 / 18)
needle(365, 509, -3.14 / 10)
needle(383, 513, -3.14 / 6)
needle(401, 512, -3.14 / 4)

penSize(3)
c.create_oval(432, 510, 455, 525, outline='white', fill='#50292a', width=1)  # правая верхняя нога
c.create_oval(300, 510, 322, 525, outline='white', fill='#50292a', width=1)  # левая верхняя нога

c.create_oval(300, 470, 450, 540, outline='white', fill='#50292a', width=1)  # туловище
c.create_oval(420, 495, 470, 520, outline='white', fill='#50292a', width=1)  # голова

c.create_oval(465, 503, 470, 508, outline='white', fill='#50292a', width=1)  # нос
c.create_oval(448, 497, 456, 505, outline='white', fill='black', width=1)  # глаз 1
c.create_oval(440, 503, 448, 511, outline='white', fill='black', width=1)  # глаз 2

c.create_oval(417, 525, 440, 540, outline='white', fill='#50292a', width=1)  # правая нижняя нога
c.create_oval(305, 525, 328, 540, outline='white', fill='#50292a', width=1)  # левая нижняя нога

needle(320, 500, 3.14 / 6)
needle(335, 493, 3.14 / 18)
needle(345, 490, 0 / 18)
needle(360, 485, 0 / 18)
needle(377, 485, -3.14 / 36)
needle(395, 490, -3.14 / 18)
needle(413, 490, -3.14 / 9)

penSize(0)
c.create_oval(365,455,380,425, outline='white', fill='white', width=0)
c.create_oval(345,415,400,430, outline='white', fill='red', width=0)
c.create_oval(355,417,365,420, outline='white', fill='white', width=1)
c.create_oval(370,421,376,424, outline='white', fill='white', width=1)
c.create_oval(379,417,389,420, outline='white', fill='white', width=1)
c.create_oval(300, 455, 330, 485, outline='white', fill='#fe8800', width=0)

needle(320, 512, 3.14 / 3)
needle(320, 508, 3.14 / 50)
needle(330, 505, 0 / 18)
needle(355, 500, 0 / 18)
needle(367, 500, -3.14 / 25)
needle(380, 504, -3.14 / 12)
needle(412, 505, -3.14 / 7)

c.create_oval(380, 450, 420, 490, outline='white', fill='red', width=0)
c.create_oval(320, 450, 350, 480, outline='white', fill='#fe8800', width=0)


needle(320, 525, 3.14 / 6)
needle(330, 527, 3.14 / 12)
needle(340, 520, 0 / 18)
needle(355, 513, 0 / 18)
needle(372, 515, -3.14 / 25)
needle(390, 518, -3.14 / 12)
needle(408, 520, -3.14 / 4)



run()
