#!/usr/bin/env python
import os
def writeInFile(mac):
	f=open("file.txt","a+")
#	print(mac.get())
	s=mac.get()
	f.write("\n"+s+"\t")

def writeInFile2(path):
	f=open("file.txt","a+")
	f.write(path+"\t")

def writeInFile3(pas):
	f=open("file.txt","a+")
	f.write(pas+"\n")


#if __name__=="__main__":
#	writeInFile("hey")
