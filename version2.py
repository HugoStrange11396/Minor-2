#!/usr/bin/env python
from bluetooth import *
from Tkinter import *
import Tkinter as tk
from Tkinter import Tk
from tkinter import *
import os
import selectPath
import saveData
import cr
import pdb
#path=''

LARGE_FONT = ("Verdana", 12) # font's family is Verdana, font's size is 12 
#master=Tk()
#v=StringVar()
 
class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("CyberXs") # set the title of the main window
        self.geometry("666x666") # set size of the main window to 300x300 pixels
 	
        # this container contains all the pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)   # make the cell in grid cover the entire window
        container.grid_columnconfigure(0,weight=1) # make the cell in grid cover the entire window
        self.frames = {} # these are pages we want to navigate to
        for F in (StartPage, PageOne, PageTwo): # for each page
            frame = F(container, self) # create the page
            self.frames[F] = frame  # store into frames
            frame.grid(row=0, column=0, sticky="nsew") # grid it to container
  
        self.show_frame(StartPage) # let the first page is StartPage

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()


    def get_page(self, page_class):
        return self.frames[page_class]
 
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Folder Security', font=LARGE_FONT)
        label.pack(pady=10, padx=10) #center alignment
        self.controller = controller
        self.v=StringVar()
        self.frame3=Frame(self)
        self.frame3.pack()
        self.frame1=Frame(self)
        self.frame1.pack()
        self.Scan()


    def mssg(self):
        if len(self.nearby_devices) > 0:
                self.d()
                self.frame3=Frame(self)
                self.frame3.pack()
                mssg= tk.Label(self.frame3,text="Select The Device")
                mssg.pack()
        else:
                self.d()
                self.frame3=Frame(self)
                self.frame3.pack()
                mssg= tk.Label(self.frame3,text="No Device in Range, Scan Again")
                mssg.pack()

    def ShowChoice(self):
            print(self.v.get())
            self.button5['state']=NORMAL

    def Scan(self):
        self.b()
        self.nearby_devices = discover_devices(lookup_names = True)
        self.mssg()
        self.frame1=Frame(self)
        self.frame1.pack()
        self.createFrame()
        print ("found %d devices" % len(self.nearby_devices))
        for name, addr in self.nearby_devices:
            Radiobutton(self.frame1, text=addr,indicatoron = 0, width=30, variable=self.v, value=name, command=self.ShowChoice).pack(pady=5, padx=10)
        self.buttons()
    
    def createFrame(self):
        self.frame2=Frame(self)
        self.frame2.pack()

    def ValidateRadioButton(self):
        if len(self.v.get()) > 0:
                self.c()
                saveData.writeInFile(self.v)
                self.controller.show_frame(PageOne)

        else:	
        	self.c()
        	self.createFrame()
        	mssg= tk.Label(self.frame2, text="Please Select any Device", fg="dark green")
        	mssg.pack()

    def b(self):
        self.frame1.destroy()
    def c(self):
        self.frame2.destroy()
    def d(self):
        self.frame3.destroy()

    def quitProg(self):
        sys.exit()

    def buttons(self):
        self.button3=tk.Button(self.frame1,text="Scan Again", command=self.Scan)
        self.button3.pack(padx=50, pady=10, side=LEFT)
        self.button5=tk.Button(self.frame1,text="Next", state=DISABLED, bg="green", command=self.ValidateRadioButton)
        self.button5.pack(padx=50, pady=10, side=LEFT)
        self.button2 = tk.Button (self.frame1,text = "Good-bye.",width=20, command=self.quitProg)
        self.button2.pack(padx=50,pady=20,side=LEFT)



 
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page One - Select Folder', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self.controller=controller
        button1 = tk.Button(self, text='Back to Home', # likewise StartPage
                            command=lambda : controller.show_frame(StartPage))
        button1.pack()
        self.selectFolder()
    
    def quitProg(self):
        sys.exit()

    def selectPathHere(self):
        self.path=selectPath.fgh()
        if len(self.path) >0:
        	saveData.writeInFile2(self.path)
        	self.nextButton['state']=NORMAL
        	label = tk.Label(text = "You chose %s" % self.path)
        	label.pack()

    def selectFolder(self):
        label = tk.Label(self,text="Folder Security", font=LARGE_FONT)
        label.pack(pady=30,padx=30)
        self.button1=tk.Button(self,text="Select Folder", command=self.selectPathHere)
        self.button1.pack()
        self.button2 = tk.Button (self,text = "Good-bye.", command=self.quitProg)
        self.button2.pack()
        self.nextButton = tk.Button (self,text = "Next", state=DISABLED, command=lambda : self.controller.show_frame(PageTwo))
        self.nextButton.pack()

#  def cryptography(self):
#	print(self.path)
#	cr.main(self.path)



class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page Two - Encryption', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        EorD = tk.Label(self, text="Do you want to Encrypt(E/e) Or Decrypt(D/d)", font=LARGE_FONT)
        EorD.pack()
        self.frame6=Frame(self)
        self.frame6.pack()
        self.ch=Entry(self)
        self.ch.pack()
        self.nextBttn = tk.Button (self,text = "Next", command=self.cryptography)
        self.nextBttn.pack()
        self.controller=controller
        self.button2 = tk.Button (self,text = "Good-bye.",width=20, command=self.quitProg)
        self.button2.pack(padx=10,pady=200,side=BOTTOM)


    def cryptography(self):
        self.f()
        self.frame6=Frame(self)
        self.frame6.pack()
        page1 = self.controller.get_page(PageOne)
        self.p=page1.path
        self.choice=self.ch.get()
        if len(self.choice) < 1:
        	error = tk.Label(self.frame6, text='Choice can not be null!!',fg="red", font=LARGE_FONT)
        	error.pack(pady=10, padx=10)
        else:
        	self.passw = tk.Label(self.frame6, text="Enter the Password:-", font=LARGE_FONT)
        	self.passw.pack()
        	self.pswd = Entry(self.frame6, show="*", width=15)
        	self.pswd.pack()
        	self.nextPass = tk.Button (self.frame6,text = "Next", command=self.pswrd)
        	self.nextPass.pack()

    def pswrd(self):
        self.psw=self.pswd.get()
        saveData.writeInFile2(self.psw)
        cr.main(self.p, self.choice,self.psw)


    def quitProg(self):
        sys.exit()

    def f(self):
        self.frame6.destroy()




if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
