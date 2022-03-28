#################################################################################
#   NOTES TO SELF:
#   .csv ~ 3x more efficient in space:
#   ~1min of logging: .csv = 123kb, .txt = 331kb
#
#
#
#
#################################################################################

import ac
import time
import json

import functions.aero_info as ai
import functions.car_info as ci
import functions.car_stats as cs
import functions.input_info as ii
import functions.lap_info as li
import functions.session_info as si
import functions.tyre_info as ti
import dataGathering.store_csv as csv
import os
import dataGathering.store_pickle as pickle

dirname = os.path.dirname(__file__)
outputs = os.path.abspath(os.path.join(dirname, "dataGathering"))

car_id = 0
cur_time = str(round(time.time()))
json_dir = os.path.abspath(os.path.join(outputs, "out", cur_time)) + 'j'

def acMain(ac_version):
    global csvfile, writer
    # GLOBAL VARIABLES FOR LABELS ON THE DISPLAY
    global l_drag, l_lift_front, l_lift_rear
    # GLOBAL VARIABLES FOR SESSION DATA
    global car_name, driver_name, track_name, track_config, track_length, session_type, car_count
    # GLOBAL VARIABLES FOR LAP INFO
    global is_invalid
    # GLOBAL VARIABLES FOR CAR STATISTICS
    global has_drs, has_ers, has_kers, has_abs, max_rpm

    os.makedirs(json_dir)

    global inputFile
    inputFile = open(os.path.abspath(os.path.join(json_dir, "input.json")), 'w+')
    global carFile
    carFile = open(os.path.abspath(os.path.join(json_dir, "car.json")), 'w+')
    global lapFile
    lapFile = open(os.path.abspath(os.path.join(json_dir, "lap.json")), 'w+')
    global tyreFile
    tyreFile = open(os.path.abspath(os.path.join(json_dir, "tyre.json")), 'w+')

    # Set the session variables
    driver_name = si.getDriverName(car_id)
    car_name = si.getCarName(car_id)
    track_name = si.getTrackName()
    track_config = si.getTrackConfig()
    track_length = si.getTrackLength()
    session_type = si.getSessionType()
    # Set the car stats variables
    has_drs = cs.getHasDRS()
    has_ers = cs.getHasERS()
    has_kers = cs.getHasKERS()
    has_abs = cs.ABSLevel()
    max_rpm = cs.getMaxRPM()
    max_fuel = cs.getMaxFuel()

    car_count = si.getCarsCount()

    # TEST ZONE
    # ############
    ac.console(str(driver_name))
    ac.console(str(has_drs))
    ac.console(str(has_ers))
    ac.console(str(has_kers))
    ac.console(str(has_abs))
    ac.console(str(max_rpm))
    ac.console("Car count: " + str(car_count))
    ac.console(str(max_fuel))
    # #############

    display = ac.newApp("DGT")
    ac.setSize(display, 300, 300)

    # Display settings for testing
    # Increase the third variable of ac.setPosition() by 30 for every variable added
    l_drag = ac.addLabel(display, "Drag: ()")
    l_lift_front = ac.addLabel(display, "Lift front: ()")
    l_lift_rear = ac.addLabel(display, "Lift rear: ()")
    ac.setPosition(l_drag, 3, 30)
    ac.setPosition(l_lift_front, 3, 60)
    ac.setPosition(l_lift_rear, 3, 90)

    csv.init()
    pickle.init()

    return "DGT"


def acUpdate(deltaT):
    global writer
    global session_status
    # GLOBAL VARIABLES FOR LABELS ON THE DISPLAY
    global l_drag, l_lift_front, l_lift_rear
    # GLOBAL VARIABLES FOR TRACK CONDITIONS
    global wind_speed, wind_dir
    # GLOBAL VARIABLES FOR INPUT
    global gas_input, brake_input, steer_input, clutch
    # GLOBAL VARIABLES FOR CAR INFO
    global car_speed,  rpm, delta_ahead, delta_behind, location, world_location, gear, damage, fuel
    # GLOBAL VARIABLES FOR LAP TIMES
    global current_lap, last_lap, best_lap, splits, lap_count, is_invalid, split, track_pos
    # GLOBAL VARIABLES FOR AERO
    global drag, lift_front, lift_rear
    # GLOBAL VARIABLES FOR TYRES

    ts = round(time.time() * 1000)

    session_status = si.getSessionStatus()
    # ac.console(str(session_status))

    # Input info functions called
    gas_input = ii.getGasInput(car_id)
    brake_input = ii.getBrakeInput(car_id)
    steer_input = ii.getSteerInput(car_id)
    clutch = ii.getClutch(car_id)

    inputList = [gas_input, brake_input, steer_input, ts]
    dInputInfo = {
        "gas": gas_input,
        "brake": brake_input,
        "steering": steer_input,
        "timestamp": ts
    }

    json.dump(dInputInfo, inputFile)
    pickle.inputPickler.dump(inputList)
    csv.inputWriter.writerow([gas_input, brake_input, steer_input, ts])


    # Car info functions called
    car_speed = ci.getSpeed(car_id)
    rpm = ci.getRPM(car_id)
    delta_ahead = ci.getDeltaToCarAhead(True)
    delta_behind = ci.getDeltaToCarBehind(True)
    location = ci.getLocation(car_id)
    world_location = ci.getWorldLocation()
    is_in_pit = ci.getCarInPit()
    gear = ci.getFormattedGear(car_id,True)
    position = ci.getPosition(car_id)
    drs_enabled = ci.getDRSEnabled()
    damage = ci.getCarDamage("front")
    fuel = ci.getFuel()

    carList = [car_speed, rpm, gear, ts]
    dCarInfo = {
        "car_speed": car_speed,
        "rpm": rpm,
        "gear": gear,
        "timestamp": ts
    }

    json.dump(dCarInfo, carFile)
    pickle.carPickler.dump(carList)
    csv.carWriter.writerow([car_speed, rpm, gear, ts])

    # Lap info functions called
    current_lap = li.getCurrentLapTime(car_id)
    last_lap = li.getLastLapTime(car_id)
    best_lap = li.getBestLapTime(car_id)
    splits = li.getSplits(car_id)
    split1 = splits[0]
    split2 = splits[1]
    split3 = splits[2]
    lap_count = li.getLapCount(car_id)
    lap_delta = li.getLapDelta(car_id)
    is_invalid = li.getInvalid(car_id)
    split = li.getSplit()
    lap_pos = ci.getLocation(car_id)

    lapList = [lap_pos, lap_count, current_lap, last_lap, best_lap, lap_delta, split1, split2, split3, str(is_invalid), ts]
    dLapInfo = {
        "lap_position": lap_pos,
        "lap_count": lap_count,
        "current_lap": current_lap,
        "last_lap": last_lap,
        "best_lap": best_lap,
        "split1": split1,
        "split2": split2,
        "split3": split3,
        "invalid:": str(is_invalid),
        "timestamp": ts
    }

    json.dump(dLapInfo, lapFile)
    pickle.lapPickler.dump(lapList)
    csv.lapWriter.writerow([lap_pos, lap_count, current_lap, last_lap, best_lap, lap_delta, split1, split2, split3, str(is_invalid), ts])

    # Tyre functions called
    tyrewear = ti.getTyreWearValue(0)
    dirty = ti.getTyreDirtyLevel(0)
    temp_inner = ti.getTyreTemperature(0, 'i')
    temp_middle = ti.getTyreTemperature(0, 'm')
    temp_outer = ti.getTyreTemperature(0, 'o')
    temp_core = ti.getTyreTemperature(0, 'c')
    tyre_pressure = ti.getTyrePressure(0)
    brake_temp = ti.getBrakeTemperature(2)

    tyreList = [tyrewear, dirty, temp_inner, temp_middle, temp_outer, temp_core, tyre_pressure, brake_temp]
    dTyreInfo = {
        "tyrewear": tyrewear,
        "dirty": dirty,
        "temp_inner": temp_inner,
        "temp_middle": temp_middle,
        "temp_outer": temp_outer,
        "temp_core": temp_core,
        "tyre_pressure": tyre_pressure,
        "brake_temp": brake_temp
    }

    json.dump(tyreList, tyreFile)
    pickle.tyrePickler.dump(tyreList)
    csv.tyreWriter.writerow([tyrewear, dirty, temp_inner, temp_middle, temp_outer, temp_core, tyre_pressure, brake_temp])


    # if session_status == 2 and not is_in_pit:
    #     with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/TestData/lap.txt', 'a') as lap_file:
    #         lap_file.write((str(dLapInfo)))
    #         lap_file.write("\n")
    #         lap_file.close()
    # with open(folder + "input.txt", 'a') as lap_file:
    #     lap_file.write((str(dInputInfo)))
    #     lap_file.write("\n")
    #     lap_file.close()
    #     with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/TestData/car.txt', 'a') as lap_file:
    #         lap_file.write((str(dCarInfo)))
    #         lap_file.write("\n")
    #         lap_file.close()

    # Live display
    ac.setText(l_drag, "Tyre pressure: {}".format(tyre_pressure))
    ac.setText(l_lift_front, "Brake temp: {}".format(brake_temp))
    ac.setText(l_lift_rear, "Temp: {}".format(temp_inner))

def acShutdown():
    return
