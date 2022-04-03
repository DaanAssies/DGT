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

    header = ['gas', 'brake', 'steer', 'clutch', 'force feedback', 'timestamp']
    inputWriter.writerow(header)

    global carWriter

    csvfile = open(os.path.abspath(os.path.join(output_dir, "car.csv")), 'w', newline='')
    carWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['speed', 'rpm', 'gear', 'fuel', 'drs available', 'drs enabled', 'damage', 'cg height', 'drive train speed', 'velocity', 'acceleration', 'tc in use', 'abs in use', 'brake bias', 'engine brake mapping', 'timestamp']
    carWriter.writerow(header)

    global lapWriter

    csvfile = open(os.path.abspath(os.path.join(output_dir, "lap.csv")), 'w', newline='')
    lapWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['lap position', 'lap count', 'current lap', 'current sector', 'last lap', 'best lap', 'lap delta', 'split', 'invalid', 'timestamp']
    lapWriter.writerow(header)

    global tyreWriter

    csvfile = open(os.path.abspath(os.path.join(output_dir, "tyre.csv")), 'w', newline='')
    tyreWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['tyre wear0', 'dirty0', 'inner temp0', 'middle temp0', 'outer temp0', 'core temp0', 'tyre pressure0', 'slip ratio0',
              'slip angle0', 'camber0', 'torque0', 'load0', 'sus travel0', 'contact normal0', 'contact point0', 'contact heading0', 'angular speed0',
              'tyre wear1', 'dirty1', 'inner temp1', 'middle temp1', 'outer temp1', 'core temp1', 'tyre pressure1', 'slip ratio1',
              'slip angle1', 'camber1', 'torque1', 'load1', 'sus travel1', 'contact normal1', 'contact point1', 'contact heading1', 'angular speed1',
              'tyre wear2', 'dirty2', 'inner temp2','middle temp2', 'outer temp2', 'core temp2', 'tyre pressure2', 'slip ratio2',
              'slip angle2', 'camber2', 'torque2', 'load2', 'sus travel2', 'contact normal2', 'contact point2', 'contact heading2', 'angular speed2',
              'tyre wear3','dirty3', 'inner temp3', 'middle temp3', 'outer temp3', 'core temp3', 'tyre pressure3', 'slip ratio3',
              'slip angle3', 'camber3', 'torque3', 'load3', 'sus travel3', 'contact normal3', 'contact point3', 'contact heading3', 'angular speed3',
              'timestamp']
    tyreWriter.writerow(header)

    global sessionWriter
    csvfile = open(os.path.abspath(os.path.join(output_dir, "session.csv")), 'w', newline='')
    sessionWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['driver name', 'session type', 'car', 'ballast', 'caster', 'tyre radius', 'min height', 'max torque', 'max power', 'max rpm', 'max sus travel', 'max turbo', 'tyre compound', 'ffb', 'track', 'track config', 'track length', 'air temp', 'air density', 'track temp', 'surface grip', 'assists']
    sessionWriter.writerow(header)
