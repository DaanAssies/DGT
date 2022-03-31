import os
import csv
import time

dirname = os.path.dirname(__file__)

def init():
    cur_time = str(round(time.time()))
    output_dir = os.path.abspath(os.path.join(dirname, "out", cur_time)) + 'c'
    os.makedirs(output_dir)

    global inputWriter

    csvfile = open(os.path.abspath(os.path.join(output_dir, "input.csv")), 'w', newline='')
    inputWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['gas', 'brake', 'steer', 'timestamp']
    inputWriter.writerow(header)

    global carWriter

    csvfile = open(os.path.abspath(os.path.join(output_dir, "car.csv")), 'w', newline='')
    carWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['speed', 'rpm', 'gear', 'fuel', 'timestamp']
    carWriter.writerow(header)

    global lapWriter

    csvfile = open(os.path.abspath(os.path.join(output_dir, "lap.csv")), 'w', newline='')
    lapWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['lap position', 'lap count', 'current lap', 'last lap', 'best lap', 'lap delta', 'split1', 'split2', 'split3', 'invalid', 'timestamp']
    lapWriter.writerow(header)

    global tyreWriter

    csvfile = open(os.path.abspath(os.path.join(output_dir, "tyre.csv")), 'w', newline='')
    tyreWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['tyre wear0', 'dirty0', 'inner temp0', 'middle temp0', 'outer temp0', 'core temp0', 'tyre pressure0', 'slip ratio0', 'slip angle0', 'tyre wear1', 'dirty1', 'inner temp1', 'middle temp1', 'outer temp1', 'core temp1', 'tyre pressure1', 'slip ratio1', 'slip angle1', 'tyre wear2', 'dirty2', 'inner temp2', 'middle temp2', 'outer temp2', 'core temp2', 'tyre pressure2', 'slip ratio2', 'slip angle2', 'tyre wear3', 'dirty3', 'inner temp3', 'middle temp3', 'outer temp3', 'core temp3', 'tyre pressure3', 'slip ratio3', 'slip angle3', 'brake temp', 'timestamp' ]
    tyreWriter.writerow(header)
