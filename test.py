#!/usr/bin/env python
from bluetooth import *
from Tkinter import *
import Tkinter as tk
from Tkinter import Tk
from tkinter import *
import os

import selectPath
LARGE_FONT= ("Verdana", 12)
path=''

root = Tk()
e=Entry(root)
e.pack()
e.focus_get()
s=e.get()
print(s)

"""

class App(Frame):    

	
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
	self.v=StringVar()
	container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)
        self.a()
	self.frame1=Frame(self)
	self.frame1.pack()
	

    def ShowChoice(self):
	print(self.v.get())

    def show_frame(self):
	#frame = self.frames[cont]
	selectFolder.tkraise(sf);

    def Scan(self):
	self.b()
	self.frame1=Frame(self)
        self.frame1.pack()
	print ("performing inquiry...")
	nearby_devices = discover_devices(lookup_names = True)
	print ("found %d devices" % len(nearby_devices))
	for name, addr in nearby_devices:
		Radiobutton(self.frame1, text=addr,indicatoron = 0, width=20, padx=20, variable=self.v, value=name, command=self.ShowChoice).pack(anchor=W)
#	for i in range(0,2):
#		self.abc = Button(self.frame1, text = addr)
#	        self.abc.pack() # This is fixing your issue
	if len(nearby_devices) > 0:
		next=Button(self.frame1, text = "Next",command=self.selectFolder).pack()
	return 0



    def a(self):
        self.call_button = Button(self, text = "Scan for BT", command=self.Scan)
        self.call_button.pack() # This is fixing your issue
	self.calls_button = Button(self, text = "Delete", command=self.b)
        self.calls_button.pack() # This is fixing your issue

    def b(self):
        self.frame1.destroy()
	

    def selectFolder(self):
	self.frame1.destroy()
	label = Label(self,text="Folder Security", font=LARGE_FONT)
	label.pack(pady=30,padx=30)
	button1=Button(self,text="Select Folder", command=self.selectPathHere)
	button1.pack()
	button2 = Button (self,text = "Good-bye.", command = self.quitProg)
	button2.pack()

    def selectPathHere(self):
	path=selectPath.fgh()
	label = Label(self,text = "You chose %s" % path)
	label.pack()
"""


"""class selectFolder(tk.Frame):
	def __init__(self, master):
        	Frame.__init__(self, master)
        	self.pack()
		label = Label(self,text="Folder Security", font=LARGE_FONT)
		label.pack(pady=30,padx=30)
		button1=Button(self,text="Select Folder", command=self.selectPathHere)
		button1.pack()
		button2 = Button (self,text = "Good-bye.", command = self.quitProg)
		button2.pack()

    	def selectPathHere(self):
		path=selectPath.fgh()
		label = Label(self,text = "You chose %s" % path)
		label.pack()

"""

root.mainloop()
"""root = Tk()
app = App(master=root)
app.mainloop()"""
