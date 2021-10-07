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

# Leading car is in position 0
def getPosition(car):
    return ac.getCarRealTimeLeaderboardPosition(car) + 1

# 0 if disabled, 1 if enabled
def getDRSEnabled():
    return info.physics.drsEnabled

# Formatted: 0=R, 1=N, 2=1, 3=2, 4=3, 5=4, 6=5, 7=6, 8=7, etc.
def getFormattedGear(car=0, formatted=True):
    gear = ac.getCarState(car, acsys.CS.Gear)
    if formatted:
        if gear == 0:
            return "R"
        elif gear == 1:
            return "N"
        else:
            return str(gear - 1)
    else:
        return gear

def getRPM(car=0):
    return ac.getCarState(car, acsys.CS.RPM)

# Amount of fuel in the car in KGs
def getFuel():
    return info.physics.fuel

# Returns the amount of tyres off-track

def getTyresOut():
    return info.physics.numberOfTyresOut

def getCarInPit():
    return info.graphics.isInPitLane


# Damage numbers go up to a high number. A slight tap results in a damage value of about 10
def getCarDamage(loc="front"):
    if loc == "front":
        return info.physics.carDamage[0]
    elif loc == "rear":
        return info.physics.carDamage[1]
    elif loc == "left":
        return info.physics.carDamage[2]
    elif loc == "right":
        return info.physics.carDamage[3]
    else:
        # Centre
        return info.physics.carDamage[4]
