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

def hedgehog(a, x, y):
    def needle(x1, y1, theta):  # иголка
        penSize(2)
        penColor('black')
        brushColor('#290000')
        polygon([(a*0 * math.cos(theta) + a*0 * math.sin(theta) + x1, a*(-0) * math.sin(theta) + a*0 * math.cos(theta) + y1),
                (a*16 * math.cos(theta) + a*0 * math.sin(theta) + x1, a*(-16) * math.sin(theta) + a*0 * math.cos(theta) + y1),
                (a*8 * math.cos(theta) + a*(-70) * math.sin(theta) + x1, a*(-8) * math.sin(theta) + a*(-70) * math.cos(theta) + y1)])


    needle(a*(-62)+x, a*15+y, 3.14 / 4)
    needle(a*(-52)+x, a*17+y, 3.14 / 6)
    needle(a*(-42)+x, a*10+y, 0 / 18)
    needle(a*(-27)+x, a*1+y, 0 / 18)
    needle(a*(-10)+x, a*4+y, -3.14 / 10)
    needle(a*8+x, a*8+y, -3.14 / 6)
    needle(a*26+x, a*7+y, -3.14 / 4)

    penSize(3)
    c.create_oval(a*57+x, a*5+y, a*80+x, a*20+y, outline='white', fill='#50292a', width=1)  # правая верхняя нога
    c.create_oval(a*(-75)+x, a*5+y, a*(-53)+x, a*20+y, outline='white', fill='#50292a', width=1)  # левая верхняя нога

    c.create_oval(a*(-75)+x, a*(-35)+y, a*75+x, a*35+y, outline='white', fill='#50292a', width=1)  # туловище
    c.create_oval(a*45+x, a*(-10)+y, a*95+x, a*15+y, outline='white', fill='#50292a', width=1)  # голова

    c.create_oval(a*90+x, a*(-2)+y, a*95+x, a*3+y, outline='white', fill='#50292a', width=1)  # нос
    c.create_oval(a*73+x, a*(-8)+y, a*81+x, a*0+y, outline='white', fill='black', width=1)  # глаз 1
    c.create_oval(a*65+x, a*(-2)+y, a*73+x, a*6+y, outline='white', fill='black', width=1)  # глаз 2

    c.create_oval(a*42+x, a*20+y, a*65+x, a*35+y, outline='white', fill='#50292a', width=1)  # правая нижняя нога
    c.create_oval(a*(-70)+x, a*20+y, a*(-47)+x, a*35+y, outline='white', fill='#50292a', width=1)  # левая нижняя нога

    #   иголки за туловищем

    needle(a*(-55)+x, a*(-5)+y, 3.14 / 6)
    needle(a*(-40)+x, a*(-12)+y, 3.14 / 18)
    needle(a*(-30)+x, a*(-15)+y, 0 / 18)
    needle(a*(-15)+x, a*(-20)+y, 0 / 18)
    needle(a*2+x, a*(-20)+y, -3.14 / 36)
    needle(a*20+x, a*(-15)+y, -3.14 / 18)
    needle(a*38+x, a*(-15)+y, -3.14 / 9)

    #   яблоко и грибок

    c.create_oval(a*(-10)+x,a*(-50)+y,a*5+x,a*(-80)+y, outline='white', fill='white', width=0)
    c.create_oval(a*(-30)+x,a*(-90)+y,a*25+x,a*(-75)+y, outline='white', fill='red', width=0)
    c.create_oval(a*(-20)+x,a*(-88)+y,a*(-10)+x,a*(-85)+y, outline='white', fill='white', width=1)
    c.create_oval(a*(-5)+x,a*(-84)+y,a*1+x,a*(-81)+y, outline='white', fill='white', width=1)
    c.create_oval(a*4+x,a*(-88)+y,a*14+x,a*(-85)+y, outline='white', fill='white', width=1)
    c.create_oval(a*(-75)+x, a*(-50)+y, a*(-45)+x, a*(-20)+y, outline='white', fill='#fe8800', width=0)

    #   иголки перед туловищем

    needle(a*(-55)+x, a*7+y, 3.14 / 3)
    needle(a*(-55)+x, a*3+y, 3.14 / 50)
    needle(a*(-45)+x, a*0+y, 0 / 18)
    needle(a*(-20)+x, a*(-5)+y, 0 / 18)
    needle(a*(-8)+x, a*(-5)+y, -3.14 / 25)
    needle(a*5+x, a*(-1)+y, -3.14 / 12)
    needle(a*37+x, a*0+y, -3.14 / 7)

    #   яблоки

    c.create_oval(a*5+x, a*(-55)+y, a*45+x, a*(-15)+y, outline='white', fill='red', width=0)
    c.create_oval(a*(-55)+x, a*(-55)+y, a*(-25)+x, a*(-25)+y, outline='white', fill='#fe8800', width=0)

    #   иголки перед туловищем

    needle(a*(-55)+x, a*20+y, 3.14 / 6)
    needle(a*(-45)+x, a*22+y, 3.14 / 12)
    needle(a*(-35)+x, a*15+y, 0 / 18)
    needle(a*(-20)+x, a*8+y, 0 / 18)
    needle(a*(-3)+x, a*10+y, -3.14 / 25)
    needle(a*15+x, a*13+y, -3.14 / 12)
    needle(a*33+x, a*15+y, -3.14 / 4)

hedgehog(0.6, 400, 550)
hedgehog(0.4, 450, 450)
hedgehog(0.3, 170, 420)

run()
