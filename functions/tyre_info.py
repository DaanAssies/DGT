import os
import sys
import ac
import acsys

sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + 'shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."

from functions.shared_memory import info

"""
0 = FL, 1 = FR, 2 = RL, 3 = RR
"""


def get_tyre_wear_value(tyre: int) -> float:
    """
    Retrieve tyre wear of a tyre. 100 is mint condition, 0 is fully worn (puncture)
    :param tyre: int [0,3]
    :return: tyre wear [0,100]
    """
    return info.physics.tyreWear[tyre]


def get_tyre_dirty(tyre: int) -> float:
    """
    Retrieve "dirty level" or a tyre. 0 is clean, 5 is most dirty
    :param tyre: int [0,3]
    :return: dirty level [0,5]
    """
    return info.physics.tyreDirtyLevel[tyre]


def get_tyre_temp(tyre: int, loc: str) -> float:
    """
    Retrieve temperature of a tyre in a location
    :param tyre: int [0,3]
    :param loc: "i" is inner, "m" is middle, "o" is outer, "c" is core temperatures
    :return: temperature of tyre in location
    """
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


def get_tyre_pressure(tyre: int) -> float:
    """
    Retrieve tyre pressure of a tyre
    :param tyre: int [0,3]
    :return: tyre pressure
    """
    return info.physics.wheelsPressure[tyre]

# Stays 26.0 for some reason
def get_brake_temp(loc: int) -> float:
    """
    Retrieve temperature of a brake
    :param loc: [0,3]
    :return: brake temperature
    """
    return info.physics.brakeTemp[loc]

# Slip ratio, between 0 and 1
def getSlipRatio(car=0):
    return ac.getCarState(car, acsys.CS.SlipRatio)

# Angle of slip
def getslipAngle(car=0):
    return ac.getCarState(car, acsys.CS.SlipAngle)
