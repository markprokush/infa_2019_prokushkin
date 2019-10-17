from tkinter import *
from random import randrange as rnd, choice
import time
import math
root = Tk()
root.geometry('800x800')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


i=0
def click(event):
    global i
    if (x1-event.x)**2+(y1-event.y)**2 < r1**2 or (x2-event.x)**2+(y2-event.y)**2 < r2**2:
        i+=1
        print(i)
motion()
canv.bind('<Button-1>', click)
mainloop()
