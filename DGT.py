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

    # For JSON dir + file creation
    # os.makedirs(json_dir)
    # global inputFile
    # inputFile = open(os.path.abspath(os.path.join(json_dir, "input.json")), 'w+')
    # global carFile
    # carFile = open(os.path.abspath(os.path.join(json_dir, "car.json")), 'w+')
    # global lapFile
    # lapFile = open(os.path.abspath(os.path.join(json_dir, "lap.json")), 'w+')
    # global tyreFile
    # tyreFile = open(os.path.abspath(os.path.join(json_dir, "tyre.json")), 'w+')

    display = ac.newApp("DGT")
    ac.setSize(display, 300, 300)

    # Display settings for testing
    # Increase the third variable of ac.setPosition() by 30 for every variable added

    # Initialize dirs and files
    csv.init()
    # pickle.init()

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
    global car_speed, rpm, delta_ahead, delta_behind, location, world_location, gear, damage, fuel
    # GLOBAL VARIABLES FOR LAP TIMES
    global current_lap, last_lap, best_lap, splits, lap_count, is_invalid, split, track_pos
    # GLOBAL VARIABLES FOR AERO
    global drag, lift_front, lift_rear
    # GLOBAL VARIABLES FOR TYRES

    ts = round(time.time() * 1000)

    session_status = si.getSessionStatus()

    # Input info functions called
    gas_input = ii.getGasInput(car_id)
    brake_input = ii.getBrakeInput(car_id)
    steer_input = ii.getSteerInput(car_id)
    clutch = ii.getClutch(car_id)

    # inputList = [gas_input, brake_input, steer_input, ts]
    # dInputInfo = {
    #     "gas": gas_input,
    #     "brake": brake_input,
    #     "steering": steer_input,
    #     "timestamp": ts
    # }
    # 
    # json.dump(dInputInfo, inputFile)
    # pickle.inputPickler.dump(inputList)
    csv.inputWriter.writerow([gas_input, brake_input, steer_input, ts])

    # Car info functions called
    car_speed = ci.getSpeed(car_id)
    rpm = ci.getRPM(car_id)
    delta_ahead = ci.getDeltaToCarAhead(True)
    delta_behind = ci.getDeltaToCarBehind(True)
    world_location = ci.getWorldLocation()
    is_in_pit = ci.getCarInPit()
    gear = ci.getFormattedGear(car_id, True)
    position = ci.getPosition(car_id)
    drs_enabled = ci.getDRSEnabled()
    damage = ci.getCarDamage("front")
    fuel = ci.getFuel()

    # carList = [car_speed, rpm, gear, ts]
    # dCarInfo = {
    #     "car_speed": car_speed,
    #     "rpm": rpm,
    #     "gear": gear,
    #     "timestamp": ts
    # }
    # 
    # json.dump(dCarInfo, carFile)
    # pickle.carPickler.dump(carList)
    csv.carWriter.writerow([car_speed, rpm, gear, fuel, ts])

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

    # lapList = [lap_pos, lap_count, current_lap, last_lap, best_lap, lap_delta, split1, split2, split3, str(is_invalid), ts]
    # dLapInfo = {
    #     "lap_position": lap_pos,
    #     "lap_count": lap_count,
    #     "current_lap": current_lap,
    #     "last_lap": last_lap,
    #     "best_lap": best_lap,
    #     "split1": split1,
    #     "split2": split2,
    #     "split3": split3,
    #     "invalid:": str(is_invalid),
    #     "timestamp": ts
    # }
    # 
    # json.dump(dLapInfo, lapFile)
    # pickle.lapPickler.dump(lapList)
    csv.lapWriter.writerow(
        [lap_pos, lap_count, current_lap, last_lap, best_lap, lap_delta, split1, split2, split3, str(is_invalid), ts])

    # Tyre functions called
    tyrewear0 = ti.getTyreWearValue(0)
    dirty0 = ti.getTyreDirtyLevel(0)
    temp_inner0 = ti.getTyreTemperature(0, 'i')
    temp_middle0 = ti.getTyreTemperature(0, 'm')
    temp_outer0 = ti.getTyreTemperature(0, 'o')
    temp_core0 = ti.getTyreTemperature(0, 'c')
    tyre_pressure0 = ti.getTyrePressure(0)
    slip_ratio0, slip_ratio1, slip_ratio2, slip_ratio3 = ti.getSlipRatio()
    slip_angle0, slip_angle1, slip_angle2, slip_angle3 = ti.getslipAngle(0)
    tyrewear1 = ti.getTyreWearValue(1)
    dirty1 = ti.getTyreDirtyLevel(1)
    temp_inner1 = ti.getTyreTemperature(1, 'i')
    temp_middle1 = ti.getTyreTemperature(1, 'm')
    temp_outer1 = ti.getTyreTemperature(1, 'o')
    temp_core1 = ti.getTyreTemperature(1, 'c')
    tyre_pressure1 = ti.getTyrePressure(1)
    tyrewear2 = ti.getTyreWearValue(2)
    dirty2 = ti.getTyreDirtyLevel(2)
    temp_inner2 = ti.getTyreTemperature(2, 'i')
    temp_middle2 = ti.getTyreTemperature(2, 'm')
    temp_outer2 = ti.getTyreTemperature(2, 'o')
    temp_core2 = ti.getTyreTemperature(2, 'c')
    tyre_pressure2 = ti.getTyrePressure(2)
    tyrewear3 = ti.getTyreWearValue(3)
    dirty3 = ti.getTyreDirtyLevel(3)
    temp_inner3 = ti.getTyreTemperature(3, 'i')
    temp_middle3 = ti.getTyreTemperature(3, 'm')
    temp_outer3 = ti.getTyreTemperature(3, 'o')
    temp_core3 = ti.getTyreTemperature(3, 'c')
    tyre_pressure3 = ti.getTyrePressure(3)
    brake_temp = ti.getBrakeTemperature(2)

    # tyreList = [tyrewear0, dirty0, temp_inner0, temp_middle0, temp_outer0, temp_core0, tyre_pressure0, ts]
    # dTyreInfo = {
    #     "tyrewear": tyrewear,
    #     "dirty": dirty,
    #     "temp_inner": temp_inner0,
    #     "temp_middle": temp_middle0,
    #     "temp_outer": temp_outer0,
    #     "temp_core": temp_core0,
    #     "tyre_pressure": tyre_pressure,
    #     "brake_temp": brake_temp,
    #     "timestamp": ts
    # }
    #
    # json.dump(tyreList, tyreFile)
    # pickle.tyrePickler.dump(tyreList)
    csv.tyreWriter.writerow(
        [tyrewear0, dirty0, temp_inner0, temp_middle0, temp_outer0, temp_core0, tyre_pressure0, slip_ratio0, slip_angle0, tyrewear1, dirty1,
         temp_inner1, temp_middle1, temp_outer1, temp_core1, tyre_pressure1, slip_ratio1, slip_angle1, tyrewear2, dirty2, temp_inner2,
         temp_middle2, temp_outer2, temp_core2, tyre_pressure2, slip_ratio2, slip_angle2, tyrewear3, dirty3, temp_inner3, temp_middle3,
         temp_outer3, temp_core3, tyre_pressure3, slip_ratio3, slip_angle3, brake_temp, ts])


def acShutdown():
    return
