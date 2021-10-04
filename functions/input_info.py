import os
import sys
import ac
import acsys

sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + 'shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."

from functions.shared_memory import info


# TODO: TEST
def getGasInput(car=0):
    return ac.getCarState(car, acsys.CS.Gas)

# TODO: TEST
def getBrakeInput(car=0):
    return ac.getCarState(car, acsys.CS.Brake)

# TODO: TEST
def getClutchInput(car=0):
    return ac.getCarState(car, acsys.CS.Clutch)

# TODO: TEST
# In radians [-2pi, 2pi]
def getSteerInput(car=0):
    return ac.getCarState(car, acsys.CS.Steer)

# TODO: TEST
def getCurrentGear(car=0):
    return ac.getCarState(car, acsys.CS.Gear)

# TODO: TEST
def getCarDamage(loc="front"):
    if loc == "front":
        return info.physics.carDamage[0]
    elif loc == "rear":
        return info.physics.carDamage[1]
    elif loc == "left":
        return info.physics.carDamage[2]
    elif loc == "right":
        return info.physics.carDamage[3]
    else:
        # Centre
        return info.physics.carDamage[4]
