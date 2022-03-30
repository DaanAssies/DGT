import os
import sys
import ac
import acsys

sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + 'shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."

from functions.shared_memory import info

# 0 = FL, 1 = FR, 2 = RL, 3 = RR

# 100 is best, 0 is fully worn (puncture)
def getTyreWearValue(tyre):
    return info.physics.tyreWear[tyre]

# 0 is clean, 5 is most dirty.
def getTyreDirtyLevel(tyre):
    return info.physics.tyreDirtyLevel[tyre]

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

# Stays 26.0 for some reason
def getBrakeTemperature(loc):
    return info.physics.brakeTemp[loc]

# Slip ratio, between 0 and 1
def getSlipRatio(car=0):
    return ac.getCarState(car, acsys.CS.SlipRatio)

# Angle of slip
def getslipAngle(car=0):
    return ac.getCarState(car, acsys.CS.SlipAngle)
