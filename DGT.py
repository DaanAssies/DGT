"""
NOTES TO SELF:
.csv ~ 3x more efficient in space:
~1min of logging: .csv = 123kb, .txt = 331kb
"""

import sys
import ac
import acsys
import time
import os
import csv
import numpy as np

import functions.aero_info as ai
import functions.car_info as ci
import functions.car_stats as cs
import functions.input_info as ii
import functions.lap_info as li
import functions.session_info as si
import functions.tyre_info as ti
import data_gathering.store_data

car_id = 0
folder = "apps/python/DGT/outputs/"


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

    global collection_array, data_collector

    # Set the session variables
    driver_name = si.get_driver_name(car_id)
    car_name = si.get_car_name(car_id)
    track_name = si.get_track_name()
    track_config = si.get_track_config()
    track_length = si.get_track_length()
    session_type = si.get_session_type()
    # Set the car stats variables
    has_drs = cs.get_has_drs()
    has_ers = cs.get_has_ers()
    has_kers = cs.get_has_kers()
    has_abs = cs.abs_level()
    max_rpm = cs.get_max_rpm()
    max_fuel = cs.get_max_fuel()

    car_count = si.get_cars_count()

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

    #Here below, we start the data_constructor

    data_collector = data_gathering.store_data.DataCollector()
    collection_array.np.array()


    #Clear output
    # with open(folder + 'input.txt', 'w') as f:
    #     f.write("\n")
    #
    # csvfile = open(folder + 'input.csv', 'w', newline='')
    # input_fields = ['gas', 'brake', 'steer', 'timestamp']
    # writer = csv.writer(csvfile, delimiter=',', quotechar='"',
    #                     quoting=csv.QUOTE_MINIMAL)

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

    session_status = si.get_session_status()
    # ac.console(str(session_status))

    # Input info functions called
    gas_input = ii.get_gas_input(car_id)
    brake_input = ii.get_brake_input(car_id)
    steer_input = ii.get_steer_input(car_id)
    clutch = ii.get_clutch(car_id)

    dInputInfo = {
        "flag": 0,
        "gas": gas_input,
        "brake": brake_input,
        "steering": steer_input,
        "timestamp": ts
    }

    writer.writerow([gas_input, brake_input, steer_input, ts])



    # Car info functions called
    car_speed = ci.get_speed(car_id)
    # ac.console(car_speed)
    rpm = ci.get_rpm(car_id)
    delta_ahead = ci.get_delta_to_car_ahead(True)
    delta_behind = ci.get_delta_to_car_behind(True)
    location = ci.get_location(car_id)
    world_location = ci.get_world_location()
    is_in_pit = ci.get_car_in_pit_lane()
    gear = ci.get_gear(car_id, True)
    position = ci.get_position(car_id)
    drs_enabled = ci.get_drs_enabled()
    damage = ci.get_car_damage("front")
    fuel = ci.get_fuel()

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
    lap_pos = ci.get_location(car_id)

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

    # Aero functions called
    drag = ai.getDrag()
    lift_front = ai.getLiftFront()
    lift_rear = ai.getLiftRear()

    # Tyre functions called
    tyrewear = ti.get_tyre_wear_value(0)
    dirty = ti.get_tyre_dirty(0)
    temp_inner = ti.get_tyre_temp(0, 'i')
    tyre_pressure = ti.get_tyre_pressure(0)
    brake_temp = ti.get_brake_temp(2)


    # if session_status == 2 and not is_in_pit:
    #     with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/TestData/lap.txt', 'a') as lap_file:
    #         lap_file.write((str(dLapInfo)))
    #         lap_file.write("\n")
    #         lap_file.close()
    with open(folder + "input.txt", 'a') as lap_file:
        lap_file.write((str(dInputInfo)))
        lap_file.write("\n")
        lap_file.close()
    #     with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/TestData/car.txt', 'a') as lap_file:
    #         lap_file.write((str(dCarInfo)))
    #         lap_file.write("\n")
    #         lap_file.close()

    # Live display
    ac.setText(l_drag, "Tyre pressure: {}".format(tyre_pressure))
    ac.setText(l_lift_front, "Brake temp: {}".format(brake_temp))
    ac.setText(l_lift_rear, "Temp: {}".format(temp_inner))

    # TEST ZONE
    # ############
    ac.console(str(drag))
    # #############

    collected_array = data_collector.capture_data()
    collection_array.vstack(collected_array)

def acShutdown():
    global csvfile

    np.save('./test.npy', collection_array)
    csvfile.close()

