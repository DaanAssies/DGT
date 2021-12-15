import functions.tyre_info
import functions.input_info
import functions.session_info
import functions.lap_info
import functions.car_info
import functions.car_stats
import functions.aero_info
from datetime import datetime

import numpy as np

global collection_array

class DataCollector:
    def __init__(self):
        self._capture_tyre_info = True
        self._capture_input_info = True
        self._capture_session_info = True
        self._capture_lap_info = True
        self._capture_car_info = True
        self._capture_car_stats = True
        self._capture_aero_info = False  # currently turned off by default due to data capture issues

    @classmethod
    def activate_module_info(cls, module):
        module = True

    @classmethod
    def deactivate_module_info(cls, module):
        module = False

    def capture_data(self):
        current_timestamp = datetime.now()

        date_array = np.array([current_timestamp], dtype=([('Timestamp', 'datetime')]))
        collection_array.hstack(date_array)

        if self._capture_tyre_info:
            tyre_array = self.capture_tyre_info()
            collection_array.hstack(tyre_array)

        if self._capture_input_info:
            input_array = self.capture_input_info()
            collection_array.hstack(input_array)

        if self._capture_session_info:
            session_array = self.capture_session_info()
            collection_array.hstack(session_array)

        if self._capture_lap_info:
            lap_array = self.capture_lap_info()
            collection_array.hstack(lap_array)

        if self._capture_car_info:
            car_array = self.capture_car_info()
            collection_array.hstack(car_array)

        if self._capture_car_stats:
            car_stats_array = self.capture_car_stats()
            collection_array.hstack(car_stats_array)

        if self._capture_aero_info:
            print("placeholder, aero data currently bugged")

        return collection_array

    @staticmethod
    def capture_tyre_info():
        tyre_wear_fl = functions.tyre_info.get_tyre_wear_value(0)
        tyre_wear_fr = functions.tyre_info.get_tyre_wear_value(1)
        tyre_wear_rl = functions.tyre_info.get_tyre_wear_value(2)
        tyre_wear_rr = functions.tyre_info.get_tyre_wear_value(3)

        tyre_dirt_fl = functions.tyre_info.get_tyre_dirty(0)
        tyre_dirt_fr = functions.tyre_info.get_tyre_dirty(1)
        tyre_dirt_rl = functions.tyre_info.get_tyre_dirty(2)
        tyre_dirt_rr = functions.tyre_info.get_tyre_dirty(3)

        tyre_temp_fl_inner = functions.tyre_info.get_tyre_temp(0, "i")
        tyre_temp_fl_middle = functions.tyre_info.get_tyre_temp(0, "m")
        tyre_temp_fl_outer = functions.tyre_info.get_tyre_temp(0, "o")
        tyre_temp_fl_core = functions.tyre_info.get_tyre_temp(0, "c")

        tyre_temp_fr_inner = functions.tyre_info.get_tyre_temp(1, "i")
        tyre_temp_fr_middle = functions.tyre_info.get_tyre_temp(1, "m")
        tyre_temp_fr_outer = functions.tyre_info.get_tyre_temp(1, "o")
        tyre_temp_fr_core = functions.tyre_info.get_tyre_temp(1, "c")

        tyre_temp_rl_inner = functions.tyre_info.get_tyre_temp(2, "i")
        tyre_temp_rl_middle = functions.tyre_info.get_tyre_temp(2, "m")
        tyre_temp_rl_outer = functions.tyre_info.get_tyre_temp(2, "o")
        tyre_temp_rl_core = functions.tyre_info.get_tyre_temp(2, "c")

        tyre_temp_rr_inner = functions.tyre_info.get_tyre_temp(3, "i")
        tyre_temp_rr_middle = functions.tyre_info.get_tyre_temp(3, "m")
        tyre_temp_rr_outer = functions.tyre_info.get_tyre_temp(3, "o")
        tyre_temp_rr_core = functions.tyre_info.get_tyre_temp(3, "c")

        tyre_pressure_fl = functions.tyre_info.get_tyre_pressure(0)
        tyre_pressure_fr = functions.tyre_info.get_tyre_pressure(1)
        tyre_pressure_rl = functions.tyre_info.get_tyre_pressure(2)
        tyre_pressure_rr = functions.tyre_info.get_tyre_pressure(3)

        brake_temp_fl = functions.tyre_info.get_brake_temp(0)
        brake_temp_fr = functions.tyre_info.get_brake_temp(1)
        brake_temp_rl = functions.tyre_info.get_brake_temp(2)
        brake_temp_rr = functions.tyre_info.get_brake_temp(3)

        tyre_wear_array = np.array([(tyre_wear_fl, tyre_wear_fr, tyre_wear_rl, tyre_wear_rr)],
                                   dtype=[('Tyre Wear Front Left', 'float'), ('Tyre Wear Front Right', 'float'),
                                          ('Tyre Wear Rear Left', 'float'), ('Tyre Waer Rear Right', 'float')])

        tyre_dirt_array = np.array([(tyre_dirt_fl, tyre_dirt_fr, tyre_dirt_rl, tyre_dirt_rr)],
                                   dtype=[('Tyre Dirt Front Left', 'float'), ('Tyre Dirt Front Right', 'float'),
                                          ('Tyre Dirt Rear Left', 'float'), ('Tyre Dirt Rear Right', 'float')])

        tyre_temp_array = np.array([(tyre_temp_fl_inner, tyre_temp_fl_middle, tyre_temp_fl_outer, tyre_temp_fl_core,
                                     tyre_temp_fr_inner, tyre_temp_fr_middle, tyre_temp_fr_outer, tyre_temp_fr_core,
                                     tyre_temp_rl_inner, tyre_temp_rl_middle, tyre_temp_rl_outer, tyre_temp_rl_core,
                                     tyre_temp_rr_inner, tyre_temp_rr_middle, tyre_temp_rr_outer, tyre_temp_rr_core)
                                    ],
                                   dtype=[('Tyre Temp Front Left Inner', 'float'),
                                          ('Tyre Temp Front Left Middle', 'float'),
                                          ('Tyre Temp Front Left Outer', 'float'),
                                          ('Tyre Temp Front Left Core', 'float'),
                                          ('Tyre Temp Front Right Inner', 'float'),
                                          ('Tyre Temp Front Right Middle', 'float'),
                                          ('Tyre Temp Front Right Outer', 'float'),
                                          ('Tyre Temp Front Right Core', 'float'),
                                          ('Tyre Temp Rear Left Inner', 'float'),
                                          ('Tyre Temp Rear Left Middle', 'float'),
                                          ('Tyre Temp Rear Left Outer', 'float'),
                                          ('Tyre Temp Rear Left Core', 'float'),
                                          ('Tyre Temp Rear Right Inner', 'float'),
                                          ('Tyre Temp Rear Right Middle', 'float'),
                                          ('Tyre Temp Rear Right Outer', 'float'),
                                          ('Tyre Temp Rear Right Core', 'float')
                                          ])

        tyre_pressure_array = np.array([(tyre_pressure_fl, tyre_pressure_fr, tyre_pressure_rl, tyre_pressure_rr)],
                                       dtype=[('Tyre Pressure Front Left', 'float'),
                                              ('Tyre Pressure Front Right', 'float'),
                                              ('Tyre Pressure Rear Left', 'float'),
                                              ('Tyre Pressure Rear Right', 'float')])

        brake_temperature_array = np.array([(brake_temp_fl, brake_temp_fr, brake_temp_rl, brake_temp_rr)],
                                           dtype=[('Break Temperature Front Left', 'float'),
                                                  ('Break Temperature Front Right', 'float'),
                                                  ('Break Temperature Rear Left', 'float'),
                                                  ('Break Temperature Rear Right', 'float')])

        tyre_array = np.hstack(tyre_wear_array, tyre_dirt_array, tyre_temp_array, tyre_pressure_array,
                               brake_temperature_array)

        return tyre_array
    
    @staticmethod
    def capture_input_info():
        gas_input = functions.input_info.get_gas_input()
        brake_input = functions.input_info.get_brake_input()
        clutch_input = functions.input_info.get_clutch()
        steer_input = functions.input_info.get_steer_input()

        input_array = np.array([(gas_input, brake_input, clutch_input, steer_input)],
                               dtype=[('Gas Input', 'float'), ('Brake Input', 'float'),
                                      ('Clutch Input', 'float'), ('Steer Input', 'float')])

        return input_array

    @staticmethod
    def capture_session_info():
        session_type = functions.session_info.get_session_type()
        driver_name = functions.session_info.get_driver_name()
        car_name = functions.session_info.get_car_name()
        track_name = functions.session_info.get_track_name()
        track_config = functions.session_info.get_track_config()
        track_length = functions.session_info.get_track_length()
        cars_count = functions.session_info.get_cars_count()
        session_status = functions.session_info.get_session_status()

        session_type_array = np.array([session_type], dtype=['Session Type'])
        string_info_array = np.array([(driver_name, car_name, track_name, track_config)],
                                     dtype=[('Driver Name', 'string'), ('Car Name', 'string'),
                                            ('Track Name', 'string'), ('Track Config', 'string')])
        float_info_array = np.array([track_length], dtype=[('Track length', 'float')])
        int_info_array = np.array([(cars_count, session_status)],
                                  dtype=[('Cars Count', 'int'), ('Session Status', 'int')])

        session_array = np.hstack(session_type_array, string_info_array, float_info_array, int_info_array)

        return session_array

    @staticmethod
    def capture_lap_info():
        current_lap_time_ms = functions.lap_info.get_current_lap_time()
        current_lap_time_str = functions.lap_info.get_current_lap_time(formatted=True)

        last_lap_time_ms = functions.lap_info.get_last_lap_time()
        last_lap_time_str = functions.lap_info.get_last_lap_time(formatted=True)

        best_lap_time_ms = functions.lap_info.get_best_lap_time()
        best_lap_time_str = functions.lap_info.get_best_lap_time(formatted=True)

        splits_ms = functions.lap_info.get_splits()
        splits_str = functions.lap_info.get_splits(formatted=True)

        last_sector = functions.lap_info.get_split()

        invalid_lap = functions.lap_info.get_invalid()

        lap_count = functions.lap_info.get_lap_count()

        race_laps = functions.lap_info.get_laps()

        lap_delta = functions.lap_info.get_lap_delta()

        lap_info_array = np.array([(current_lap_time_ms, current_lap_time_str, last_lap_time_ms, last_lap_time_str,
                                    best_lap_time_ms, best_lap_time_str, splits_ms, splits_str, last_sector,
                                    invalid_lap, lap_count, race_laps, lap_delta)],
                                  dtype=[('Current Lap Time milliseconds', 'int'), ('Current Lap Time', 'string'),
                                         ('Last Lap Time milliseconds', 'int'), ('Last Lap Time', 'string'),
                                         ('Best Lap Time milliseconds', 'int'), ('Best Lap Time', 'string'),
                                         ('Splits milliseconds', 'list'), ('Splits', 'list'),
                                         ('Last Sector', 'string'), ('Invalid Lap', 'bool'),
                                         ('Lap Count', 'int'), ('Race Laps', 'string'),
                                         ('Lap Delta', 'float')])

        return lap_info_array

    @staticmethod
    def capture_car_info():
        current_speed_kmh = functions.car_info.get_speed()
        current_speed_mph = functions.car_info.get_speed(unit="mph")
        current_speed_ms = functions.car_info.get_speed(unit="ms")

        delta_car_ahead_notformat = functions.car_info.get_delta_to_car_ahead()
        delta_car_ahead_str = functions.car_info.get_delta_to_car_ahead(formatted=True)

        delta_car_behind_notformat = functions.car_info.get_delta_to_car_behind()
        delta_car_behind_str = functions.car_info.get_delta_to_car_behind(formatted=True)

        location_car = functions.car_info.get_location()

        world_location = functions.car_info.get_world_location()

        position = functions.car_info.get_position()

        drs_enabled = functions.car_info.get_drs_enabled()

        current_gear_int = functions.car_info.get_gear()
        current_gear_string = functions.car_info.get_gear(formatted=True)

        current_rpm = functions.car_info.get_rpm()

        current_fuel = functions.car_info.get_fuel()

        amount_of_tyres_off_track = functions.car_info.get_tyres_off_track()

        car_in_pitlane = functions.car_info.get_car_in_pit_lane()

        car_damage_front = functions.car_info.get_car_damage()
        car_damage_rear = functions.car_info.get_car_damage("rear")
        car_damage_left = functions.car_info.get_car_damage("left")
        car_damage_right = functions.car_info.get_car_damage("right")
        car_damage_centre = functions.car_info.get_car_damage("centre")

        car_info_array = np.array([(current_speed_kmh, current_speed_mph, current_speed_ms, delta_car_ahead_notformat,
                                    delta_car_ahead_str, delta_car_behind_notformat, delta_car_behind_str,
                                    location_car, world_location, position, drs_enabled, current_gear_int,
                                    current_gear_string, current_rpm, current_fuel, amount_of_tyres_off_track,
                                    car_in_pitlane, car_damage_front, car_damage_rear, car_damage_left,
                                    car_damage_right, car_damage_centre)], dtype=[('Current Speed KMH', 'float'),
                                                                                  ('Current Speed MPH', 'float'),
                                                                                  ('Current Speed MS', 'float'),
                                                                                  ('Delta Car Ahead', 'float'),
                                                                                  ('Delta Car Ahead Format', 'string'),
                                                                                  ('Delta Car Behind', 'float'),
                                                                                  ('Delta Car Behind Format', 'string'),
                                                                                  ('Car Location', 'float'),
                                                                                  ('World Location', 'list'),
                                                                                  ('Position', 'int'),
                                                                                  ('DRS Enabled', 'bool'),
                                                                                  ('Get Current Gear', 'int'),
                                                                                  ('Get Current Gear Formatted'
                                                                                   , 'string'),
                                                                                  ('Current RPM', 'float'),
                                                                                  ('Current Fuel', 'float'),
                                                                                  ('Amount of tyres off track', 'int'),
                                                                                  ('Car in Pitlane', 'bool'),
                                                                                  ('Car Damage Front', 'float'),
                                                                                  ('Car Damage Rear', 'float'),
                                                                                  ('Car Damage Left', 'float'),
                                                                                  ('Car Damage Right', 'float'),
                                                                                  ('Car Damage Centre', 'float')])

        return car_info_array

    @staticmethod
    def capture_car_stats():
        has_drs = functions.car_stats.get_has_drs()
        has_ers = functions.car_stats.get_has_ers()
        has_kers = functions.car_stats.get_has_kers()
        abs_level = functions.car_stats.abs_level()
        max_rpm = functions.car_stats.get_max_rpm()
        max_fuel = functions.car_stats.get_max_fuel()

        car_stats_array = np.array([(has_drs, has_ers, has_kers, abs_level, max_rpm, max_fuel)],
                                   dtype=[('Car Has DRS', 'int'), ('Car Has ERS', 'int'), ('Car Has KERS', 'int'),
                                            ('Car ABS Level', 'int'), ('Car Max RPM', 'int'), ('Car Max Fuel', 'int')])

        return car_stats_array

    @staticmethod
    def capture_aero_info():
        print("Aero info placeholder")


test = DataCollector()

test.capture_data()
