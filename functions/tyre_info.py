import os
import sys
import ac
import acsys
from functions.shared_memory import info

sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + '/../shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."


# 0 = FL, 1 = FR, 2 = RL, 3 = RR
# TODO: TEST ALL
# TODO: Might want a check that values do not exceed 3
# TODO: Check value, might need some calculation
def getTyreWearValue(tyre):
    return info.physics.tyreWear[tyre]

def getTyreDirtyLevel(tyre):
    return info.physics.TyreDirtyLevel[tyre]

def getTyreTemperature(tyre, loc):
    # Inner
    if loc == "i":
        return info.physics.tyreTempI[tyre]
    # Middle
    elif loc == "m":
        return info.physics.tyreTempM[tyre]
    # Outer
    elif loc == "o":
        return info.physics.tyreTempO[tyre]
    # Core
    elif loc == "c":
        return info.physics.tyreCoreTemperature[tyre]

def getTyrePressure(tyre):
    return info.physics.wheelsPressure[tyre]

def getBrakeTemperature(loc):
    return info.physics.brakeTemp[loc]