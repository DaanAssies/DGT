import numpy as np
import matplotlib.pyplot as plt
import os
import pickle

dirname = os.path.dirname(__file__)
dirdata = os.path.abspath(os.path.join(dirname, "1647866067"))
lap_file = "lap.csv"
car_file = "car.csv"
input_file = "input.csv"
pickledir = os.path.abspath(os.path.join(dirname, "1648490239p"))
picklefile = os.path.join(pickledir, "input.pkl")

def getNumpy(file):
    with open(os.path.join(dirdata, file), 'r'):
        out = np.genfromtxt(os.path.join(dirdata, file), delimiter=',', skip_header=1)
    return out

# Function to get the timestamps where laps get started and where they end. Includes the lap count
def getTimeStamps(array):
    last = 0
    out = []
    for m in array:
        if m[1] > last:
            out.append(m[10])
        last = m[1]
    return out

def getSpeed(file, lap):
    speed = []
    time = []
    array = getNumpy(file)
    timestamps = getTimeStamps(getNumpy(lap_file))
    print(timestamps)
    for m in array:
        if timestamps[(lap - 1)] <= m[3] < timestamps[lap]:
            speed.append(m[0])
            time.append(m[3])
    return speed, time

def getLapPosition(file, lap):
    pos = []
    time = []
    array = getNumpy(file)
    timestamps = getTimeStamps(getNumpy(lap_file))
    for m in array:
        if timestamps[(lap - 1)] <= m[10] < timestamps[lap]:
            pos.append(m[0])
            time.append(m[2])
    return pos, time

def unpickle(file):
    print(file)
    f = open(file, 'rb')
    unpickler = pickle.Unpickler(f)
    res = []
    while True:
        try:
            x = unpickler.load()
            res.append(x)
        except EOFError:
            return res


def createPlot(x, y):
    plt.plot(x, y)
    plt.show()

def main():
    # speed, time = getSpeed(car_file, 1)
    # pos, rel_time = getLapPosition(lap_file, 1)
    # print(len(pos))
    # createPlot(rel_time, speed)
    print(unpickle(picklefile))


if __name__ == "__main__":
    main()
