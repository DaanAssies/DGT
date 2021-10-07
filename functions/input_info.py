import os
import sys
import ac
import acsys

sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + 'shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."

from functions.shared_memory import info

# Between 0 and 1
def getGasInput(car=0):
    return ac.getCarState(car, acsys.CS.Gas)

# Between 0 and 1
def getBrakeInput(car=0):
    return ac.getCarState(car, acsys.CS.Brake)

# Not based on input, but is based on whether the clutch is 'biting' in the car or no. Between 0 and 1
def getClutch(car=0):
    return ac.getCarState(car, acsys.CS.Clutch)

# In radians [-2pi, 2pi]
def getSteerInput(car=0):
    return ac.getCarState(car, acsys.CS.Steer)
