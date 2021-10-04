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
def getHasDRS():
    return info.static.hasDRS

# TODO: TEST
def getHasERS():
    return info.static.hasERS

# TODO: TEST
def getHasKERS():
    return info.static.hasKERS

# TODO: TEST
def ABS():
    return info.physics.abs
