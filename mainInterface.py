#!/usr/bin/python3

from tkinter import *
import os

# All colors will be replaced with a variable once the theme config settings are done

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
