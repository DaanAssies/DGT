import os
import sys
import ac
import acsys

sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + 'shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."

from functions.shared_memory import info


def get_has_drs() -> int:
    """
    Retrieves if the current car driven has DRS
    :return: 0 if no DRS, 1 if there is DRS
    """
    return info.static.hasDRS


def get_has_ers() -> int:
    """
    Retrieves if the current car driven has ERS
    :return: 0 if no ERS, 1 if there is ERS
    """
    return info.static.hasERS


def get_has_kers() -> int:
    """
    Retrieves if the current car has KERS
    :return: 0 if no KERS, 1 if there is KERS
    """
    return info.static.hasKERS


def abs_level() -> int:
    """
    Retrieves the ABS level active for the current car (seems to be buggy)
    :return: value between 0 and 1, the higher, the stronger the ABS
    """
    return info.physics.abs


def get_max_rpm() -> int:
    """
    Retrieves the Maximum RPM of a car
    :return: the maximum RPM
    """
    if info.static.maxRpm:
        return info.static.maxRpm
    else:
        return 1000000


def get_max_fuel() -> int:
    """
    Retrieves the maximum fuel of car
    :return: the maximum fuel (in KG (or maybe even Liters))
    """
    return info.static.maxFuel
