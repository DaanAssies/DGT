import os
import sys
import ac
import acsys

sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + 'shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."

from functions.shared_memory import info


# returns type ACC_SESSION_TYPE
# For some reason this only works after x amount of ticks after loading into the game. It returns 0 before that.
def get_session_type():
    """
    Retrieve session type. unknown = -1, practice = 0, qualifying = 1, race = 2, hotlap = 3, timeattack = 4, rest irr
    unknown = -1, practice = 0, qualifying = 1, race = 2, hotlap = 3, timeattack = 4, rest irrelevant
    :return: type ACC_SESSION_TYPE current session type
    """
    return info.graphics.session


def get_driver_name(car: int = 0) -> str:
    """
    Retrieve nickname of the driver of a car
    :param car: the car selected (user is 0)
    :return: driver name
    """
    return ac.get_driver_name(car)


def get_car_name(car: int = 0) -> str:
    """
    Retrieve name of a car. Car type (e.g. La Ferrari)
    :param car: the car selected (user is 0)
    :return: car name
    """
    return ac.getCarName(car)


def get_track_name() -> str:
    """
    Retrieve name of the current track driven
    :return: track driven
    """
    return ac.getTrackName(0)


def get_track_config() -> str:
    """
    Retrieve configuration of track driven
    :return: configuration of track
    """
    return ac.getTrackConfiguration(0)


def get_track_length() -> float:
    """
    Retrieve the track length
    :return: track length in m
    """
    return ac.getTrackLength(0)


def get_cars_count() -> int:
    """
    Retrieve session's max number of cars
    :return: maximum car count in current session
    """
    return ac.getCarsCount()


def get_session_status() -> int:
    """
    Retrieve the status of current session 0=OFF, 1= REPLAY, 2=LIVE, 3=PAUSE
    :return: session status
    """
    return info.graphics.status

# in KG
def get_car_ballast(car: int = 0) -> int:
    return ac.getCarBallast(car)

# In radians
def get_caster(car: int = 0):
    return ac.getCarState(car, acsys.CS.Caster)

# Radius of each tyre [0, ...]. I return just one tyre because it should be the same for all tyres
def get_radius(car: int = 0):
    return ac.getCarState(car, acsys.CS.TyreRadius)[0]

def get_car_min_height(car: int = 0) -> int:
    return ac.getCarMinHeight(car)

def get_car_ffb() -> int:
    return ac.getCarFFB()
