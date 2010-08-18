#!/usr/bin/python

import curses
import curses.ascii
from curses import panel


x_max = 50
y_max = 50

x = 20
y = 20


def update_pos(c):
    global x,y
    if(259 == c):
        x = (x_max if x==0 else x-1)
    if(258 == c):
        x = (0 if x==x_max else x+1)

    if(260 == c):
        y = (y_max if y==0 else y-1)
    if(261 == c):
        y = (0 if y==y_max else y+1)


def run(win):
    
    while(1):
        update_pos(win.getch())
        win.move(x,y)
        win.addstr('#')
        win.move(0,0)
        win.refresh() 

curses.wrapper(run)

