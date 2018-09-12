#!/usr/bin/env python
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os, random, sys, pkg_resources
import pdb

global passw
global encfiles 
encfiles=[]
global choice
choice=""
global password
password=""
passw="asdf"


def encrypt(key, filename):
        chunksize = 64 * 1024
        outFile = os.path.join(os.path.dirname(filename), "(encrypted)"+os.path.basename(filename))
        filesize = str(os.path.getsize(filename)).zfill(16)
        IV = ''
 
        for i in range(16):
                IV += chr(random.randint(0, 0xFF))
       
        encryptor = AES.new(key, AES.MODE_CBC, IV)
 
        with open(filename, "rb") as infile:
                with open(outFile, "wb") as outfile:
                        outfile.write(filesize)
                        outfile.write(IV)
                        while True:
                                chunk = infile.read(chunksize)
                               
                                if len(chunk) == 0:
                                        break
 
                                elif len(chunk) % 16 !=0:
                                        chunk += ' ' *  (16 - (len(chunk) % 16))
 
                                outfile.write(encryptor.encrypt(chunk))
 
 
def decrypt(key, filename):
        name=os.path.basename(filename)
        name=name.replace('(encrypted)','')
        OutFile = os.path.join(os.path.dirname(filename), name)
        chunksize = 64 * 1024
        with open(filename, "rb") as infile:
                filesize = infile.read(16)
                IV = infile.read(16)
                decryptor = AES.new(key, AES.MODE_CBC, IV)
                with open(outFile, "wb") as outfile:
                        while True:
                                chunk = infile.read(chunksize)
                                if len(chunk) == 0:
                                        break
 
                                outfile.write(decryptor.decrypt(chunk))
 
                        outfile.truncate(int(filesize))
       
def allfiles(path):
        allFiles = []
        for root, subfiles, files in os.walk(path):
                for names in files:
                        allFiles.append(os.path.join(root, names))
        return allFiles


#passwordcheck





def ncrypt(path,encFile):
	
	encFiles=encFile	
	print(encFiles)
	
        for Tfiles in encFiles:
                print(Tfiles)
		
                if os.path.basename(Tfiles).startswith("(encrypted)"):
			
                        print "%s is already encrypted" %str(Tfiles)
                        pass
	
                elif Tfiles == os.path.join(os.getcwd(), sys.argv[0]):
			
                        pass
                else:
			
                        encrypt(SHA256.new(password).digest(), str(Tfiles))
			
                        print "Done encrypting %s" %str(Tfiles)
                        os.remove(Tfiles)
 
 
def dcrypt(path):
        flename = raw_input("Enter the filename to decrypt: ")
	foldername=path
	filename=os.path.join(foldername, flename)
	print(filename)
        if not os.path.exists(filename):
                print "The file does not exist"
                sys.exit(0)
        elif not os.path.basename(filename).startswith("(encrypted)"):
                print "%s is already not encrypted" %filename
                sys.exit()
        else:
                decrypt(SHA256.new(password).digest(), filename)
		print os.path.dirname(filename)
                print "Done decrypting %s" %os.path.basename(filename)
                os.remove(filename)


def passValidate(filess,passs,ch):
	choice=ch
	password=passs
	fname=filess
	print(fname)
	if password==passw:
		encFiles = allfiles(fname)
		print(encFiles)
		
		if choice == "E" or choice == "e":
			
			ncrypt(fname,encFiles)
		elif choice == "D" or choice == "d":
			dcrypt(fname)
		else:
			print "Please choose a valid command."
	else:
		print("Wrong password!")


def main(path,ch,pswd):
#	choice = raw_input("Do you want to (E)ncrypt or (D)ecrypt? ")
	choice=ch
#	password = raw_input("Enter the password: ")
	password=pswd
	files=path
	print(path)
	passValidate(files,password,choice)
 


