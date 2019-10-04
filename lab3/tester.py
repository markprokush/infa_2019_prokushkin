from graph import *
c=canvas()

def noga(x,y):
    c.create_oval(-7.5+x, -15+y, 7.5+x, 15+y, outline='white', fill='black', width=0)

noga(0,0)
run()