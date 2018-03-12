#!/usr/bin/python3

# Interface for a raspberry pi zero based smartwatch using the adafruit pitft - 2.8" touchscreen
#
# Copyright (C) 2018  Sarah Lynn Lefebvre
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see https://www.gnu.org/licenses/gpl.html.

from tkinter import *
import os

# All colors will be replaced with a variable once the theme config settings are done
# i am thinking of having the clock interface code in another file, 
# and using this to show the butons and status bar at all times instead

root = Tk()
root.geometry("320x240")
root.configure(background = "#212121")

def gotoMenu(): # will be changed to actually go to menu later
    root.destroy()

def sleep(): # will be changed later once a method to put the watch to sleep is found
    root.destroy()

# we may not need this
#
#def refresh():
#    frame.grid_forget()

menuIcon = PhotoImage(file="application-menu.png")
sleepIcon = PhotoImage(file="system-suspend-hibernate.png")

mainFrame = Frame(root)
mainFrame.grid(row = 0, column = 2, rowspan = 1, columnspan = 2)


clockFrame = Frame(mainFrame)
clockFrame.configure(background = "#212121")
clockFrame.grid(row = 0, column = 1, rowspan = 1, columnspan = 1)
label = Label(clockFrame, text="Clock goes here")#, fg = "#fbf9fc")
label.grid(row = 0, column = 0)#, ipadx = 10, ipady = 10)


#indicatorFrame(root)

buttonFrame = Frame(mainFrame)
buttonFrame.grid(row = 0, column = 2, rowspan = 1, columnspan = 2)
menuButton = Button(buttonFrame, image = menuIcon, command = gotoMenu)
menuButton.grid(row = 0, column = 0)
sleepButton = Button(buttonFrame, image = sleepIcon, background = "#212121",  command = sleep)
sleepButton.grid(row = 1, column = 0)

root.mainloop()

