import sys
import ac
import acsys
import time
# import functions.car_data as cf

try:
    import functions.car_data as cf
except:
    ac.console("ERROR IMPORTING")

car_id = 0


def acMain(ac_version):
    # GLOBAL VARIABLES FOR LABELS ON THE DISPLAY
    global l_car_speed, l_delta_ahead, l_delta_behind, l_location, l_world_location
    # GLOBAL VARIABLES FOR SESSION DATA
    global car_name, driver_name, track_name, track_config, track_length, session_type, car_count
    # GLOBAL VARIABLES FOR CAR INFO
    global has_drs
    # GLOBAL VARIABLES FOR LAP INFO
    global is_invalid

    # Set the session variables
    driver_name = cf.SESSIONINFO.getDriverName(car_id)
    car_name = cf.SESSIONINFO.getCarName(car_id)
    track_name = cf.SESSIONINFO.getTrackName()
    track_config = cf.SESSIONINFO.getTrackConfig()
    track_length = cf.SESSIONINFO.getTrackLength()
    session_type = cf.SESSIONINFO.getSessionType()
    # Set the car info variables
    has_drs = cf.CARSTATS.getHasDRS()
    car_count = cf.SESSIONINFO.getCarsCount()

    # TEST ZONE
    #############
    ac.console(str(driver_name))
    ac.console("Car count: " + str(car_count))
    ##############

    display = ac.newApp("1testapp")
    ac.setSize(display, 300, 300)

    # Display settings for testing
    # Increase the third variable of ac.setPosition() by 30 for every variable added
    l_car_speed = ac.addLabel(display, "Speed: ()")
    l_delta_ahead = ac.addLabel(display, "Delta to car ahead: ()")
    l_delta_behind = ac.addLabel(display, "Delta to car behind: ()")
    l_location = ac.addLabel(display, "Track relative position: ()")
    l_world_location = ac.addLabel(display, "World precise position: ()")
    ac.setPosition(l_car_speed, 3, 30)
    ac.setPosition(l_delta_ahead, 3, 60)
    ac.setPosition(l_delta_behind, 3, 90)
    ac.setPosition(l_location, 3, 120)
    ac.setPosition(l_world_location, 3, 150)

    return "1testapp"


def acUpdate(deltaT):
    # GLOBAL VARIABLES FOR LABELS ON THE DISPLAY
    global l_car_speed, l_delta_ahead, l_delta_behind, l_location, l_world_location
    # GLOBAL VARIABLES FOR TRACK CONDITIONS
    global wind_speed, wind_dir
    # GLOBAL VARIABLES FOR CAR INFO
    global car_speed, car_gas, rpm, delta_ahead, delta_behind, location, world_location
    # GLOBAL VARIABLES FOR LAP TIMES
    global current_lap, last_lap, best_lap, splits, lap_count, is_invalid, split

    # Car info functions called
    car_speed = cf.CARINFO.getSpeed(car_id)
    car_gas = cf.INPUTINFO.getGasInput(car_id)
    rpm = cf.CARINFO.getRPM(car_id)
    delta_ahead = cf.CARINFO.getDeltaToCarAhead(True)
    delta_behind = cf.CARINFO.getDeltaToCarBehind(True)
    location = cf.CARINFO.getLocation(car_id)
    world_location = cf.CARINFO.getWorldLocation()

    # Lap info functions called
    current_lap = cf.LAPINFO.getCurrentLapTime(car_id, True)
    last_lap = cf.LAPINFO.getLastLapTime(car_id, True)
    best_lap = cf.LAPINFO.getBestLapTime(car_id, True)
    splits = cf.LAPINFO.getSplits(car_id, True)
    lap_count = cf.LAPINFO.getLapCount(car_id)
    lap_delta = cf.LAPINFO.getLapDelta(car_id)
    is_invalid = cf.LAPINFO.getInvalid(car_id)
    split = cf.LAPINFO.getSplit()

    # Live display
    ac.setText(l_car_speed, "Speed: {}".format(car_speed))
    ac.setText(l_delta_ahead, "Delta to car ahead: {}".format(delta_ahead))
    ac.setText(l_delta_behind, "Delta to car behind: {}".format(delta_behind))
    ac.setText(l_location, "Track relative position: {}".format(location))
    ac.setText(l_world_location, "World precise position: {}".format(world_location))

