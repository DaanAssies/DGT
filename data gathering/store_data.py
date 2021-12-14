import functions.tyre_info
import functions.input_info
import functions.session_info
# import functions.lap_info
# import functions.car_info
# import functions.car_stats
# import functions.aero_info
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
            print("Capture input info here")

        if self._capture_session_info:
            print("Capture session info here")

        if self._capture_lap_info:
            print("Capture lap info here")

        if self._capture_car_info:
            print("Capture car info")

        if self._capture_car_stats:
            print("Capture car stats")

        if self._capture_aero_info:
            print("Capture aero info")

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

        tyre_wear_array = np.array([('Tyre Wear Front Left', tyre_wear_fl), ('Tyre Wear Front Right', tyre_wear_fr),
                                    ('Tyre Wear Rear Left', tyre_wear_rl), ('Tyre Wear Rear Right', tyre_wear_rr)],
                                   dtype=[('Variable name', 'string'), ('value', 'float')])

        tyre_dirt_array = np.array([('Tyre Dirt Front Left', tyre_dirt_fl), ('Tyre Dirt Front Right', tyre_dirt_fr),
                                    ('Tyre Dirt Rear Left', tyre_dirt_rl), ('Tyre Dirt Rear Right', tyre_dirt_rr)],
                                   dtype=[('Variable name', 'string'), ('value', 'float')])

        tyre_temp_array = np.array([('Tyre Temp Front Left Inner', tyre_temp_fl_inner),
                                    ('Tyre Temp Front Left Middle', tyre_temp_fl_middle),
                                    ('Tyre Temp Front Left Outer', tyre_temp_fl_outer),
                                    ('Tyre Temp Front Left Core', tyre_temp_fl_core),
                                    ('Tyre Temp Front Right Inner', tyre_temp_fr_inner),
                                    ('Tyre Temp Front Right Middle', tyre_temp_fr_middle),
                                    ('Tyre Temp Front Right Outer', tyre_temp_fr_outer),
                                    ('Tyre Temp Front Right Core', tyre_temp_fr_core),
                                    ('Tyre Temp Rear Left Inner', tyre_temp_rl_inner),
                                    ('Tyre Temp Rear Left Middle', tyre_temp_rl_middle),
                                    ('Tyre Temp Rear Left Outer', tyre_temp_rl_outer),
                                    ('Tyre Temp Rear Left Core', tyre_temp_rl_core),
                                    ('Tyre Temp Rear Right Inner', tyre_temp_rr_inner),
                                    ('Tyre Temp Rear Right Middle', tyre_temp_rr_middle),
                                    ('Tyre Temp Rear Right Outer', tyre_temp_rr_outer),
                                    ('Tyre Temp Rear Right Core', tyre_temp_rr_core)
                                    ],
                                   dtype=[('Variable name', 'string'), ('value', 'float')])

        tyre_pressure_array = np.array([('Tyre Pressure Front Left', tyre_pressure_fl),
                                        ('Tyre Pressure Front Right', tyre_pressure_fr),
                                        ('Tyre Pressure Rear Left', tyre_pressure_rl),
                                        ('Tyre Pressure Rear Right', tyre_pressure_rr)],
                                       dtype=[('Variable name', 'string'), ('value', 'float')])

        brake_temperature_array = np.array([('Brake Temperature Front Left', brake_temp_fl),
                                            ('Brake Temperature Front Right', brake_temp_fr),
                                            ('Brake Temperature Rear Left', brake_temp_rl),
                                            ('Brake Temp Rear Right', brake_temp_rr)],
                                           dtype=[('Variable name', 'string'), ('value', 'float')])

        tyre_array = np.hstack(tyre_wear_array, tyre_dirt_array, tyre_temp_array, tyre_pressure_array,
                               brake_temperature_array)

        return tyre_array
    
    @staticmethod
    def capture_input_info():
        gas_input = functions.input_info.get_gas_input()
        brake_input = functions.input_info.get_brake_input()
        clutch_input = functions.input_info.get_clutch()
        steer_input = functions.input_info.get_steer_input()

        input_array = np.array([('Gas Input', gas_input), ('Brake Input', brake_input), ('Clutch Input', clutch_input),
                                ('Steer Input', steer_input)], dtype=[('Variable name', 'string'), ('value', 'float')])

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

    @staticmethod
    def capture_lap_info():
        print("Lap information")

    @staticmethod
    def capture_car_info():
        print("car information")

    @staticmethod
    def capture_car_stats():
        print("Car stats")

    @staticmethod
    def capture_aero_info():
        print("Aero info")


test = DataCollector()

test.capture_data()
