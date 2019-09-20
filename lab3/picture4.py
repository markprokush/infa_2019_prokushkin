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
run()
