#!/usr/bin/python
import random, sys, os, signal
import os.path
from termcolor import colored
from os import listdir

myPath="/"
myFiles=[]
print colored("You done fucked up now!", 'red')

def signalHandler(signal, frame):
    print colored("You are not allowed to leave until you complete the task", 'red')
signal.signal(signal.SIGINT, signalHandler)

def bitchMode(difficultyRating):
    for dirpath, dirnames, filenames in os.walk(myPath):
        for filename in [f for f in filenames if f.endswith("")]:
            myFiles.append(os.path.join(dirpath, filename))
    fileKill=random.choice(myFiles)
    if difficultyRating==4:
        retardMode(fileKill)
    else:
        killCommand(fileKill)

def hardMode():
    myFiles=os.listdir(myPath)
    fileKill=random.choice(myFiles)
    killCommand(fileKill)

def hardcoreMode():
#   os.rmdir(myPath)
    print 'test'
    sys.exit()

def retardMode():
    fileKill2=random.choice(myFiles)
#   os.rename(fileKill,fileKill2)
    sys.exit()

def killCommand(fileKill):
    doaNumber=random.randint(1,6)
    print "The bullet is in chamber: "+str(doaNumber)
    doaKill=random.randint(1,6)
    print "You spun the chamber landing on: "+str(doaKill)
    if doaNumber == doaKill:
        print colored("Sucks to suck", 'red')
        print "Deleting random file: "+str(fileKill)
#       os.rmdir(fileKill)
    else:
        print colored("You live to see another day", 'green')
    sys.exit()

def main():
    print """Difficulty raiting:
"""+colored("""1""", 'blue')+""" = You're a bitch, this pulls every system file and only deletes one
"""+colored("""2""", 'green')+""" = No bitches here, pulls all the top level directories and deletes one of them
"""+colored("""3""", 'red')+""" = King Leonidas, Deletes the root directory
"""+colored("""4""", 'yellow')+""" = You aren't here to have fun, Takes two random files and overwrites one with the other\n \n"""
    difficultyRating = raw_input(colored("So what's it going to be? Are you a bitch or a man?(1-4): ", 'red'))
    if difficultyRating== "1":
        bitchMode(difficultyRating)
    if difficultyRating=="2":
        hardMode()
    if difficultyRating=="3":
        hardcoreMode()
    if difficultyRating=="4":
        bitchMode(difficultyRating)
    else:
        print "\n\n\ndon't be a moron, enter one number between 1 and 4"
        main()
if __name__=='__main__':
    main()
    sys.exit()

