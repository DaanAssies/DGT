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
    global l_car_speed, l_car_gas, l_wind_dir, l_wind_speed, l_current_lap, l_last_lap, l_best_lap, l_splits, l_lap_count, l_lap_delta
    # GLOBAL VARIABLES FOR SESSION DATA
    global car_name, driver_name, track_name, track_config, track_length, wind_speed, wind_dir, has_drs
    # Set the session variables
    driver_name = cf.SESSIONINFO.getDriverName(car_id)
    car_name = cf.SESSIONINFO.getCarName(car_id)
    track_name = cf.SESSIONINFO.getTrackName()
    track_config = cf.SESSIONINFO.getTrackConfig()
    track_length = cf.SESSIONINFO.getTrackLength()
    # wind_speed = cf.ACSESSION.getWindSpeed(car_id)
    # wind_dir = cf.ACSESSION.getWindDir()

    # TEST ZONE
    #############
    has_drs = cf.CARSTATS.getHasDRS()
    ac.console("Here")
    ac.console(str(has_drs))
    ac.console(str(driver_name))
    ##############

    display = ac.newApp("1testapp")
    ac.setSize(display, 300, 300)

    # Display settings for testing
    # Increase the third variable of ac.setPosition() by 30 for every variable added
    l_car_speed = ac.addLabel(display, "Speed: ()")
    l_car_gas = ac.addLabel(display, "Gas: ()")
    l_current_lap = ac.addLabel(display, "Current Lap: ()")
    l_last_lap = ac.addLabel(display, "Last Lap: ()")
    l_best_lap = ac.addLabel(display, "Best Lap: ()")
    l_splits = ac.addLabel(display, "Splits: ()")
    l_lap_count = ac.addLabel(display, "Lap count: ()")
    l_lap_delta = ac.addLabel(display, "Lap Delta: ()")
    # l_wind_dir = ac.addLabel(display, "Wind direction: ()")
    # l_wind_speed = ac.addLabel(display, "Wind speed: ()")
    ac.setPosition(l_car_speed, 3, 30)
    ac.setPosition(l_car_gas, 3, 60)
    # ac.setPosition(l_wind_dir, 3, 90)
    # ac.setPosition(l_wind_speed, 3, 120)
    ac.setPosition(l_current_lap, 3, 90)
    ac.setPosition(l_last_lap, 3, 120)
    ac.setPosition(l_best_lap, 3, 150)
    ac.setPosition(l_splits, 3, 180)
    ac.setPosition(l_lap_count, 3, 210)
    ac.setPosition(l_lap_delta, 3, 240)

    return "1testapp"


def acUpdate(deltaT):
    # GLOBAL VARIABLES FOR LABELS ON THE DISPLAY
    global l_car_speed, l_car_gas, l_wind_dir, l_wind_speed, l_current_lap, l_splits, l_lap_count, l_lap_delta
    # GLOBAL VARIABLES FOR TRACK CONDITIONS
    global wind_speed, wind_dir
    # GLOBAL VARIABLES FOR CAR STATE
    global car_speed, car_gas
    # GLOBAL VARIABLES FOR LAP TIMES
    global current_lap, last_lap, best_lap, splits, lap_count

    # wind_dir = cf.ACSESSION.getWindDir(car_id)
    # wind_speed = cf.ACSESSION.getWindSpeed(car_id)

    #Car info functions called
    curr_time = time.asctime( time.localtime(time.time()) )
    ac.log(str(curr_time))
    car_speed = cf.CARINFO.getSpeed(car_id)
    car_gas = cf.INPUTINFO.getGasInput(car_id)

    #Lap info functions called
    current_lap = cf.LAPINFO.getCurrentLapTimeF(car_id)
    last_lap = cf.LAPINFO.getLastLapTimeF(car_id)
    best_lap = cf.LAPINFO.getBestLapTimeF(car_id)
    splits = cf.LAPINFO.getSplitsF(car_id)
    lap_count = cf.LAPINFO.getLapCount(car_id)
    lap_delta = cf.LAPINFO.getLapDelta(car_id)

    #Live display
    ac.setText(l_car_speed, "Speed: {}".format(car_speed))
    ac.setText(l_car_gas, "Gas Input: {}".format(car_gas))
    ac.setText(l_current_lap, "Current Lap: {}".format(current_lap))
    ac.setText(l_last_lap, "Last Lap: {}".format(last_lap))
    ac.setText(l_best_lap, "Best Lap: {}".format(best_lap))
    ac.setText(l_splits, "Splits: {}".format(splits))
    ac.setText(l_lap_count, "Lap Count: {}".format(lap_count))
    ac.setText(l_lap_delta, "Lap Delta: {}".format(lap_delta))
    # ac.setText(l_wind_dir, "Wind Direction: {}".format(wind_dir))
    # ac.setText(l_wind_speed, "Wind Speed: {}".format(wind_speed))
