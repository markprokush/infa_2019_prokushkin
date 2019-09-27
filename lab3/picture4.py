from graph import *
import math
windowSize(600, 700)
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

def cords(event):
    print(event.x,event.y)
onMouseDown(cords,0)

def needle(x1, y1, theta):  # иголка
    penSize(2)
    penColor('black')
    brushColor('#290000')
    polygon([(0 * math.cos(theta) + 0 * math.sin(theta) + x1, -0 * math.sin(theta) + 0 * math.cos(theta) + y1),
             (16 * math.cos(theta) + 0 * math.sin(theta) + x1, -16 * math.sin(theta) + 0 * math.cos(theta) + y1),
             (8 * math.cos(theta) + (-70) * math.sin(theta) + x1, -8 * math.sin(theta) + (-70) * math.cos(theta) + y1)])




def ezh(x,y):

    needle(313 + x, 520 + y, 3.14 / 4)
    needle(323 + x, 522 + y, 3.14 / 6)
    needle(333 + x, 515 + y, 0 / 18)
    needle(348 + x, 506 + y, 0 / 18)
    needle(365 + x, 509 + y, -3.14 / 10)
    needle(383 + x, 513 + y, -3.14 / 6)
    needle(401 + x, 512 + y, -3.14 / 4)

    penSize(3)
    c.create_oval(432 + x, 510 + y, 455 + x, 525 + y, outline='white', fill='#50292a', width=1)  # правая верхняя нога
    c.create_oval(300 + x, 510 + y, 322 + x, 525 + y, outline='white', fill='#50292a', width=1)  # левая верхняя нога

    c.create_oval(300 + x, 470 + y, 450 + x, 540 + y, outline='white', fill='#50292a', width=1)  # туловище
    c.create_oval(420 + x, 495 + y, 470 + x, 520 + y, outline='white', fill='#50292a', width=1)  # голова

    c.create_oval(465 + x, 503 + y, 470 + x, 508 + y, outline='white', fill='#50292a', width=1)  # нос
    c.create_oval(448 + x, 497 + y, 456 + x, 505 + y, outline='white', fill='black', width=1)  # глаз 1
    c.create_oval(440 + x, 503 + y, 448 + x, 511 + y, outline='white', fill='black', width=1)  # глаз 2

    c.create_oval(417 + x, 525 + y, 440 + x, 540 + y, outline='white', fill='#50292a', width=1)  # правая нижняя нога
    c.create_oval(305 + x, 525 + y, 328 + x, 540 + y, outline='white', fill='#50292a', width=1)  # левая нижняя нога

    #   иголки за туловищем

    needle(320 + x, 500 + y, 3.14 / 6)
    needle(335 + x, 493 + y, 3.14 / 18)
    needle(345 + x, 490 + y, 0 / 18)
    needle(360 + x, 485 + y, 0 / 18)
    needle(377 + x, 485 + y, -3.14 / 36)
    needle(395 + x, 490 + y, -3.14 / 18)
    needle(413 + x, 490 + y, -3.14 / 9)

    #   яблоко и грибок

    c.create_oval(365 + x, 455 + y, 380 + x, 425 + y, outline='white', fill='white', width=0)
    c.create_oval(345 + x, 415 + y, 400 + x, 430 + y, outline='white', fill='red', width=0)
    c.create_oval(355 + x, 417 + y, 365 + x, 420 + y, outline='white', fill='white', width=1)
    c.create_oval(370 + x, 421 + y, 376 + x, 424 + y, outline='white', fill='white', width=1)
    c.create_oval(379 + x, 417 + y, 389 + x, 420 + y, outline='white', fill='white', width=1)
    c.create_oval(300 + x, 455 + y, 330 + x, 485 + y, outline='white', fill='#fe8800', width=0)

    #   иголки перед туловищем

    needle(320 + x, 512 + y, 3.14 / 3)
    needle(320 + x, 508 + y, 3.14 / 50)
    needle(330 + x, 505 + y, 0 / 18)
    needle(355 + x, 500 + y, 0 / 18)
    needle(367 + x, 500 + y, -3.14 / 25)
    needle(380 + x, 504 + y, -3.14 / 12)
    needle(412 + x, 505 + y, -3.14 / 7)

    #   яблоки

    c.create_oval(380 + x, 450 + y, 420 + x, 490 + y, outline='white', fill='red', width=0)
    c.create_oval(320 + x, 450 + y, 350 + x, 480 + y, outline='white', fill='#fe8800', width=0)

    #   иголки перед туловищем

    needle(320 + x, 525 + y, 3.14 / 6)
    needle(330 + x, 527 + y, 3.14 / 12)
    needle(340 + x, 520 + y, 0 / 18)
    needle(355 + x, 513 + y, 0 / 18)
    needle(372 + x, 515 + y, -3.14 / 25)
    needle(390 + x, 518 + y, -3.14 / 12)
    needle(408 + x, 520 + y, -3.14 / 4)


windowSize(600, 700)
penSize(0)
c = canvas()
# фон
brushColor(66, 205, 91)
rectangle(0, 0, 600, 800)
brushColor(170, 128, 106)
rectangle(0, 400, 600, 600)

ezh(-200,-135)
# деревья


penColor(243, 229, 9)
brushColor(243, 229, 9)
rectangle(0, 0, 40, 430)
rectangle(60, 0, 170, 600)
rectangle(400, 0, 440, 430)
rectangle(470, 0, 660, 470)

ezh(0,0)
#mushrooms
#1
c.create_oval(273, 573, 288, 600, outline='white', fill='white', width=0)
c.create_oval(265, 568, 294, 578, outline='white', fill='red', width=0)
c.create_oval(270, 571, 276, 575, outline='white', fill='white', width=1)
c.create_oval(282, 570, 289, 572, outline='white', fill='white', width=1)
#c.create_oval(379, 417, 389, 420, outline='white', fill='white', width=1)

c.create_oval(303, 563, 315, 588, outline='white', fill='white', width=0)
c.create_oval(295, 558, 321, 566, outline='white', fill='red', width=0)
c.create_oval(314, 563, 320, 565, outline='white', fill='white', width=1)
c.create_oval(305, 559, 311, 562, outline='white', fill='white', width=1)
c.create_oval(299, 562, 301, 563, outline='white', fill='white', width=1)

c.create_oval(340, 574, 362, 598, outline='white', fill='white', width=0)
c.create_oval(330, 569, 374, 577, outline='white', fill='red', width=0)
c.create_oval(340, 574, 346, 576, outline='white', fill='white', width=1)
c.create_oval(350, 570, 359, 575, outline='white', fill='white', width=1)
c.create_oval(366, 574, 370, 572, outline='white', fill='white', width=1)

c.create_oval(426,575,460,640,outline='white', fill='white', width=1)
c.create_oval(407, 569, 468, 576, outline='white', fill='red', width=0)
c.create_oval(435, 572, 441, 571, outline='white', fill='white', width=0)
c.create_oval(447, 572, 451, 574, outline='white', fill='white', width=0)
c.create_oval(415,571,421,575,outline='white', fill='white', width=0)
c.create_oval(459,574,462,573,outline='white', fill='white', width=0)
#ветки
brushColor(243, 229, 9)
penColor(243, 229, 9)
polygon([(400,85),(359,36),(403,73),(400,85)])
polygon([(438,238),(462,157),(438,224),(438,224)])
polygon([(170,128),(233,0),(218,0),(168,72)])
polygon([(400,290),(360,183),(399,249),(400,290)])










run()
