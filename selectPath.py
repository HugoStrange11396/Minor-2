#!/usr/bin/env python
from Tkinter import Tk
import tkinter as tk
import tkFileDialog
import os
from tkFileDialog import askopenfilename
import cr
def fgh():
	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	tempdir = tkFileDialog.askdirectory(initialdir = "/",title='Please select a directory')
	#if len(tempdir) > 0:
	#    print "You chose %s" % tempdir
	return tempdir
#filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)
#def helloCallBack():
#    os.system('./selectItem.py')

#root=tk.Tk()
#button1 = tk.Button(text="SelectItem", command= helloCallBack)
#button1.pack()
#root.mainloop()

