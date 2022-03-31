import pickle
import os
import csv
import time

dirname = os.path.dirname(__file__)

def init():
    cur_time = str(round(time.time()))
    output_dir = os.path.abspath(os.path.join(dirname, "out", cur_time)) + 'p'
    os.makedirs(output_dir)

    inputFile = open(os.path.abspath(os.path.join(output_dir, "input.pkl")), 'wb+')
    carFile = open(os.path.abspath(os.path.join(output_dir, "car.pkl")), 'wb+')
    lapFile = open(os.path.abspath(os.path.join(output_dir, "lap.pkl")), 'wb+')
    tyreFile = open(os.path.abspath(os.path.join(output_dir, "tyre.pkl")), 'wb+')

    global inputPickler
    inputPickler = pickle.Pickler(inputFile)

    global carPickler
    carPickler = pickle.Pickler(carFile)

    global lapPickler
    lapPickler = pickle.Pickler(lapFile)

    global tyrePickler
    tyrePickler = pickle.Pickler(tyreFile)