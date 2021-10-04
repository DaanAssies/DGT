import os
import sys
import ac
import acsys

sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + 'shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."

from functions.shared_memory import info


def formatTime(millis):
    m = int(millis / 60000)
    s = int((millis % 60000) / 1000)
    ms = millis % 1000

    return "{:02d}:{:02d}.{:03d}".format(m, s, ms)

def getCurrentLapTime(car=0, formatted=False):
    if formatted:
        time = ac.getCarState(car, acsys.CS.LapTime)
        if time > 0:
            return formatTime(time)
        else:
            return "--:--"
    else:
        return ac.getCarState(car, acsys.CS.LapTime)

def getLastLapTime(car=0, formatted=False):
    if formatted:
        time = ac.getCarState(car, acsys.CS.LastLap)
        if time > 0:
            return formatTime(time)
        else:
            return "--:--"
    else:
        return ac.getCarState(car, acsys.CS.LastLap)

# The best lap does not safe if it was an invalidated lap
def getBestLapTime(car=0, formatted=False):
    if formatted:
        time = ac.getCarState(car, acsys.CS.BestLap)
        if time > 0:
            return formatTime(time)
        else:
            return "--:--"
    else:
        return ac.getCarState(car, acsys.CS.BestLap)

def getSplits(car=0, formatted=False):
    if formatted:
        times = ac.getLastSplits(car)
        formattedtimes = []

        if len(times) != 0:
            for t in times:
                formattedtimes.append(formatTime(t))
            return formattedtimes
        else:
            return "--:--"
    else:
        return ac.getLastSplits(car)

# Returns the last sector split to 1 decimal and returns nothing if the last sector completed a lap.
def getSplit():
    return info.graphics.split

# False when lap counts, True when lap doesn't count.
# Updates live so needs a check every lap whether there was a True value.
def getInvalid(car=0):
    import functions.car_info as ci
    return ac.getCarState(car, acsys.CS.LapInvalidated) or ci.getTyresOut() > 2

def getLapCount(car=0):
    return ac.getCarState(car, acsys.CS.LapCount) + 1

# Returns the total number of laps in the race
def getLaps():
    if info.graphics.numberOfLaps > 0:
        return info.graphics.numberOfLaps
    else:
        return "-"

# Delta to fastest lap
def getLapDelta(car=0):
    return ac.getCarState(car, acsys.CS.PerformanceMeter)
