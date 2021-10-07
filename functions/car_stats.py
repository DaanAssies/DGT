import os
import sys
import ac
import acsys

sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + 'shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."

from functions.shared_memory import info

# 0 if no, 1 if yes
def getHasDRS():
    return info.static.hasDRS

# 0 if no, 1 if yes
def getHasERS():
    return info.static.hasERS

# 0 if no, 1 if yes
def getHasKERS():
    return info.static.hasKERS

# abs level
def ABSLevel():
    return info.physics.abs


# Returns 1000000 if the car does not have this statistic
def getMaxRPM():
    if info.static.maxRpm:
        return info.static.maxRpm
    else:
        return 1000000

# Maximum fuel in KGs
def getMaxFuel():
    return info.static.maxFuel
