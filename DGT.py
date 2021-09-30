import sys
import ac
import acsys
import time
import os

# try:
import functions.aero_info as ai
import functions.car_info as ci
import functions.car_stats as cs
import functions.input_info as ii
import functions.lap_info as li
import functions.session_info as si
import functions.tyre_info as ti
# except:
#     ac.console("ERROR IMPORTING")

car_id = 0


def acMain(ac_version):
    # GLOBAL VARIABLES FOR LABELS ON THE DISPLAY
    global l_car_speed, l_delta_ahead, l_delta_behind, l_location, l_world_location, l_session_status
    # GLOBAL VARIABLES FOR SESSION DATA
    global car_name, driver_name, track_name, track_config, track_length, session_type, car_count
    # GLOBAL VARIABLES FOR CAR INFO
    global has_drs
    # GLOBAL VARIABLES FOR LAP INFO
    global is_invalid

    # Set the session variables
    driver_name = si.getDriverName(car_id)
    car_name = si.getCarName(car_id)
    track_name = si.getTrackName()
    track_config = si.getTrackConfig()
    track_length = si.getTrackLength()
    session_type = si.getSessionType()
    # Set the car info variables
    has_drs = cs.getHasDRS()
    car_count = si.getCarsCount()

    # TEST ZONE
    #############
    # ac.console(str(driver_name))
    # ac.console("Car count: " + str(car_count))
    ##############

    display = ac.newApp("DGT")
    ac.setSize(display, 300, 300)

    # Display settings for testing
    # Increase the third variable of ac.setPosition() by 30 for every variable added
    l_car_speed = ac.addLabel(display, "Speed: ()")
    l_delta_ahead = ac.addLabel(display, "Delta to car ahead: ()")
    l_delta_behind = ac.addLabel(display, "Delta to car behind: ()")
    l_location = ac.addLabel(display, "Track relative position: ()")
    l_world_location = ac.addLabel(display, "World precise position: ()")
    l_session_status = ac.addLabel(display, "Session status: ()")
    ac.setPosition(l_car_speed, 3, 30)
    ac.setPosition(l_delta_ahead, 3, 60)
    ac.setPosition(l_delta_behind, 3, 90)
    ac.setPosition(l_location, 3, 120)
    ac.setPosition(l_world_location, 3, 150)
    ac.setPosition(l_session_status, 3, 180)

    # Clear output files
    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/lap.txt', 'w') as f:
        f.write("\n")
    f.close()
    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/car.txt', 'w') as f:
        f.write("\n")
    f.close()
    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/input.txt', 'w') as f:
        f.write("\n")
    f.close()



    return "DGT"


def acUpdate(deltaT):
    global session_status
    # GLOBAL VARIABLES FOR LABELS ON THE DISPLAY
    global l_car_speed, l_delta_ahead, l_delta_behind, l_location, l_world_location, l_session_status
    # GLOBAL VARIABLES FOR TRACK CONDITIONS
    global wind_speed, wind_dir
    # GLOBAL VARIABLES FOR INPUT
    global gas_input, brake_input, steer_input
    # GLOBAL VARIABLES FOR CAR INFO
    global car_speed,  rpm, delta_ahead, delta_behind, location, world_location
    # GLOBAL VARIABLES FOR LAP TIMES
    global current_lap, last_lap, best_lap, splits, lap_count, is_invalid, split, track_pos

    ts = round(time.time() * 1000)

    session_status = si.getSessionStatus()
    # ac.console(str(session_status))

    # Input info functions called
    gas_input = ii.getGasInput(car_id)
    brake_input = ii.getBrakeInput(car_id)
    steer_input = ii.getSteerInput(car_id)

    dInputInfo = {
        "flag": 0,
        "gas": gas_input,
        "brake": brake_input,
        "steering": steer_input,
        "timestamp": ts
    }

    # Car info functions called
    car_speed = ci.getSpeed(car_id)
    # ac.console(car_speed)
    rpm = ci.getRPM(car_id)
    delta_ahead = ci.getDeltaToCarAhead(True)
    delta_behind = ci.getDeltaToCarBehind(True)
    location = ci.getLocation(car_id)
    world_location = ci.getWorldLocation()
    is_in_pit = ci.getCarInPit()

    dCarInfo = {
        "flag": 1,
        "timestamp": ts,
        "car_speed": car_speed,
        "rpm": rpm}

    # Lap info functions called
    current_lap = li.getCurrentLapTime(car_id)
    last_lap = li.getLastLapTime(car_id, True)
    best_lap = li.getBestLapTime(car_id, True)
    splits = li.getSplits(car_id, True)
    lap_count = li.getLapCount(car_id)
    lap_delta = li.getLapDelta(car_id)
    is_invalid = li.getInvalid(car_id)
    split = li.getSplit()
    lap_pos = ci.getLocation(car_id)

    dLapInfo = {
        "lap_position": lap_pos,
        "flag": 2,
        "timestamp": ts,
        "current": current_lap,
        "last": last_lap,
        "best": best_lap,
        "splits": splits,
        "invalid:": str(is_invalid)
    }
    if session_status == 2 and not is_in_pit:
        with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/TestData/lap.txt', 'a') as lap_file:
            lap_file.write((str(dLapInfo)))
            lap_file.write("\n")
            lap_file.close()
        with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/TestData/input.txt', 'a') as lap_file:
            lap_file.write((str(dInputInfo)))
            lap_file.write("\n")
            lap_file.close()
        with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/TestData/car.txt', 'a') as lap_file:
            lap_file.write((str(dCarInfo)))
            lap_file.write("\n")
            lap_file.close()

    # # Clear py.log to make sure it does not reach 2000 lines limit
    # with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/py_log.txt', 'r+') as py_log:
    #     py_log.truncate(124)
    #     py_log.close()

    # Live display
    ac.setText(l_car_speed, "Speed: {}".format(car_speed))
    ac.setText(l_delta_ahead, "Delta to car ahead: {}".format(delta_ahead))
    ac.setText(l_delta_behind, "Delta to car behind: {}".format(delta_behind))
    ac.setText(l_location, "Track relative position: {}".format(location))
    ac.setText(l_world_location, "World precise position: {}".format(world_location))
    ac.setText(l_session_status, "Session status: {}".format(session_status))

