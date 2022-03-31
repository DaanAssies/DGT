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

import functions.car_info as ci
import functions.input_info as ii
import functions.lap_info as li
import functions.session_info as si
import functions.tyre_info as ti
import dataGathering.store_csv as csv
import os

dirname = os.path.dirname(__file__)
outputs = os.path.abspath(os.path.join(dirname, "dataGathering"))

car_id = 0
cur_time = str(round(time.time()))
json_dir = os.path.abspath(os.path.join(outputs, "out", cur_time)) + 'j'


def acMain(ac_version):
    global csvfile, writer

    display = ac.newApp("DGT")
    ac.setSize(display, 300, 300)

    # Initialize dirs and files
    csv.init()

    # Write to session.csv with information about the session
    session_type = si.get_session_type()
    car = si.get_car_name()
    car_ballast = si.get_car_ballast()
    caster = si.get_caster()
    radius = si.get_radius()
    min_height = si.get_car_min_height()
    ffb = si.get_car_ffb()
    track = si.get_track_name()
    track_config = si.get_track_config()
    track_len = si.get_track_length()

    csv.sessionWriter.writerow([session_type, car, car_ballast, caster, radius, min_height, ffb, track, track_config, track_len])



    return "DGT"


def acUpdate(deltaT):
    global writer

    ts = round(time.time() * 1000)

    session_status = si.get_session_status()

    # Input info functions called
    gas_input = ii.get_gas_input(car_id)
    brake_input = ii.get_brake_input(car_id)
    steer_input = ii.get_steer_input(car_id)
    clutch = ii.get_clutch(car_id)
    last_ff = ii.get_last_ff()

    csv.inputWriter.writerow([gas_input, brake_input, steer_input, clutch, last_ff, ts])

    # Car info functions called.
    car_speed = ci.get_speed(car_id)
    rpm = ci.get_rpm(car_id)
    gear = ci.get_gear(car_id, True)
    drs_enabled = ci.get_drs_enabled()
    damage = ci.get_car_damage("front")
    fuel = ci.get_fuel()
    cg_height = ci.get_cg_height()
    dt_speed = ci.get_drive_train_speed()

    csv.carWriter.writerow([car_speed, rpm, gear, fuel, drs_enabled, damage, cg_height, dt_speed, ts])

    # Lap info functions called
    current_lap = li.get_current_lap_time(car_id)
    last_lap = li.get_last_lap_time(car_id)
    best_lap = li.get_best_lap_time(car_id)
    lap_count = li.get_lap_count(car_id)
    lap_delta = li.get_lap_delta(car_id)
    is_invalid = li.get_invalid(car_id)
    split = li.get_split()
    lap_pos = ci.get_location(car_id)

    # Does not work on some version of ac
    # splits = li.get_splits(car_id)
    # split1 = splits[0]
    # split2 = splits[1]
    # split3 = splits[2]

    csv.lapWriter.writerow(
        [lap_pos, lap_count, current_lap, last_lap, best_lap, lap_delta, split, str(is_invalid), ts])

    # Tyre functions called
    tyrewear0 = ti.get_tyre_wear_value(0)
    dirty0 = ti.get_tyre_dirty(0)
    temp_inner0 = ti.get_tyre_temp(0, 'i')
    temp_middle0 = ti.get_tyre_temp(0, 'm')
    temp_outer0 = ti.get_tyre_temp(0, 'o')
    temp_core0 = ti.get_tyre_temp(0, 'c')
    tyre_pressure0 = ti.get_tyre_pressure(0)
    slip_ratio0, slip_ratio1, slip_ratio2, slip_ratio3 = ti.get_slip_ratio()
    slip_angle0, slip_angle1, slip_angle2, slip_angle3 = ti.get_slip_angle()
    tyrewear1 = ti.get_tyre_wear_value(1)
    dirty1 = ti.get_tyre_dirty(1)
    temp_inner1 = ti.get_tyre_temp(1, 'i')
    temp_middle1 = ti.get_tyre_temp(1, 'm')
    temp_outer1 = ti.get_tyre_temp(1, 'o')
    temp_core1 = ti.get_tyre_temp(1, 'c')
    tyre_pressure1 = ti.get_tyre_pressure(1)
    tyrewear2 = ti.get_tyre_wear_value(2)
    dirty2 = ti.get_tyre_dirty(2)
    temp_inner2 = ti.get_tyre_temp(2, 'i')
    temp_middle2 = ti.get_tyre_temp(2, 'm')
    temp_outer2 = ti.get_tyre_temp(2, 'o')
    temp_core2 = ti.get_tyre_temp(2, 'c')
    tyre_pressure2 = ti.get_tyre_pressure(2)
    tyrewear3 = ti.get_tyre_wear_value(3)
    dirty3 = ti.get_tyre_dirty(3)
    temp_inner3 = ti.get_tyre_temp(3, 'i')
    temp_middle3 = ti.get_tyre_temp(3, 'm')
    temp_outer3 = ti.get_tyre_temp(3, 'o')
    temp_core3 = ti.get_tyre_temp(3, 'c')
    tyre_pressure3 = ti.get_tyre_pressure(3)
    brake_temp = ti.get_brake_temp(2)
    camber0, camber1, camber2, camber3 = ti.get_camber()
    torque0, torque1, torque2, torque3 = ti.get_torque()
    load0, load1, load2, load3 = ti.get_load()
    sus0, sus1, sus2, sus3 = ti.get_suspension_travel()
    cont_normal0 = ti.get_tyre_contact_normal(0, 0)
    cont_normal1 = ti.get_tyre_contact_normal(0, 1)
    cont_normal2 = ti.get_tyre_contact_normal(0, 2)
    cont_normal3 = ti.get_tyre_contact_normal(0, 3)
    cont_point0 = ti.get_tyre_contact_point(0, 0)
    cont_point1 = ti.get_tyre_contact_point(0, 1)
    cont_point2 = ti.get_tyre_contact_point(0, 2)
    cont_point3 = ti.get_tyre_contact_point(0, 3)

    csv.tyreWriter.writerow(
        [tyrewear0, dirty0, temp_inner0, temp_middle0, temp_outer0, temp_core0, tyre_pressure0, slip_ratio0,
         slip_angle0, camber0, torque0, load0, sus0, cont_normal0, cont_point0,
         tyrewear1, dirty1, temp_inner1, temp_middle1, temp_outer1, temp_core1, tyre_pressure1, slip_ratio1,
         slip_angle1, camber1, torque1, load1, sus1, cont_normal1, cont_point1,
         tyrewear2, dirty2, temp_inner2, temp_middle2, temp_outer2, temp_core2, tyre_pressure2, slip_ratio2,
         slip_angle2, camber2, torque2, load2, sus2, cont_normal2, cont_point2,
         tyrewear3, dirty3, temp_inner3, temp_middle3, temp_outer3, temp_core3, tyre_pressure3, slip_ratio3,
         slip_angle3, camber3, torque3, load3, sus3, cont_normal3, cont_point3,
         ts])

    # Race functions
    delta_ahead = ci.get_delta_to_car_ahead(True)
    delta_behind = ci.get_delta_to_car_behind(True)
    world_location = ci.get_world_location()
    is_in_pit = ci.get_car_in_pit_lane()
    position = ci.get_position(car_id)


def acShutdown():
    return
