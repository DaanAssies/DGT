import os
import sys
import ac
import acsys

sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + 'shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."


def get_gas_input(car: int = 0) -> float:
    """
    Retrieve the gas input given to a car
    :param car: the car selected (user is 0)
    :return: gas input between 0 and 1
    """
    return ac.getCarState(car, acsys.CS.Gas)


def get_brake_input(car: int = 0) -> float:
    """
    Retrieve the brake input given to a car
    :param car: the car selected (user is 0)
    :return: brake input between 0 and 1
    """
    return ac.getCarState(car, acsys.CS.Brake)


def get_clutch(car: int = 0) -> float:
    """
    Retrieve the clutch status in the game of a car
    :param car: the car selected (user is 0)
    :return: deployment of the clutch (1 is fully deployed, 0 is not deployed).
    """
    return ac.getCarState(car, acsys.CS.Clutch)


def get_steer_input(car: int = 0) -> float:
    """
    Retrieve the steering input given to a car
    :param car: the car selected (user is 0)
    :return: steering input to the car, depends on the settings in AC, in degrees
    """
    return ac.getCarState(car, acsys.CS.Steer)

# Test on not laptop [0, ...]
def get_last_ff(car: int = 0) -> float:
    return ac.getCarState(car, acsys.CS.LastFF)
