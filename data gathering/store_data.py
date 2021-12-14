import functions.tyre_info
import functions.input_info
import functions.session_info
import functions.lap_info
import functions.car_info
import functions.car_stats
import functions.aero_info
from datetime import datetime

import numpy as np


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

        if self._capture_tyre_info:
            tyre_array = self.capture_tyre_info()

        if self._capture_input_info:
            input_array = self.capture_input_info()

        if self._capture_session_info:
            session_array = self.capture_session_info()

        if self._capture_lap_info:
            print("Capture lap info here")

        if self._capture_car_info:
            print("Capture car info")

        if self._capture_car_stats:
            car_stats_array = self.capture_car_stats()

        if self._capture_aero_info:
            print("placeholder, aero data currently bugged")

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
        print("Lap information")

    @staticmethod
    def capture_car_info():
        print("car information")

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
