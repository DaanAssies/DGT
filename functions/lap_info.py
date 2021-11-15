import os
import sys
import ac
import acsys
from functions.shared_memory import info
from typing import Union

sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + 'shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."


def format_time(millis: int) -> str:
    """
    Format time takes an integer representing milliseconds and turns it into a readable string.
    :param millis: the amount of milliseconds
    :return: formatted string [minutes, seconds, milliseconds]
    """
    m = int(millis / 60000)
    s = int((millis % 60000) / 1000)
    ms = millis % 1000

    return "{:02d}:{:02d}.{:03d}".format(m, s, ms)


def get_current_lap_time(car: int = 0, formatted: bool = False) -> Union[int, str]:
    """
    Retrieves the current lap time of the car selected
    :param car: the car selected (user is 0)
    :param formatted: true if format should be in readable str
    :return: current lap time in milliseconds (int) or string format
    """
    if formatted:
        time = ac.getCarState(car, acsys.CS.LapTime)
        if time > 0:
            return format_time(time)
        else:
            return "--:--"
    else:
        return ac.getCarState(car, acsys.CS.LapTime)


def get_last_lap_time(car: int = 0, formatted: bool = False) -> Union[int, str]:
    """
    Retrieves the last lap time of the car selected
    :param car: the car selected (user is 0)
    :param formatted: true if format should be in readable str
    :return: last lap time in milliseconds (int) or string format
    """
    if formatted:
        time = ac.getCarState(car, acsys.CS.LastLap)
        if time > 0:
            return format_time(time)
        else:
            return "--:--"
    else:
        return ac.getCarState(car, acsys.CS.LastLap)


def get_best_lap_time(car: int = 0, formatted: bool = False) -> Union[int, str]:
    """
    Retrieve the best lap time recorded, does not save if invalidated lap
    :param car: the car selected (user is 0)
    :param formatted: true if format should be in readable str
    :return: best lap time in string format or formatted string
    """
    if formatted:
        time = ac.getCarState(car, acsys.CS.BestLap)
        if time > 0:
            return format_time(time)
        else:
            return "--:--"
    else:
        return ac.getCarState(car, acsys.CS.BestLap)


def get_splits(car: int = 0, formatted: bool = False) -> Union[list, str]:
    """
    Retrieve the split times of the completed lap
    :param car: the car selected (user is 0)
    :param formatted: true if format should be in readable str
    :return: list containing the splits in milliseconds (int) or string format
    """
    if formatted:
        times = ac.getLastSplits(car)
        formattedtimes = []

        if len(times) != 0:
            for t in times:
                formattedtimes.append(format_time(t))
            return formattedtimes
        else:
            return "--:--"
    else:
        return ac.getLastSplits(car)


def get_split() -> str:
    """
    Retrieve the last sector split, but will return nothing if the last sector is the completion of a lap
    :return: split in string format
    """
    return info.graphics.split


def get_invalid(car: int = 0) -> bool:
    """
    Retrieve if the current lap is invalid
    :param car: the car selected (user is 0)
    :return: Invalid lap in boolean form
    """
    import functions.car_info as ci

    return ac.getCarState(car, acsys.CS.LapInvalidated) or ci.get_tyres_off_track() > 2


def get_lap_count(car: int = 0) -> int:
    """
    Retrieve the current number of laps
    :param car: the car selected (user is 0)
    :return: The current number of laps (added by 1 default)
    """
    return ac.getCarState(car, acsys.CS.LapCount) + 1


def get_laps() -> str:
    """
    Returns the total number of laps in a race (only in a race)
    :return: total number of race laps
    """
    if info.graphics.numberOfLaps > 0:
        return info.graphics.numberOfLaps
    else:
        return "-"


def get_lap_delta(car: int = 0) -> float:
    """
    Retrieves the delta to the fastest lap
    :param car: the car selected (user is 0)
    :return: delta to the fastest lap in seconds (float)
    """
    return ac.getCarState(car, acsys.CS.PerformanceMeter)
