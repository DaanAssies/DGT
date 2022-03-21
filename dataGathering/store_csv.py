import os
import csv
import time

dirname = os.path.dirname(__file__)

def init():
    cur_time = str(round(time.time()))
    output_dir = os.path.abspath(os.path.join(dirname, cur_time))
    os.makedirs(output_dir)

    global inputWriter

    csvfile = open(os.path.abspath(os.path.join(output_dir, "input.csv")), 'w', newline='')
    inputWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['gas', 'brake', 'steer', 'timestamp']
    inputWriter.writerow(header)

    global carWriter

    csvfile = open(os.path.abspath(os.path.join(output_dir, "car.csv")), 'w', newline='')
    carWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['speed', 'rpm', 'gear', 'timestamp']
    carWriter.writerow(header)

    global lapWriter

    csvfile = open(os.path.abspath(os.path.join(output_dir, "lap.csv")), 'w', newline='')
    lapWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['lap position', 'lap count', 'current lap', 'last lap', 'best lap', 'lap delta', 'split1', 'split2', 'split3', 'invalid', 'timestamp']
    lapWriter.writerow(header)

    global tyreWriter

    csvfile = open(os.path.abspath(os.path.join(output_dir, "tyre.csv")), 'w', newline='')
    tyreWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['tyre wear', 'dirty', 'inner temp', 'middle temp', 'outer temp', 'core temp', 'tyre pressure', 'brake temp' ]
    tyreWriter.writerow(header)