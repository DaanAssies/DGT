import os
import sys
import ac
import acsys

sysdir = os.path.dirname(__file__) + '/../stdlib64'
sys.path.insert(0, sysdir)
sys.path.insert(0, os.path.dirname(__file__) + '/../shared_memory')
os.environ['PATH'] = os.environ['PATH'] + ";."

from shared_memory.sim_info import info


def formatTime(millis):
    m = int(millis / 60000)
    s = int((millis % 60000) / 1000)
    ms = millis % 1000

    return "{:02d}:{:02d}.{:03d}".format(m, s, ms)


def formatGear(gear):
    if gear == 0:
        return "R"
    elif gear == 1:
        return "N"
    else:
        return str(gear - 1)


class SESSIONINFO:
    # returns type ACC_SESSION_TYPE
    # unknown = -1, practice = 0, qualifying = 1, race = 2, hotlap = 3, timeattack = 4, rest irrelevant
    # For some reason this only works after x amount of ticks after loading into the game. It returns 0 before that.
    @staticmethod
    def getSessionType():
        return info.graphics.session

    @staticmethod
    def getDriverName(car=0):
        return ac.getDriverName(car)

    @staticmethod
    def getCarName(car=0):
        return ac.getCarName(car)

    @staticmethod
    def getTrackName():
        return ac.getTrackName(0)

    @staticmethod
    def getTrackConfig():
        return ac.getTrackConfiguration(0)

    @staticmethod
    def getTrackLength():
        return ac.getTrackLength(0)

    # Returns session's max no. of cars
    @staticmethod
    def getCarsCount():
        return ac.getCarsCount()

    # Returns the session status. 0=OFF, 1= REPLAY, 2=LIVE, 3=PAUSE
    @staticmethod
    def getSessionStatus():
        return info.graphics.status


class LAPINFO:
    @staticmethod
    def getCurrentLapTime(car=0, formatted=False):
        if formatted:
            time = ac.getCarState(car, acsys.CS.LapTime)
            if time > 0:
                return formatTime(time)
            else:
                return "--:--"
        else:
            return ac.getCarState(car, acsys.CS.LapTime)

    @staticmethod
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
    @staticmethod
    def getBestLapTime(car=0, formatted=False):
        if formatted:
            time = ac.getCarState(car, acsys.CS.BestLap)
            if time > 0:
                return formatTime(time)
            else:
                return "--:--"
        else:
            return ac.getCarState(car, acsys.CS.BestLap)

    @staticmethod
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
    @staticmethod
    def getSplit():
        return info.graphics.split

    # False when lap counts, True when lap doesn't count.
    # Updates live so needs a check every lap whether there was a True value.
    @staticmethod
    def getInvalid(car=0):
        return ac.getCarState(car, acsys.CS.LapInvalidated) or CARINFO.getTyresOut() > 2

    @staticmethod
    def getLapCount(car=0):
        return ac.getCarState(car, acsys.CS.LapCount) + 1

    # Returns the total number of laps in the race
    @staticmethod
    def getLaps():
        if info.graphics.numberOfLaps > 0:
            return info.graphics.numberOfLaps
        else:
            return "-"

    # Delta to fastest lap
    @staticmethod
    def getLapDelta(car=0):
        return ac.getCarState(car, acsys.CS.PerformanceMeter)


class CARINFO:
    @staticmethod
    def getSpeed(car=0, unit="kmh"):
        if unit == "kmh":
            return ac.getCarState(car, acsys.CS.SpeedKMH)
        elif unit == "mph":
            return ac.getCarState(car, acsys.CS.SpeedMPH)
        elif unit == "ms":
            return ac.getCarState(car, acsys.CS.SpeedMS)

    @staticmethod
    def getDeltaToCarAhead(formatted=False):
        time = 0
        dist = 0
        track_len = SESSIONINFO.getTrackLength()
        lap = LAPINFO.getLapCount(0)
        pos = CARINFO.getLocation(0)

        for car in range(SESSIONINFO.getCarsCount()):
            if CARINFO.getPosition(car) == CARINFO.getPosition(0) - 1:
                lap_next = LAPINFO.getLapCount(car)
                pos_next = CARINFO.getLocation(car)

                dist = max(0, (pos_next * track_len + lap_next * track_len) - (pos * track_len + lap * track_len))
                time = max(0.0, dist / max(10.0, CARINFO.getSpeed(0, "ms")))
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

    @staticmethod
    def getDeltaToCarBehind(formatted=False):
        time = 0
        dist = 0
        track_len = SESSIONINFO.getTrackLength()
        lap = LAPINFO.getLapCount(0)
        pos = CARINFO.getLocation(0)
        for car in range(SESSIONINFO.getCarsCount()):
            if CARINFO.getPosition(car) == CARINFO.getPosition(0) + 1:
                lap_next = LAPINFO.getLapCount(car)
                pos_next = CARINFO.getLocation(car)

                dist = max(0, (pos * track_len + lap * track_len) - (pos_next * track_len + lap_next * track_len))
                time = max(0.0, dist / max(10.0, CARINFO.getSpeed(car, "ms")))
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
    @staticmethod
    def getLocation(car=0):
        return ac.getCarState(car, acsys.CS.NormalizedSplinePosition)

    # Gets the location of the car in [x,y,z] coordinates, x=0,z=0 is middle
    @staticmethod
    def getWorldLocation(car=0):
        return ac.getCarState(car, acsys.CS.WorldPosition)

    # TODO: TEST
    @staticmethod
    def getPosition(car):
        return ac.getCarRealTimeLeaderboardPosition(car) + 1

    # TODO: TEST
    @staticmethod
    def getDRSEnabled():
        return info.physics.drsEnabled

    # TODO: TEST
    @staticmethod
    def getFormattedGear(car=0):
        return formatGear(ac.getCarState(car, acsys.CS.Gear))

    # TODO: TEST
    @staticmethod
    def getRPM(car=0):
        return ac.getCarState(car, acsys.CS.RPM)

    # TODO: TEST
    @staticmethod
    def getRPMMax():
        if info.static.maxRpm:
            return info.static.maxRpm
        else:
            return 8000

    # TODO: TEST
    @staticmethod
    def getFuel():
        return info.physics.fuel

    # TODO: TEST
    @staticmethod
    def getMaxFuel():
        return info.static.maxFuel

    # Returns the amount of tyres off-track
    @staticmethod
    def getTyresOut():
        return info.physics.numberOfTyresOut

    @staticmethod
    def getCarInPit():
        return info.graphics.isInPitLane

class CARSTATS:
    # TODO: TEST
    @staticmethod
    def getHasDRS():
        return info.static.hasDRS

    # TODO: TEST
    @staticmethod
    def getHasERS():
        return info.static.hasERS

    # TODO: TEST
    @staticmethod
    def getHasKERS():
        return info.static.hasKERS

    # TODO: TEST
    @staticmethod
    def ABS():
        return info.physics.abs


class INPUTINFO:
    # TODO: TEST
    @staticmethod
    def getGasInput(car=0):
        return ac.getCarState(car, acsys.CS.Gas)

    # TODO: TEST
    @staticmethod
    def getBrakeInput(car=0):
        return ac.getCarState(car, acsys.CS.Brake)

    # TODO: TEST
    @staticmethod
    def getClutchInput(car=0):
        return ac.getCarState(car, acsys.CS.Clutch)

    # TODO: TEST
    # In radians [-2pi, 2pi]
    @staticmethod
    def getSteerInput(car=0):
        return ac.getCarState(car, acsys.CS.Steer)

    # TODO: TEST
    @staticmethod
    def getCurrentGear(car=0):
        return ac.getCarState(car, acsys.CS.Gear)

    # TODO: TEST
    @staticmethod
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
            return info.physics.carDamage[4]

class AEROINFO:
    # Methods in this class return a scalar vector
    # TODO: TEST
    @staticmethod
    def getDrag(car=0):
        return ac.getCarState(car, acsys.CS.Aero, 0)

    # TODO: TEST
    @staticmethod
    def getLiftFront(car=0):
        return ac.getCarState(car, acsys.CS.Aero, 1)

    # TODO: TEST
    @staticmethod
    def getLiftRear(car=0):
        return ac.getCarState(car, acsys.CS.Aero, 2)

class TYREINFO:
    # TODO: TEST ALL
    @staticmethod
    def getTyreWear():
        return info.physics.tyreWear
