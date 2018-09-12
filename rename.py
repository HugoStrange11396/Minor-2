#!/usr/bin/env python
import os

path='/root/.testingBro'
def hideFolder(path):
	name=os.path.basename(path)
	print(name)
	parent=os.path.dirname(path)
	print(parent)
	os.chdir(parent)
	os.rename(path,"."+name)

def showFolder(path):
	name=os.path.basename(path)
#	print(name)
	name=name.strip('.')
	print(name)
	parent=os.path.dirname(path)
	print(parent)
	os.chdir(parent)
	os.rename(path,name)

showFolder(path)
