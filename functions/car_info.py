import os
import sys
import ac
import acsys
from functions.shared_memory import info


sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + '/../shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."


def formatGear(gear):
    if gear == 0:
        return "R"
    elif gear == 1:
        return "N"
    else:
        return str(gear - 1)

def formatTime(millis):
    m = int(millis / 60000)
    s = int((millis % 60000) / 1000)
    ms = millis % 1000

    return "{:02d}:{:02d}.{:03d}".format(m, s, ms)


def getSpeed(car=0, unit="kmh"):
    if unit == "kmh":
        return ac.getCarState(car, acsys.CS.SpeedKMH)
    elif unit == "mph":
        return ac.getCarState(car, acsys.CS.SpeedMPH)
    elif unit == "ms":
        return ac.getCarState(car, acsys.CS.SpeedMS)

def getDeltaToCarAhead(formatted=False):
    import functions.session_info as si
    import functions.lap_info as li
    time = 0
    dist = 0
    track_len = si.getTrackLength()
    lap = li.getLapCount(0)
    pos = getLocation(0)

    for car in range(si.getCarsCount()):
        if getPosition(car) == getPosition(0) - 1:
            lap_next = li.getLapCount(car)
            pos_next = getLocation(car)

            dist = max(0, (pos_next * track_len + lap_next * track_len) - (pos * track_len + lap * track_len))
            time = max(0.0, dist / max(10.0, getSpeed(0, "ms")))
            break

    if not formatted:
        return time
    else:
        if dist > track_len:
            laps = dist / track_len
            if laps > 1:
                return "+{:3.1f}".format(laps) + " Laps"
            else:
                return "+{:3.1f}".format(laps) + " Lap"
        elif time > 60:
            return "+" + formatTime(int(time * 1000))
        else:
            return "+{:3.3f}".format(time)

def getDeltaToCarBehind(formatted=False):
    import functions.session_info as si
    import functions.lap_info as li
    time = 0
    dist = 0
    track_len = si.getTrackLength()
    lap = li.getLapCount(0)
    pos = getLocation(0)
    for car in range(si.getCarsCount()):
        if getPosition(car) == getPosition(0) + 1:
            lap_next = li.getLapCount(car)
            pos_next = getLocation(car)

            dist = max(0, (pos * track_len + lap * track_len) - (pos_next * track_len + lap_next * track_len))
            time = max(0.0, dist / max(10.0, getSpeed(car, "ms")))
            break

    if not formatted:
        return time
    else:
        if dist > track_len:
            laps = dist / track_len
            if laps > 1:
                return "-{:3.1f}".format(laps) + " Laps"
            else:
                return "-{:3.1f}".format(laps) + " Lap"
        elif time > 60:
            return "-" + formatTime(int(time * 1000))
        else:
            return "-{:3.3f}".format(time)

# Gets the position of the car on track. 0 is the start/finish line [0,1]
def getLocation(car=0):
    return ac.getCarState(car, acsys.CS.NormalizedSplinePosition)

# Gets the location of the car in [x,y,z] coordinates, x=0,z=0 is middle
def getWorldLocation(car=0):
    return ac.getCarState(car, acsys.CS.WorldPosition)

# TODO: TEST
def getPosition(car):
    return ac.getCarRealTimeLeaderboardPosition(car) + 1

# TODO: TEST
def getDRSEnabled():
    return info.physics.drsEnabled

# TODO: TEST
def getFormattedGear(car=0):
    return formatGear(ac.getCarState(car, acsys.CS.Gear))

# TODO: TEST
def getRPM(car=0):
    return ac.getCarState(car, acsys.CS.RPM)

# TODO: TEST
def getRPMMax():
    if info.static.maxRpm:
        return info.static.maxRpm
    else:
        return 8000

# TODO: TEST
def getFuel():
    return info.physics.fuel

# TODO: TEST

def getMaxFuel():
    return info.static.maxFuel

# Returns the amount of tyres off-track

def getTyresOut():
    return info.physics.numberOfTyresOut

def getCarInPit():
    return info.graphics.isInPitLane
