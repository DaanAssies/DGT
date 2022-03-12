import os
import csv

dirname = os.path.dirname(__file__)
# file_input = os.path.abspath(os.path.join(dirname, "..", "outputs\input.csv"))

def init():
    global inputWriter

    csvfile = open(os.path.abspath(os.path.join(dirname, "..", "outputs\input.csv")), 'w', newline='')
    inputWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['gas', 'brake', 'steer', 'timestamp']
    inputWriter.writerow(header)

    global carWriter

    csvfile = open(os.path.abspath(os.path.join(dirname, "..", "outputs\car.csv")), 'w', newline='')
    carWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['speed', 'rpm', 'gear', 'timestamp']
    carWriter.writerow(header)

    global lapWriter

    csvfile = open(os.path.abspath(os.path.join(dirname, "..", "outputs\lap.csv")), 'w', newline='')
    lapWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['lap position', 'lap count', 'current lap', 'last lap', 'best lap', 'lap delta', 'splits', 'invalid', 'timestamp']
    lapWriter.writerow(header)
