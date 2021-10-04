import os
import sys
import ac
import acsys

sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + 'shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."

from functions.shared_memory import info

# METHODS IN THIS CLASS RETURN A SCALAR VECTOR

# TODO: TEST
def getDrag(car=0):
    return ac.getCarState(car, acsys.CS.Aero, 0)

# TODO: TEST
def getLiftFront(car=0):
    return ac.getCarState(car, acsys.CS.Aero, 1)

# TODO: TEST
def getLiftRear(car=0):
    return ac.getCarState(car, acsys.CS.Aero, 2)