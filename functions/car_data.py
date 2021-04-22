import sys
import ac
import acsys


def formatTime(millis):
    m = int(millis / 60000)
    s = int((millis % 60000) / 1000)
    ms = millis % 1000

    return "{:02d}:{:02d}.{:03d}".format(m, s, ms)


class SESSIONINFO:
    @staticmethod
    def getDriverName(car):
        return ac.getDriverName(car)

    @staticmethod
    def getCarName(car):
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

    # WIND IS NOT A FUNCTION IN ac PACKAGE
    # @staticmethod
    # def getWindSpeed():
    #     return ac.getWindSpeed()
    #
    # @staticmethod
    # def getWindDir():
    #     return ac.getWindDirection()

    @staticmethod
    def getCarsCount():
        return ac.getCarsCount


class LAPINFO:

    @staticmethod
    def getCurrentLapTime(car):
        return ac.getCarState(car, acsys.CS.LapTime)

    @staticmethod
    def getLastLapTime(car):
        return ac.getCarState(car, acsys.CS.LastLap)

    @staticmethod
    def getBestLapTime(car):
        return ac.getCarState(car, acsys.CS.BestLap)

    @staticmethod
    def getSplits(car):
        return ac.getLastSplits(car)

    # TODO: Check whether invalidated value is 1 or 0
    # TODO: TEST
    @staticmethod
    def getInvalid(car):
        if ac.getCarState(car, acsys.CS.LapInvalidated) == 1:
            return True
        else:
            return False

    # FORMATTED LAP DATA FROM FUNCTIONS ABOVE, same function names but with an F appended
    # TODO: Set formatting as option in functions above
    ###############
    @staticmethod
    def getCurrentLapTimeF(car):
        time = ac.getCarState(car, acsys.CS.LapTime)
        if time > 0:
            return formatTime(time)
        else:
            return "--:--"

    @staticmethod
    def getLastLapTimeF(car):
        time = ac.getCarState(car, acsys.CS.LastLap)
        if time > 0:
            return formatTime(time)
        else:
            return "--:--"

    @staticmethod
    def getBestLapTimeF(car):
        time = ac.getCarState(car, acsys.CS.BestLap)
        if time > 0:
            return formatTime(time)
        else:
            return "--:--"

    # Sector times of last lap
    @staticmethod
    def getSplitsF(car):
        times = ac.getLastSplits(car)
        formattedtimes = []

        if len(times) != 0:
            ac.console("lol")
            for t in times:
                formattedtimes.append(formatTime(t))
            return formattedtimes
        else:
            return "--:--"
    ##############

    @staticmethod
    def getLapCount(car):
        return ac.getCarState(car, acsys.CS.LapCount) + 1

    # Delta to fastest lap
    @staticmethod
    def getLapDelta(car):
        return ac.getCarState(car, acsys.CS.PerformanceMeter)


class CARINFO:
    @staticmethod
    def getSpeed(car, unit="kmh"):
        if unit == "kmh":
            return ac.getCarState(car, acsys.CS.SpeedKMH)
        elif unit == "mph":
            return ac.getCarState(car, acsys.CS.SpeedMPH)
        elif unit == "ms":
            return ac.getCarState(car, acsys.CS.SpeedMS)

    # TODO: TEST
    @staticmethod
    def getDeltaToPrevCar(formatted=False):
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

    # TODO: TEST
    @staticmethod
    def getDeltaToNextCar(formatted=False):
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

    # TODO: TEST
    @staticmethod
    def getLocation(car):
        return ac.getCarState(car, acsys.CS.NormalizedSplinePosition)

    # TODO: TEST
    @staticmethod
    def getGasInput(car):
        return ac.getCarState(car, acsys.CS.Gas)

    # TODO: TEST
    @staticmethod
    def getBrakeInput(car):
        return ac.getCarState(car, acsys.CS.Brake)

    # TODO: TEST
    @staticmethod
    def getClutchInput(car):
        return ac.getCarState(car, acsys.CS.Clutch)

    # TODO: TEST
    # In radians [-2pi, 2pi]
    @staticmethod
    def getSteerInput(car):
        return ac.getCarState(car, acsys.CS.Steer)

    # TODO: TEST
    @staticmethod
    def getCurrentGear(car):
        return ac.getCarState(car, acsys.CS.Gear)

    # TODO: TEST
    @staticmethod
    def getPosition(car):
        return ac.getCarRealTimeLeaderboardPosition(car) + 1
