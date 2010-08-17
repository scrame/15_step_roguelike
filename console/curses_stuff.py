#!/usr/bin/python

import curses
import curses.ascii
from curses import panel

def run(win):
    while(1):
        win.move(20,20)
        win.addstr(curses.ascii.unctrl(win.getch()))
        win.refresh() 

curses.wrapper(run)

