import os
import sys
import ac
import acsys
from functions.shared_memory import info

sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + '/../shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."


# returns type ACC_SESSION_TYPE
# unknown = -1, practice = 0, qualifying = 1, race = 2, hotlap = 3, timeattack = 4, rest irrelevant
# For some reason this only works after x amount of ticks after loading into the game. It returns 0 before that.
def getSessionType():
    return info.graphics.session

def getDriverName(car=0):
    return ac.getDriverName(car)

def getCarName(car=0):
    return ac.getCarName(car)

def getTrackName():
    return ac.getTrackName(0)

def getTrackConfig():
    return ac.getTrackConfiguration(0)

def getTrackLength():
    return ac.getTrackLength(0)

# Returns session's max no. of cars
def getCarsCount():
    return ac.getCarsCount()

# Returns the session status. 0=OFF, 1= REPLAY, 2=LIVE, 3=PAUSE
def getSessionStatus():
    return info.graphics.status
