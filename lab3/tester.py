from graph import *
c = canvas()
def mushroom(a, x, y):
    c.create_oval(a * (-7.5) + x, a * (-15) + y, a * 7.5 + x, a * 15 + y, outline='white', fill='yellow', width=0)
    c.create_oval(a * (-27.5) + x, a * (-25) + y, a * 27.5 + x, a * (-10) + y, outline='white', fill='red', width=0)
    c.create_oval(a * (-17.5) + x, a * (-23) + y, a * (-7.5) + x, a * (-20) + y, outline='white', fill='white', width=1)
    c.create_oval(a * (-2.5) + x, a * (-19) + y, a * 3.5 + x, a * (-16) + y, outline='white', fill='white', width=1)
    c.create_oval(a * 6.5 + x, a * (-23) + y, a * 16.5 + x, a * (-20) + y, outline='white', fill='white', width=1)
mushroom(1.5, 400, 500)
mushroom(1.4, 330, 690)
mushroom(1.3, 260, 690)
mushroom(1, 200, 690)
mushroom(0.9, 420, 660)

run()